from itertools import permutations
from sys import maxsize

def tsp(graph, s, V):

    vertex = [i for i in range(V) if i != s]
    min_cost = maxsize
    next_permutation = permutations(vertex)

    for i in next_permutation:
        current_cost = 0  
        k = s  

        for j in i:
            current_cost += graph[k][j]
            k = j
        current_cost += graph[k][s]
        if current_cost < min_cost:
            min_cost = current_cost
            wynik = i
    # return wynik
    return min_cost, wynik