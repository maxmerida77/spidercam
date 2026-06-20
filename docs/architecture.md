# Arquitectura del sistema

```
Video de fútbol
        ↓
Detección de balón        (src/spidercam/detection)
        ↓
Tracking                  (src/spidercam/tracking)
        ↓
Filtro de Kalman          (src/spidercam/tracking)
        ↓
Estimación de trayectoria (src/spidercam/tracking)
        ↓
Generador de referencias  (src/spidercam/control)
        ↓
Control PID               (src/spidercam/control)
        ↓
SpiderCam virtual         (src/spidercam/simulation)
        ↓
Visualización 3D          (src/spidercam/visualization)
```

## Decisiones técnicas clave

### Mapeo 2D → 3D (homografía)
Se asume el balón sobre el plano de la cancha. Se calcula una homografía
una sola vez por video (cámara fija de cancha completa) usando
`cv2.findHomography`, calibrada con puntos conocidos de la cancha
(esquinas de área, círculo central). La altura Z de la SpiderCam se trata
como simplificación (fija o función simple), no se estima profundidad real.

### Cinemática de la SpiderCam
El control opera completamente en espacio cartesiano (X, Y, Z) del carro/
cámara. La cinemática inversa (distancia euclidiana de cada anclaje al
carro) se usa únicamente para renderizar los 4 cables en la visualización
3D, no como parte del lazo de control. No se modela cinemática directa,
tensión de cables ni catenaria (cables rectos, sin pandeo).

### Regla dura: `simulation/` vs `visualization/`
- `simulation/` contiene únicamente matemáticas: estado del carro, cálculo
  de longitudes de cable, integración de la posición en el tiempo. Solo
  puede depender de NumPy/SciPy. **Nunca** debe importar PyQtGraph, PyQt5
  ni ningún otro toolkit gráfico.
- `visualization/` es el único lugar del proyecto donde vive PyQtGraph.
  Recibe estado ya calculado (posiciones, longitudes de cable) y lo
  dibuja; no calcula nada por su cuenta.
- Si algún día `simulation/` "necesita saber" algo sobre cómo se ve algo
  en pantalla, es señal de que esa lógica está en el módulo equivocado.

### Visualización 3D: PyQtGraph
Se eligió PyQtGraph (`GLViewWidget` para 3D + `PlotWidget` para series de
tiempo) sobre VPython porque el proyecto necesita mostrar, en la misma
aplicación, tanto la escena 3D de la SpiderCam como gráficas de métricas
de seguimiento (sección 6 del alcance). PyQtGraph cubre ambos casos con
un solo toolkit; VPython habría requerido una librería adicional para las
gráficas 2D.
