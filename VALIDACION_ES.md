# Evidencia de validación automatizada

Se ejecutaron diez escenarios diferentes con datos ficticios o sintéticos. Este informe describe ejecuciones reales del código mediante un script automatizado. No representa tráfico de usuarios, experiencia laboral ni contribuciones realizadas manualmente por Erik.

Resultado: **10 de 10 escenarios aprobados**.

Consulta `validation-results.json` para ver cada entrada, resultado y fecha UTC de ejecución.

## Repetir las ejecuciones

Desde la carpeta del repositorio ejecuta:

```bash
python validate_scenarios.py
```

En Mercado Aprende instala primero las dependencias del README. En los otros cinco proyectos basta Python. El script utiliza almacenamiento temporal: no cambia registros personales ni realiza compras reales. Regenera el informe local; para conservar nuevos resultados en GitHub debes revisarlos y hacer un commit.

## Qué se comprobó

| Escenario | Entrada | Resultado |
|---|---|---|
| 1 | {"mode": "original", "width": 16, "height": 16, "synthetic_pattern": 1} | Aprobado |
| 2 | {"mode": "blur", "width": 16, "height": 16, "synthetic_pattern": 2} | Aprobado |
| 3 | {"mode": "edges", "width": 16, "height": 16, "synthetic_pattern": 3} | Aprobado |
| 4 | {"mode": "original", "width": 16, "height": 16, "synthetic_pattern": 4} | Aprobado |
| 5 | {"mode": "blur", "width": 16, "height": 16, "synthetic_pattern": 5} | Aprobado |
| 6 | {"mode": "edges", "width": 16, "height": 16, "synthetic_pattern": 6} | Aprobado |
| 7 | {"mode": "original", "width": 16, "height": 16, "synthetic_pattern": 7} | Aprobado |
| 8 | {"mode": "blur", "width": 16, "height": 16, "synthetic_pattern": 8} | Aprobado |
| 9 | {"mode": "edges", "width": 16, "height": 16, "synthetic_pattern": 9} | Aprobado |
| 10 | {"mode": "original", "width": 16, "height": 16, "synthetic_pattern": 10} | Aprobado |
