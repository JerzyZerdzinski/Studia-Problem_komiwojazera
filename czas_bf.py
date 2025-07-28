import random
import time
 
# Generuje graf nieskierowany o n wierzchołkach z losowymi wagami z przedziału
def generate_graph(n, weight_range=(1, 100)): 
    graph = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(float('inf'))
        graph.append(row)
 
    for i in range(n):
        for j in range(i + 1, n):
            weight = random.randint(*weight_range)
            graph[i][j] = weight
            graph[j][i] = weight 
 
    return graph
 
#Usuwa D dróg z grafu o V wierzchołkach podanego za pomocą macierzy przejść
def deleting_roads(graph, D, V):
    for i in range(D):
        x = random.randint(0, V-1)
        while (graph[x].count(float('inf'))>=V-2):
            x = random.randint(0, V-1)
        y=x
        while (x==y or graph[y].count(float('inf'))>=V-2):
            y = random.randint(0, V-1)
        graph[x][y] = float('inf')
        graph[y][x] = float('inf')
    return graph
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

for i in range(5, 14):
    graph = generate_graph(i)
    start = time.time()
    tsp(graph, 0, i)
    end = time.time()
    wynik = end - start
    print(wynik)
