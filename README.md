# programa-python

# Fase 5 – Evaluación Final POA: Reabastecimiento de Inventario

Solución desarrollada en **Python** para el curso **Fundamentos de Programación (213022)** de la **Universidad Nacional Abierta y a Distancia (UNAD)**, correspondiente al **Problema 3** del *Anexo 4 – Banco de Problemas*.

## Descripción del problema

Se cuenta con una matriz que almacena información de inventario con el siguiente formato por fila:

`[Código del artículo, Nombre del artículo, Stock actual, Stock mínimo requerido]`

El programa evalúa cada artículo y determina cuántas unidades deben pedirse para reabastecerlo:
- Si el **stock actual** es menor que el **stock mínimo requerido**, la cantidad a pedir es `Stock mínimo requerido - Stock actual`.
- Si el **stock actual** es mayor o igual al **stock mínimo requerido**, la cantidad a pedir es `0`.

Al finalizar, muestra en consola el nombre de cada artículo junto con la cantidad exacta a solicitar.

## Estructura del proyecto

- `reabastecimiento.py` (o el nombre que le des a tu archivo `.py`): contiene las funciones modulares para calcular la cantidad a pedir, generar el reporte y ejecutar el programa principal.
- `README.md`: documentación general de la solución.

## Estructuras y conceptos aplicados

- **Matriz / listas anidadas:** almacenamiento de los artículos y sus atributos.
- **Ciclo `for`:** recorrido de cada fila de la matriz de inventario.
- **Condicionales (`if` / `return`):** comparación entre el stock actual y el stock mínimo requerido.
- **Funciones:** separación de responsabilidades (`calcular_cantidad_a_pedir`, `mostrar_reporte_reabastecimiento` y `main`).

## Ejecución

Asegúrate de tener **Python 3** instalado y ejecuta desde consola o terminal:

```bash
python reabastecimiento.py
