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

