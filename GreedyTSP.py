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