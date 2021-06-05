
import random
from copy import copy
from math import sqrt

def neighbourhood(sol):
    c1 = random.randint(0, len(sol) - 1)
    c2 = random.randint(0, len(sol) - 2)

    if c2 >= c1:
        c2 += 1
    
    new_sol = copy(sol)

    temp = sol[c1]
    new_sol[c1] = new_sol[c2]
    new_sol[c2] = temp

    return new_sol

def distance(pos1, pos2):
    # Straight line distance between two points
    return sqrt(pow(pos2[0] - pos1[0], 2) + pow(pos2[1] - pos1[1], 2))

def evaluate(f1_pos, f2_pos, client_pos, sol):
    total = distance(f1_pos, client_pos[sol[0]])

    for i in range(len(sol) - 1):
        total += distance(client_pos[sol[i]], client_pos[sol[i + 1]])
    
    total += distance(client_pos[sol[-1]], f2_pos)

    return total

def hill_climbing(f1_pos, f2_pos, client_pos):
    # Initial solution is random
    current = list(range(len(client_pos)))
    random.shuffle(current)

    iterations_without_improvement = 0

    # Best accept with a neighbourhood of size 50
    while iterations_without_improvement < 100:
        best = current

        for _ in range(50):
            neighbour = neighbourhood(current)
            # The acceptance test is evaluate(neighbour) < evaluate(best) since we want to minimize the distance travelled
            if evaluate(f1_pos, f2_pos, client_pos, neighbour) < evaluate(f1_pos, f2_pos, client_pos, best):
                best = neighbour
        
        if current == best:
            iterations_without_improvement += 1
        else:
            current = best
    
    return current


# Problem 1
f1_pos = [1, 1]
f2_pos = [10, 10]
client_pos = [[8, 8], [4, 4], [3, 3], [7, 7], [2, 2], [9, 9]]

sol = hill_climbing(f1_pos, f2_pos, client_pos)
print(sol, evaluate(f1_pos, f2_pos, client_pos, sol))

# Problem 2
f1_pos = [1, 1]
f2_pos = [10, 10]
client_pos = [[2, 2], [2, 8], [6, 6], [1, 6], [10, 5], [5, 8]]

sol = hill_climbing(f1_pos, f2_pos, client_pos)
print(sol, evaluate(f1_pos, f2_pos, client_pos, sol))

# Problem 3
f1_pos = [1, 1]
f2_pos = [5, 2]
client_pos = [[2, 8], [1, 4], [6, 6], [6, 1], [1, 6], [5, 8]]

sol = hill_climbing(f1_pos, f2_pos, client_pos)
print(sol, evaluate(f1_pos, f2_pos, client_pos, sol))
