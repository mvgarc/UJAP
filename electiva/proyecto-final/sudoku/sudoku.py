import random
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
        for j in range(9):
            if (i, j) not in FIJAS:
                individuo[i][j] = random.randint(1, 9)
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

def mutar(individuo, prob=0.1):
    for _ in range(2):
        if random.random() < prob:
            i, j = random.randint(0, 8), random.randint(0, 8)
            if (i, j) not in FIJAS:
                individuo[i][j] = random.randint(1, 9)

def algoritmo_genetico():
    poblacion = [crear_individuo() for _ in range(200)]

    for generacion in range(1000):
        poblacion.sort(key=lambda x: fitness(x))

        if fitness(poblacion[0]) == 0:
            print(f"Solución encontrada en generación {generacion}")
            return poblacion[0]

        nueva_poblacion = poblacion[:10]  # elitismo

        while len(nueva_poblacion) < 200:
            p1 = seleccion(poblacion)
            p2 = seleccion(poblacion)
            hijo = cruzar(p1, p2)
            mutar(hijo)
            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion

        if generacion % 50 == 0:
            print(f"Gen {generacion} | Mejor fitness: {fitness(poblacion[0])}")

    return poblacion[0]

def mostrar(sudoku):
    for fila in sudoku:
        print(fila)

