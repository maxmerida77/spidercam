import sys
import os
from collections import deque

# --- LÍNEAS NUEVAS PARA SOLUCIONAR EL ERROR ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
# ----------------------------------------------
import math
import numpy as np
from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import yaml
from spidercam.control.reference_generator import ReferenceGenerator

from spidercam.geometry.cable_kinematics import CableKinematics

class Viewer3D:
    def __init__(self):
        self.app = QtWidgets.QApplication.instance()
        if self.app is None:
            self.app = QtWidgets.QApplication(sys.argv)

        self.window = QtWidgets.QWidget()
        self.window.setWindowTitle('SpiderCam Autónoma - Fase 2 (Cinemática)')
        self.window.resize(1200, 600)

        main_layout = QtWidgets.QHBoxLayout()
        self.window.setLayout(main_layout)

        # SECCIÓN IZQUIERDA: 3D
        self.view_3d = gl.GLViewWidget()
        self.view_3d.setCameraPosition(distance=140, elevation=30, azimuth=45)
        main_layout.addWidget(self.view_3d, stretch=2)

        # NUEVO: Leer configuración maestra
        with open("config/config.yaml", 'r') as file:
            config = yaml.safe_load(file)
            
        self.anchors = np.array(config['stadium']['anchor_points'])
        
        # NUEVO: Actualizar la cuadrícula para el nuevo tamaño FIFA (105x68)
        grid = gl.GLGridItem()
        grid.setSize(x=120, y=80, z=0) 
        grid.setSpacing(x=10, y=10, z=0)
        grid.translate(52.5, 34, 0) # Desplaza la cuadrícula para alinearla a los postes [0, 105]
        self.view_3d.addItem(grid)
        anchor_scatter = gl.GLScatterPlotItem(pos=self.anchors, color=(1, 0.2, 0.2, 1), size=10)
        self.view_3d.addItem(anchor_scatter)

        self.kinematics = CableKinematics(self.anchors)

        self.spidercam_pos = np.array([0, 0, 15])
        self.spidercam_scatter = gl.GLScatterPlotItem(pos=np.array([self.spidercam_pos]), color=(0.2, 1, 0.2, 1), size=15)
        self.view_3d.addItem(self.spidercam_scatter)

        self.cables = []
        for i in range(4):
            cable = gl.GLLinePlotItem(color=(1, 1, 1, 0.8), width=2, antialias=True)
            self.view_3d.addItem(cable)
            self.cables.append(cable)

        # SECCIÓN DERECHA: GRÁFICAS
        panel_2d = QtWidgets.QVBoxLayout()
        main_layout.addLayout(panel_2d, stretch=1)

        # --- NUEVO: Panel de longitudes de cable (Cinemática Inversa) ---
        self.plot_lengths = pg.PlotWidget(title="Longitudes de Cable (Cinemática Inversa)")
        self.plot_lengths.showGrid(x=True, y=True)
        self.plot_lengths.setLabel('left', 'Longitud', units='u')
        self.plot_lengths.setLabel('bottom', 'Frame')
        self.plot_lengths.addLegend()
        panel_2d.addWidget(self.plot_lengths)

        # Un color por cable, mapeado 1:1 con el índice del anclaje correspondiente
        cable_colors = [(255, 80, 80), (80, 255, 80), (80, 160, 255), (255, 220, 80)]
        self.length_curves = []
        for i, color in enumerate(cable_colors):
            curve = self.plot_lengths.plot(
                pen=pg.mkPen(color=color, width=2),
                name=f'Cable {i + 1} (Anclaje {i + 1})'
            )
            self.length_curves.append(curve)

        # Ventana deslizante de las últimas N muestras (evita crecimiento indefinido)
        self.history_size = 300
        self.frame_count = 0
        self.frame_axis = deque(maxlen=self.history_size)
        self.length_history = [deque(maxlen=self.history_size) for _ in range(4)]
        # --- FIN NUEVO ---

        self.plot_error = pg.PlotWidget(title="Error de Seguimiento (PID)")
        self.plot_error.showGrid(x=True, y=True)
        panel_2d.addWidget(self.plot_error)
        self.plot_kalman = pg.PlotWidget(title="Señal Visión vs. Filtro Kalman")
        self.plot_kalman.showGrid(x=True, y=True)
        panel_2d.addWidget(self.plot_kalman)

    def render_frame(self, spidercam_pos):
        """
        Actualiza la posición del punto verde, estira/encoge los cables
        y refresca la gráfica de longitudes calculadas por la cinemática inversa.
        """
        spidercam_pos = np.array(spidercam_pos)

        self.spidercam_scatter.setData(pos=np.array([spidercam_pos]))

        lengths = self.kinematics.calculate_lengths(spidercam_pos)

        for i in range(4):
            pts = np.vstack([self.anchors[i], spidercam_pos])
            self.cables[i].setData(pos=pts)

        # --- NUEVO: actualizar buffers y curvas de longitud ---
        self.frame_count += 1
        self.frame_axis.append(self.frame_count)
        for i in range(4):
            self.length_history[i].append(lengths[i])
            self.length_curves[i].setData(x=list(self.frame_axis), y=list(self.length_history[i]))
        # --- FIN NUEVO ---

    def run(self):
        self.window.show()
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    viewer = Viewer3D()
    ref_gen = ReferenceGenerator()  # Inicializamos el escudo de seguridad

    t = 0
    def update_test():
        global t
        t += 0.05
        
        # El "balón" se vuelve loco y se va a la coordenada X=200, Y=-50 (Muy fuera del estadio)
        x_wild = 52.5 + 150 * math.cos(t) 
        y_wild = 34.0 + 100 * math.sin(t) 
        
        # El limitador lo frena a la fuerza (solo le pasamos [X, Y], el generador pondrá la altura Z fija)
        safe_target = ref_gen.generate([x_wild, y_wild])
        
        # Mandamos la coordenada 100% segura al visor
        viewer.render_frame(safe_target)

    timer = QtCore.QTimer()
    timer.timeout.connect(update_test)
    timer.start(50)
    
    viewer.run()
