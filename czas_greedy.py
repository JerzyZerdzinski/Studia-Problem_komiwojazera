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

for i in range(5, 1000,20):
    graph = generate_graph(i)
    start = time.time()
    greedy_tsp(graph, 0)
    end = time.time()
    wynik = end - start
    print(wynik)

for i in range(5, 1000,20):
    print(i)
