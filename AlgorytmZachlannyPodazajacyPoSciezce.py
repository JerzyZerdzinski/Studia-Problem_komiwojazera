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