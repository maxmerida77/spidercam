# SpiderCam Autónoma Guiada por Visión Artificial

Sistema que detecta y sigue un balón de fútbol en video real mediante visión
artificial, y usa esa información para controlar una SpiderCam virtual dentro
de una simulación 3D, manteniendo la jugada dentro del encuadre.

## Arquitectura

```
Video de fútbol → Detección de balón → Tracking → Filtro de Kalman →
Estimación de trayectoria → Generador de referencias → Control PID →
SpiderCam virtual → Visualización 3D
```

Ver `docs/architecture.md` para el detalle completo.

## Estructura del proyecto

```
spidercam_vision/
├── config/                  Parámetros del sistema (config.yaml)
├── data/
│   ├── raw/                 Videos de entrada (no versionado)
│   └── processed/           Resultados, métricas, trayectorias exportadas
├── docs/                    Documentación técnica del proyecto
├── notebooks/                Experimentación rápida (Kalman, calibración, etc.)
├── scripts/                 Puntos de entrada ejecutables (CLI)
├── src/spidercam/           Código fuente (paquete principal)
│   ├── detection/           Detección del balón (YOLOv8)
│   ├── tracking/            Filtro de Kalman
│   ├── geometry/            Homografía y cinemática de cables
│   ├── control/             Generador de referencias y PID
│   ├── simulation/          Modelo del estadio y de la SpiderCam (solo matemáticas)
│   ├── visualization/       Visualización 3D y métricas (PyQtGraph)
│   └── metrics/             Métricas de desempeño
└── tests/                   Pruebas unitarias (reproducibilidad, RNF-04)
```

## Instalación

```bash
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

No se usa Conda por ahora: todas las dependencias (OpenCV, Ultralytics,
SciPy, PyQt5) distribuyen wheels binarios estables para Windows vía pip.
Si en algún punto aparece un problema real de instalación que pip no
resuelva, se evalúa migrar a `environment.yml`.

## Decisión de visualización: PyQtGraph

Se eligió PyQtGraph sobre VPython porque el proyecto necesita 3D (la
SpiderCam y sus cables) y gráficas 2D de métricas en la misma aplicación;
PyQtGraph cubre ambos con un solo toolkit. Detalle en `docs/architecture.md`.

## Regla de diseño: `simulation/` vs `visualization/`

`simulation/` solo contiene matemáticas (NumPy/SciPy), nunca imports de
PyQtGraph/PyQt. `visualization/` es el único lugar que dibuja en pantalla.
Ver `docs/architecture.md` para el detalle completo.

## Uso (placeholder, se completa en Fase 8)

```bash
python scripts/calibrate_homography.py --video data/raw/clip.mp4
python scripts/run_pipeline.py --config config/config.yaml
```

## Fases de desarrollo

1. Simulación SpiderCam
2. Modelo geométrico y cinemático
3. Planeación de trayectorias
4. Detección de balón (visión artificial)
5. Tracking y filtro de Kalman
6. Generación de referencias
7. Control PID
8. Integración completa
9. Visualización y presentación final
