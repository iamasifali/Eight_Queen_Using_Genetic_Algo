import random

 

def random_chromosome(size): #making random chromosomes

    return [ random.randint(0, nq-1) for _ in range(nq) ]

 
def fitness(chromosome):

    horizontal_collisions = sum([chromosome.count(queen)-1 for queen in chromosome])/2

    diagonal_collisions = 0

    n = len(chromosome)

    coordinate = [(i,chromosome[i]) for i in range(n)]

    for i in range(n):

        for item in coordinate[(i+1):]:

            if abs(coordinate[i][0]-item[0])==abs(coordinate[i][1]-item[1]):

                diagonal_collisions+=1

    return int(maxFitness - (horizontal_collisions + diagonal_collisions))

 
def probability(chromosome, fitness):

    return fitness(chromosome) / maxFitness

 
def random_pick(population, probabilities):

    populationWithProbabilty = zip(population, probabilities)

    total = sum(w for c, w in populationWithProbabilty)

    r = random.uniform(0, total)

    upto = 0

    for c, w in zip(population, probabilities):

        if upto + w >= r:

            return c

        upto += w

    assert False, "Shouldn't get here"

       
def reproduce(x, y): #doing cross_over between two chromosomes

    n = len(x)

    c = random.randint(0, n - 1)

    return x[0:c] + y[c:n]

 
def mutate(x):  #randomly changing the value of a random index of a chromosome

    n = len(x)

    c = random.randint(0, n - 1)

    m = random.randint(1, n-1)

    x[c] = m

    return x

 
def genetic_queen(population, fitness):

    mutation_probability = 0.03

    new_population = []

    #print(population)

    probabilities = [probability(n, fitness) for n in population]

    for i in range(len(population)):

        x = random_pick(population, probabilities) #best parent 1

        y = random_pick(population, probabilities) #best parent 2

        child = reproduce(x, y) #creating two new chromosomes from the best 2 parents

        if random.random() < mutation_probability:

            child = mutate(child)

        #print_chromosome(child)

        new_population.append(child)

        if fitness(child) == maxFitness: break

    return new_population

 
def print_chromosome(chrom):

    print("{}" .format(str(chrom)))

 
if __name__ == "__main__":

    nq = 8 #say N = 8

    maxFitness = (nq*(nq-1))/2  # 8*7/2 = 28

    population = [random_chromosome(nq) for _ in range(500)]

    #print(population)

    generation = 1

    i=1

    while not maxFitness in [fitness(chrom) for chrom in population]:

        #print(population)

        population = genetic_queen(population, fitness)

        generation += 1

        i+=1

    chrom_out = []

    for chrom in population:

        if fitness(chrom) == maxFitness:

            #print("");

            #print("One of the solutions: ")

            chrom_out = chrom

            print_chromosome(chrom)

            break

           
