import random

from sys import maxsize
from itertools import permutations  

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
from sys import maxsize
from itertools import permutations  

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

def deleting_roads(graph_p, D, V):
    for i in range(D):
        x = random.randint(0, V-1)
        while (graph_p[x].count(float('inf'))>=V-2):
            x = random.randint(0, V-1)
        y=x
        while (x==y or graph_p[y].count(float('inf'))>=V-2):
            y = random.randint(0, V-1)
        graph_p[x][y] = float('inf')
        graph_p[y][x] = float('inf')
    return graph_p

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

import random
import numpy as np

def ant_colonyTSP(graph, num_ants, num_iterations, alpha, beta, rho, q):
    """
    graph: Macierz sąsiedztwa (kosztów przejścia między miastami)
    num_ants: Liczba mrówek
    num_iterations: Liczba iteracji algorytmu
    alpha: Współczynnik znaczenia feromonów
    beta: Współczynnik znaczenia heurystyki
    rho: Współczynnik odparowywania feromonów
    q: Ilość feromonów dodawanych przez mrówki
    """
    num_cities = len(graph)
    pheromones = np.ones((num_cities, num_cities))  # Inicjalizacja feromonów
    best_path = None
    best_cost = float('inf')

    for _ in range(num_iterations):
        all_paths = []
        all_costs = []

        for ant in range(num_ants):
            # Budowanie trasy dla jednej mrówki
            visited = [False] * num_cities
            current_city = random.randint(0, num_cities - 1)
            path = [current_city]
            visited[current_city] = True
            total_cost = 0

            for _ in range(num_cities - 1):
                probabilities = []
                for next_city in range(num_cities):
                    if not visited[next_city]:
                        pheromone = pheromones[current_city][next_city] ** alpha
                        if graph[current_city][next_city] != float('inf'):
                            heuristic = (1 / graph[current_city][next_city]) ** beta
                        else:
                            heuristic=0
                        probabilities.append(pheromone * heuristic)
                    else:
                        probabilities.append(0)
                probabilities = np.array(probabilities) / sum(probabilities)
                next_city = np.random.choice(range(num_cities), p=probabilities)
                path.append(next_city)
                visited[next_city] = True
                total_cost += graph[current_city][next_city]
                current_city = next_city

            # Powrót do miasta początkowego
            total_cost += graph[current_city][path[0]]
            path.append(path[0])
            all_paths.append((path, total_cost))
            all_costs.append(total_cost)

            # Aktualizacja najlepszego rozwiązania
            if total_cost < best_cost:
                best_cost = total_cost
                best_path = path

        # Aktualizacja feromonów
        pheromones *= (1 - rho)  # Odparowanie feromonów
        for path, cost in all_paths:
            for i in range(len(path) - 1):
                pheromones[path[i]][path[i+1]] += q / cost
    path = [int(x) for x in best_path]
    return path, best_cost

def ant_colony_deletedTSP(graph, num_ants, num_iterations, alpha, beta, rho, q, vector):
    """
    graph: Macierz sąsiedztwa (kosztów przejścia między miastami)
    num_ants: Liczba mrówek
    num_iterations: Liczba iteracji algorytmu
    alpha: Współczynnik znaczenia feromonów
    beta: Współczynnik znaczenia heurystyki
    rho: Współczynnik odparowywania feromonów
    q: Ilość feromonów dodawanych przez mrówki
    vector: rozwiazanie dla grafu pełnego
    """
    num_cities = len(graph)
    pheromones = np.ones((num_cities, num_cities))  # Inicjalizacja feromonów
    prev = vector[0]
    for i in range(1,len(vector)):
        pheromones[prev][vector[i]] = 3
        prev = vector[i]
    for i in range (num_cities):
        for j in range (num_cities):
            if graph[i][j] == float('inf'):
                pheromones[i][j]=0
    best_path = None
    best_cost = float('inf')

    for _ in range(num_iterations):
        all_paths = []
        all_costs = []

        for ant in range(num_ants):
            # Budowanie trasy dla jednej mrówki
            visited = [False] * num_cities
            current_city = random.randint(0, num_cities - 1)
            path = [current_city]
            visited[current_city] = True
            total_cost = 0 

            for _ in range(num_cities - 1):
                
                probabilities = []
                for next_city in range(num_cities):
                    if not visited[next_city] and pheromones[current_city][next_city] != 0:
                        pheromone = pheromones[current_city][next_city] ** alpha
                        if graph[current_city][next_city] != float('inf'):
                            heuristic = (1 / graph[current_city][next_city]) ** beta
                        else:
                            heuristic=0
                        probabilities.append(pheromone * heuristic)
                    else:
                        probabilities.append(0)
                if sum(probabilities) == 0:
                    break
                probabilities = np.array(probabilities) / sum(probabilities)
                next_city = np.random.choice(range(num_cities), p=probabilities)
                path.append(next_city)
                visited[next_city] = True
                total_cost += graph[current_city][next_city]
                current_city = next_city

            # Powrót do miasta początkowego
            total_cost += graph[current_city][path[0]]
            path.append(path[0])
            all_paths.append((path, total_cost))
            all_costs.append(total_cost)

            # Aktualizacja najlepszego rozwiązania
            if total_cost < best_cost and len(path) == num_cities+1:
                best_cost = total_cost
                best_path = path

        # Aktualizacja feromonów
        pheromones *= (1 - rho)  # Odparowanie feromonów
        for path, cost in all_paths:
            for i in range(len(path) - 1):
                pheromones[path[i]][path[i+1]] += q / cost
    path = [int(x) for x in best_path]
    return path, best_cost

def display_graph(graph):
    """
    Wyświetla macierz sąsiedztwa grafu.

    :param graph: Macierz sąsiedztwa grafu
    """
    print("Macierz sąsiedztwa grafu:")
    for row in graph:
        print(" ".join(f"{weight:3}" for weight in row))

V=10
# V = int(input())
warunek = True 
while warunek:
    graph = generate_graph(V)
    path, cost = ant_colonyTSP(graph, V, 100, 1, 2, 0.5, 50)
    s = 0
    # cost, solution_vector = tsp(graph, s, V)
    # display_graph(graph)
    # print(ant_colonyTSP(graph, V, 100, 1, 2, 0.5, 50))
    graph_d = deleting_roads(graph, 10, V)
    # display_graph(graph_d)
    print(path, cost)
    # if not ant_colony_deletedTSP(graph_d, V, 100, 1, 2, 0.5, 50, path):
    print(ant_colony_deletedTSP(graph_d, V, 100, 1, 2, 0.5, 50, path))
    print()
    print()
        # warunek = False
