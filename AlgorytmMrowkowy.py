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