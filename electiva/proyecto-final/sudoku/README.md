# 🧬 Resolución de Sudoku con Algoritmos Genéticos Híbridos (GA + Búsqueda Local)

## Descripción del Proyecto

Este proyecto implementa un **Algoritmo Genético (GA)** para resolver un Sudoku clásico de 9x9, incorporando una **estrategia híbrida de búsqueda local** (*Hybrid Genetic Algorithm*).

El objetivo es demostrar cómo los principios de la **computación evolutiva** pueden aplicarse a problemas de optimización combinatoria, mejorando significativamente la convergencia mediante técnicas avanzadas.

---

## Objetivos

- Representar un Sudoku como un **individuo genético**
- Definir una función de **fitness basada en conflictos**
- Aplicar operadores genéticos:
  - Selección
  - Cruce
  - Mutación
  - Elitismo
- Implementar **búsqueda local posterior a la mutación**
- Visualizar el **antes y después** del Sudoku en consola
- Alcanzar una **solución válida (fitness = 0)**

---

## Conceptos Aplicados

| Concepto | Aplicación en el Proyecto |
|--------|---------------------------|
| Individuo | Un tablero completo de Sudoku |
| Gen | Una celda del tablero |
| Población | Conjunto de sudokus |
| Fitness | Cantidad de conflictos en filas, columnas y subcuadros |
| Selección | Torneo |
| Cruce | Intercambio de filas |
| Mutación | Swaps dentro de una fila |
| Elitismo | Conservación de los mejores individuos |
| 🔥 Búsqueda Local | Optimización posterior a la mutación |

---

## Algoritmo Utilizado

### 🧬 Algoritmo Genético Híbrido

1. Inicialización de población válida por filas
2. Evaluación del fitness
3. Selección por torneo
4. Cruce entre padres
5. Mutación controlada
6. 🔥 **Búsqueda local (hill climbing por swaps)**
7. Elitismo
8. Repetir hasta encontrar solución o alcanzar el límite

---

## Búsqueda Local (Hybrid GA)

Después de la mutación, se aplica una búsqueda local:

- Se prueban pequeños **intercambios (swaps)** entre celdas no fijas
- Se conserva el cambio **solo si mejora el fitness**
- Permite escapar de mínimos locales
- Acelera la convergencia drásticamente

> Esta técnica convierte el GA clásico en un **algoritmo evolutivo avanzado**.

---

## Visualización en Consola

El programa muestra:

- Sudoku inicial (con ceros)
- Evolución del fitness por generaciones
- Sudoku final resuelto
- Fitness final

Ejemplo:
Gen 0 | Mejor fitness: 36
Solución encontrada en generación 12
Fitness final: 0


---

## Requisitos

- Python 3.8+
- Librerías estándar:
  - `random`
  - `copy`
  - `pandas` *(opcional, solo para visualización alternativa)*

No se requiere dataset externo.

---

## Ejecución

```bash
python sudoku_ga.py
```

## Estructura del Código

```bash
crear_individuo() → Genera sudokus válidos por fila

fitness() → Cuenta conflictos

seleccion() → Torneo

cruzar() → Cruce por filas

mutar() → Swap controlado

busqueda_local() → Optimización local

algoritmo_genetico() → Control principal

mostrar_tabla_ascii() → Visualización en consola
```