# Notebooks de experimentación

Espacio para iteración rápida ANTES de llevar algo a `src/spidercam/`.
Casos de uso típicos: ajustar matrices Q/R del filtro de Kalman, graficar
trayectoria filtrada vs. cruda, probar umbrales de confianza de YOLO,
explorar ganancias de PID con datos sintéticos.

Regla: una vez que algo "funciona" en un notebook, se migra a un módulo
real en `src/spidercam/` con su test correspondiente en `tests/`. Los
notebooks no son código de producción ni se importan desde `src/`.
