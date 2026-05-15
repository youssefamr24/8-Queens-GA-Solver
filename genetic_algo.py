import random

class Chromosome:
    def __init__(self, genes=None):
        # Initial population
        self.genes = genes if genes else [ random.randint(1, 8) for _ in range(8) ]
        self.fitness = self.calculate_fitness()

    # Fitness evaluation is for counting the number of non-attacking pairs of queens
    def calculate_fitness(self):

        clashes = 0
        n = len(self.genes)
        for i in range(n):
            for j in range(i + 1, n):
                # 1. check same row
                if self.genes[i] == self.genes[j]:
                    clashes += 1
                # 2. check diagonal
                if abs(self.genes[i] - self.genes[j]) == abs(i - j):
                    clashes += 1 
        
        return 28 - clashes
    

# Selection is for choosing the fittest solutions to be parents
def selection(population):
        
    # using weighted random choice (Roulette Wheel Selection)
    total_fitness = sum(c.fitness for c in population)
    probabilities = [ c.fitness / total_fitness for c in population]
    return random.choices(population, weights=probabilities, k=2)
    
    
# Crossover is for combining two parents to create offspring(children)
def crossover(parent1, parent2):
    # Pick a random split point
    cp = random.randint(1, 6)
    child1_genes = parent1.genes[:cp] + parent2.genes[cp:]
    child2_genes = parent2.genes[:cp] + parent1.genes[cp:]
    return Chromosome(child1_genes), Chromosome(child2_genes)
    

# Mutation is for introducing random changes to maintain genetic diversity
def mutate(chromosome, mutation_rate=0.1):
    if random.random() < mutation_rate:
        # Randomly change one gene (queen's position)
        index = random.randint(0, 7)
        # Change the row of a random queen to a new random position
        chromosome.genes[index] = random.randint(1, 8)
        # Recalculate fitness after mutation
        chromosome.fitness = chromosome.calculate_fitness()
    return chromosome

