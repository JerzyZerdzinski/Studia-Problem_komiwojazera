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
import random
import numpy as np
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

for i in range(4, 50):
    graph = generate_graph(i)
    if i<=10:
        path, cost = ant_colonyTSP(graph, i, 100, 1, 2, 0.5, 10*i)
        start = time.time()
        ant_colony_deletedTSP(graph, i, 100, 1, 2, 0.5, 10*i, path)
        end=time.time()
    elif i<=50:
        path, cost = ant_colonyTSP(graph, i//2, 10*i, 1, 2, 0.3, 10*i)
        start = time.time()
        ant_colony_deletedTSP(graph, i//2, 10*i, 1, 2, 0.3, 10*i, path)
        end = time.time()
    else:
        path, cost = ant_colonyTSP(graph, int(i*0.3), 5*i, 1, 2, 0.1, 10*i)
        star = time.time()
        ant_colony_deletedTSP(graph, int(i*0.3), 5*i, 1, 2, 0.1, 10*i, path)
        end=time.time()
    wynik = end - start
    print(wynik)
for i in range(4, 50):
    print(i)
