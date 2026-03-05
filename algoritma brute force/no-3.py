# Nama: [Raka Restu Saputra]
# NIM: [247006111172]

import itertools

def solve_tsp_mini():
    dist = {
        'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
        'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
        'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
        'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
    }
    
    other_cities = ['B', 'C', 'D']
    permutations = list(itertools.permutations(other_cities))
    
    results = []
    for p in permutations:
        route = ['A'] + list(p) + ['A']
        total_dist = 0
        for i in range(len(route) - 1):
            total_dist += dist[route[i]][route[i+1]]
        results.append((route, total_dist))
        
    return results

all_routes = solve_tsp_mini()
for r, d in all_routes:
    print(f"Rute: {'-'.join(r)}, Jarak: {d}")