#############################################
#                                           #
#   HackerRank Week of Code 30 Challenges   #
#                                           #
#                   Poles                   # 
#                                           # 
#############################################

import random, time

def initial_population(altitude, number):
    nodes = []
    if number == 1:
        nodes.append([altitude[0]])
        nodes.append([altitude[0]])
        nodes.append([altitude[0]])
        nodes.append([altitude[0]])
        return nodes
    for i in range(4):
        population = altitude[1:]
        dna_string = []
        for j in range(number - 1):
            node = population.pop(population.index(random.choice(population)))
            dna_string.append(node)
        dna_string += altitude[:1]
        nodes.append(sorted(dna_string, reverse = True))
    return nodes

def check_fitness(altitude, generation, costs):
    fitness = {}
    for _ in range(len(generation)):
        cost = 0
        start = len(altitude) - 1
        for i in generation[_]:
            for j in range(start, -1, -1):
                if i == altitude[j]: 
                    start = altitude.index(i) - 1
                    break
                else:
                    cost += costs[altitude[j]][j - altitude.index(i)]
        fitness[_] = cost  
    return fitness

def mutate(dna_, probability, altitude):
    dna = dna_
    for chain in range(len(dna)):
        dice = random.randint(1, 100) <= probability
        if dice:
            upper_random = (len(dna[chain]) - 1, len(dna[chain]) - 2)[len(dna[chain]) > 1]
            mutated_node = random.randint(0, upper_random)
            node_position = altitude.index(dna[chain][mutated_node])
            dice = random.randint(1,2) == 1
            limit = (0, len(altitude) - 1)[dice]
            step = (-1, 1)[dice]
            for j in range(node_position + step, limit, step):
                if altitude[j] not in dna[chain]:
                    dna[chain][mutated_node] = altitude[j]
                    break
    return dna

def cross_section(pair, divider):
    sectioned = [[],[],[],[]]
    sectioned[0] = sorted(pair[0][:divider[0]] + pair[1][divider[0]:], reverse = True)
    sectioned[1] = sorted(pair[1][:divider[0]] + pair[0][divider[0]:], reverse = True)
    sectioned[2] = sorted(pair[2][:divider[1]] + pair[3][divider[1]:], reverse = True)
    sectioned[3] = sorted(pair[3][:divider[1]] + pair[2][divider[1]:], reverse = True)
    return sectioned

def populate_next_generation(altitude, costs, generation, fitness, max_cost):
    fitness_levels = sorted(fitness, key = fitness.get)
    mating_pairs = []
    mating_pairs.append(generation[fitness_levels[0]])
    mating_pairs.append(generation[fitness_levels[2]])
    mating_pairs.append(generation[fitness_levels[1]])
    mating_pairs.append(generation[fitness_levels[2]])
    if len(mating_pairs[0][:-1]) == 0:
        mutation_threshold = -1
    elif len(mating_pairs[0][:-1]) > 1:
        mutation_threshold = 5
    else:
        mutation_threshold = 100
    divider = [random.randint(0, len(mating_pairs[0])), random.randint(0, len(mating_pairs[0]))]
    mating_pairs = cross_section(mating_pairs, divider)
    mating_pairs = mutate(mating_pairs, mutation_threshold, altitude)
    return mating_pairs

start_time = time.time()

#n,k = input().strip().split(' ')
#n,k = [int(n),int(k)]
#altitude, weight = [], []
#for a0 in range(n):
#    x_i,w_i = input().strip().split(' ')
#    x_i,w_i = int(x_i),int(w_i)
#    altitude.append(x_i)
#    weight.append(w_i)

#n, k = 6, 2
#altitude = [10,12,16,18,30,32]
#weight = [15,17,18,13,10,1]

#n, k = 3, 1
#altitude = [20,30,40]
#weight = [1,1,1]

n, k = 4, 2
altitude = [5, 10, 15, 50]
weight = [1, 1, 1, 1]


generation = initial_population(altitude, k)

costs = {}
for i in range(len(altitude) - 1, -1, -1):
    move_cost = []
    for j in range(i, -1, -1):
        move_cost.append(weight[i] * abs(altitude[i] - altitude[j]))
    costs[altitude[i]] = move_cost

max_cost = sum([sum(costs[_]) for _ in costs]) + 1
generation_fitness = check_fitness(altitude, generation, costs)

while 0 not in generation_fitness.values():
    print(generation)
    generation = populate_next_generation(altitude, costs, generation, generation_fitness, max_cost)
    if min(generation_fitness.values()) < max_cost: 
        max_cost = min(generation_fitness.values())
        grail = generation
    generation_fitness = check_fitness(altitude, generation, costs)
    elapsed_time = time.time()
    if elapsed_time - start_time > 9.85:
        print(max_cost)
        break    