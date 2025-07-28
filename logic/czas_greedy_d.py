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

def greedy_tsp(graph, s):
    n = len(graph)  
    visited = [False] * n  
    solution = []  
    total_cost = 0  
    current_city = s
    visited[current_city] = True
    for _ in range(n - 1):  
        next_city = None
        min_cost = float('inf')
        for city in range(n):
            if not visited[city] and graph[current_city][city] < min_cost:
                min_cost = graph[current_city][city]
                next_city = city
        if next_city is not None:
            solution.append(next_city)
            visited[next_city] = True
            total_cost += min_cost
            current_city = next_city
    total_cost += graph[current_city][s]
    return total_cost, solution

def greedy_tsp_d(graph, vector, V):
    solution = []
    prev = 0
    i = vector[0]
    cost = 0
    for _ in range(V-1):
        if graph[prev][i] != float('inf') and i not in solution and i != 0:
            solution.append(i)
            cost += graph[prev][i]
            prev = i
 
        else:
            prev = i
            min_value = float('inf')
            for j in range(V):
                if min_value>graph[prev][j] and j not in solution and j != 0:
                    min_value = graph[prev][j]
                    i=j
 
            solution.append(i)
            cost += graph[prev][i]
 
        if vector.index(i)<V-2:
            i = vector[vector.index(i)+1]
    cost += graph[vector[V-2]][0]
    return solution, cost


for i in range(5, 14):
    graph = generate_graph(i)
    cost, vector = greedy_tsp(graph, 0)
    graph= deleting_roads(graph, i//5, i)
    start = time.time()
    greedy_tsp_d(graph, vector, i)
    end = time.time()
    wynik = end - start
    print(wynik)


for i in range(5, 1000,20):
    print(i)