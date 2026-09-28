# Bloque 5: métricas

Hoja de cálculo: https://docs.google.com/spreadsheets/d/1mtCjLLvpqAHB74ZJJYPq-fgoHT1PTwplwgfisGmjzYA/edit?usp=sharing

## Métricas DORA (datos en `datos/despliegues.csv`, periodo de 28 días)
- Frecuencia de despliegue: 20 despliegues / 28 días = 0,71 por día (≈ 5 por semana)
- Lead time de cambios (mediana, en horas): 20 h (promedio 24,7 h)
- Tasa de fallo de cambios: 4 / 20 = 20 %
- Tiempo medio de recuperación (horas): (5 + 3 + 2 + 8) / 4 = 4,5 h

Observación: 3 de los 4 despliegues fallidos ocurrieron un viernes y el otro un sábado,
lo que respalda la política de no desplegar al final de la semana.

## Cuatro métricas por enfoque
| Enfoque | Métrica | Qué atributo ISO 25010 respalda |
|---|---|---|
| Scrum | Defectos escapados por sprint | Fiabilidad (ausencia de fallos) |
| Kanban | Tiempo de ciclo (de "En desarrollo" a "Hecho") | Mantenibilidad (modificabilidad) |
| XP | Cobertura de pruebas unitarias (hoy 100 %) | Mantenibilidad (capacidad de ser probado) |
| DevOps | Tasa de fallo de cambios (hoy 20 %) | Fiabilidad (capacidad de recuperación) |