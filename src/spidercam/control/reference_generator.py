"""
Generador de referencias para la SpiderCam (OE-05, RF-05).

Responsabilidad:
    A partir de la trayectoria estimada del balón (salida del Kalman, ya
    en coordenadas de cancha), generar la posición objetivo (X, Y, Z) que
    debe alcanzar la SpiderCam en cada instante. Aquí se aplica la
    saturación al volumen de trabajo definido por los anclajes.
"""
import numpy as np
import yaml

class ReferenceGenerator:
    def __init__(self, config_path="config/config.yaml"):
        # Cargamos el archivo de configuración maestro
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
            
        # Extraemos la geometría del estadio y la cámara
        anchors = np.array(config['stadium']['anchor_points'])
        margin = config['spidercam']['workspace_margin_m']
        self.z_fixed = config['spidercam']['z_fixed_m']

        # Calculamos los límites matemáticos del "Muro Invisible"
        # X e Y usan el mínimo/máximo de los postes, recortando el margen de seguridad
        self.x_min = np.min(anchors[:, 0]) + margin
        self.x_max = np.max(anchors[:, 0]) - margin
        self.y_min = np.min(anchors[:, 1]) + margin
        self.y_max = np.max(anchors[:, 1]) - margin
        
        # Z (altura) tiene un límite de piso seguro (2m) y el techo son los motores
        self.z_min = 2.0 
        self.z_max = np.max(anchors[:, 2]) - margin

    def generate(self, ball_position_field) -> tuple[float, float, float]:
        """Devuelve la posición de referencia (X, Y, Z) segura para la SpiderCam."""
        # Para esta versión, la cámara se posiciona exactamente sobre el X,Y del balón
        # a una altura Z fija definida en la configuración.
        x, y = ball_position_field[0], ball_position_field[1]
        target_pos = [x, y, self.z_fixed]
        
        return self._clip_to_workspace(target_pos)

    def _clip_to_workspace(self, position):
        """Satura la posición al volumen de trabajo físico del rig."""
        safe_x = np.clip(position[0], self.x_min, self.x_max)
        safe_y = np.clip(position[1], self.y_min, self.y_max)
        safe_z = np.clip(position[2], self.z_min, self.z_max)
        
        # Devolvemos una tupla de flotantes nativos
        return (float(safe_x), float(safe_y), float(safe_z))
