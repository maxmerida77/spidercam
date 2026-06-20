"""
Visualización 3D de la simulación (OE-01, RF-07).

Responsabilidad:
    Dibujar el estadio, los 4 cables, el carro/cámara y la trayectoria
    del balón en una ventana 3D, cuadro a cuadro. También aloja las
    gráficas 2D de métricas (trayectoria, error de seguimiento) en la
    misma aplicación.

Implementación: PyQtGraph (pyqtgraph.opengl.GLViewWidget para 3D,
pyqtgraph.PlotWidget para series de tiempo). Ver docs/architecture.md,
sección "Visualización 3D: PyQtGraph", para la justificación de esta
decisión sobre VPython.

Este es el ÚNICO módulo del proyecto que puede importar pyqtgraph/PyQt5.
simulation/ no debe depender de esto bajo ninguna circunstancia.
"""
import pyqtgraph as pg
import pyqtgraph.opengl as gl


class Viewer3D:
    def __init__(self, stadium):
        self.stadium = stadium
        # TODO: inicializar QApplication, GLViewWidget (escena 3D) y
        # PlotWidget(s) (métricas) en un mismo layout

    def render_frame(self, spidercam_position, cable_lengths, ball_position):
        """Renderiza un frame de la simulación."""
        raise NotImplementedError
