import random
import pandas as pd
import copy

# Sudoku base (0 = vacío)
SUDOKU_BASE = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def obtener_fijas(sudoku):
    fijas = []
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                fijas.append((i, j))
    return fijas

FIJAS = obtener_fijas(SUDOKU_BASE)

def crear_individuo():
    individuo = copy.deepcopy(SUDOKU_BASE)
    for i in range(9):
        numeros = set(range(1, 10))
        for j in range(9):
            if individuo[i][j] != 0:
                numeros.discard(individuo[i][j])
        numeros = list(numeros)
        random.shuffle(numeros)

        for j in range(9):
            if individuo[i][j] == 0:
                individuo[i][j] = numeros.pop()
    return individuo


def fitness(individuo):
    errores = 0

    # Filas
    for fila in individuo:
        errores += 9 - len(set(fila))

    # Columnas
    for col in range(9):
        columna = [individuo[fila][col] for fila in range(9)]
        errores += 9 - len(set(columna))

    # Subcuadros
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            bloque = []
            for x in range(3):
                for y in range(3):
                    bloque.append(individuo[i+x][j+y])
            errores += 9 - len(set(bloque))

    return errores

def seleccion(poblacion):
    torneo = random.sample(poblacion, 3)
    torneo.sort(key=lambda x: fitness(x))
    return torneo[0]

def cruzar(padre1, padre2):
    hijo = copy.deepcopy(padre1)
    fila = random.randint(0, 8)
    hijo[fila] = padre2[fila][:]
    return hijo

def mutar(individuo, prob=0.2):
    if random.random() < prob:
        fila = random.randint(0, 8)

        if len(set(individuo[fila])) < 9:
            libres = [j for j in range(9) if (fila, j) not in FIJAS]
            if len(libres) >= 2:
                a, b = random.sample(libres, 2)
                individuo[fila][a], individuo[fila][b] = individuo[fila][b], individuo[fila][a]


def algoritmo_genetico():
    poblacion = [crear_individuo() for _ in range(200)]

    mejor_fitness_historico = float("inf")

    for generacion in range(1000):
        poblacion.sort(key=lambda x: fitness(x))
        mejor = poblacion[0]
        fit = fitness(mejor)

        if fit < mejor_fitness_historico:
            mejor_fitness_historico = fit

        if fit == 0:
            print(f"\n Solución encontrada en generación {generacion}")
            return mejor

        nueva_poblacion = poblacion[:10]  # elitismo

        while len(nueva_poblacion) < 200:
            p1 = seleccion(poblacion)
            p2 = seleccion(poblacion)
            hijo = cruzar(p1, p2)
            mutar(hijo)
            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion

        if generacion % 50 == 0:
            print(f"Gen {generacion} | Mejor fitness: {fit}")

    print("\n No se encontró solución perfecta")
    return poblacion[0]


def mostrar_tabla_ascii(sudoku, titulo):
    print("\n" + "="*45)
    print(titulo.center(45))
    print("="*45)

    print("     " + " ".join([f"C{i+1}" for i in range(9)]))
    print("   +" + "---+" * 9)

    for i, fila in enumerate(sudoku):
        fila_str = " | ".join(str(x) for x in fila)
        print(f"F{i+1} | {fila_str} |")
        if (i+1) % 3 == 0:
            print("   +" + "---+" * 9)

solucion = algoritmo_genetico()

mostrar_tabla_ascii(SUDOKU_BASE, "SUDOKU INICIAL")
mostrar_tabla_ascii(solucion, "SUDOKU FINAL")


print("\n Fitness final:", fitness(solucion))
