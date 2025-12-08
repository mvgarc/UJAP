import random

TARGET = "INGENIERIA UJAP"
GENES = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def create_genome():
    return "".join(random.choice(GENES) for _ in range(len(TARGET)))

def fitness(genome):
    return sum(1 for a, b in zip(genome, TARGET) if a == b)

def crossover(p1, p2):
    point = random.randint(1, len(TARGET)-1)
    return p1[:point] + p2[point:]

def mutate(genome):
    i = random.randint(0, len(genome)-1)
    new_char = random.choice(GENES)
    return genome[:i] + new_char + genome[i+1:]

population = [create_genome() for _ in range(100)]

generation = 0
while True:
    population = sorted(population, key=fitness, reverse=True)
    if population[0] == TARGET:
        print("Generación:", generation)
        print("Resultado:", population[0])
        break

    new_population = population[:20]  # elite
    while len(new_population) < 100:
        p1, p2 = random.sample(population[:50], 2)
        child = crossover(p1, p2)
        if random.random() < 0.1:
            child = mutate(child)
        new_population.append(child)

    population = new_population
    generation += 1
