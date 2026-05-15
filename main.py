from genetic_algo import Chromosome, selection, crossover, mutate

def run_evolution(pop_size=100, mutation_rate=0.1):
    # Step 1: Iniitialize population
    population = [ Chromosome() for _ in range(pop_size)]
    generation = 0

    while True:
        # Sort population by fitness (descending)
        population.sort(key=lambda x: x.fitness, reverse=True)
        best_individual = population[0]

        # Logging progress
        print(f"Generation: {generation}, Best Fitness: {best_individual.fitness}, Genes: {best_individual.genes}")

        # Terminaiton: if we found a perfect solution (fitness = 28)
        if best_individual.fitness == 28:
            print("Solution found!")
            return best_individual
        
        # Create new generation
        new_population = []
        
        # Keep the absolute best individual for the next generation (elitism)
        new_population.append(best_individual)

        # Fill the rest of the new population through reproduction
        while len(new_population) < pop_size:
            # Selection & Crossover
            parent1, parent2 = selection(population)
            child1, child2 = crossover(parent1, parent2)

            # Mutation
            new_population.append(mutate(child1, mutation_rate))
            if len(new_population) < pop_size:
                new_population.append(mutate(child2, mutation_rate))
        
        population = new_population
        generation += 1

if __name__ == "__main__":
    solution = run_evolution()
    print(f"Final Configuration: {solution.genes}")
        

