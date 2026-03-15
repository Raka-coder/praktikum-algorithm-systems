print("Nama : Raka Restu Saputra")
print("NPM  : 247006111172\n")

import itertools

def solve_tsp_brute_force():

    a, b, c = 1, 7, 2
    n_cities = 5 + a  
    
    matrix = [[0 for _ in range(n_cities + 1)] for _ in range(n_cities + 1)]
    for i in range(1, n_cities + 1):
        for j in range(1, n_cities + 1):
            if i == j:
                matrix[i][j] = 0 
            else:
                cost = ((abs(i - j) * a + b * j + c) % 30) + 5
                matrix[i][j] = cost

    print("MATRIKS BIAYA PERJALANAN:")
    for i in range(1, n_cities + 1):
        print(f"Dari Kota {i} -> ", end="")
        for j in range(1, n_cities + 1):
            if i == j:
                print("--", end=" ")
            else:
                print(f"{matrix[i][j]:2d}", end=" ")
        print()

    other_cities = list(range(2, n_cities + 1))
    min_cost = float('inf')
    best_path = []

    for p in itertools.permutations(other_cities):
        current_path = [1] + list(p)
        current_cost = 0
        
        for i in range(len(current_path) - 1):
            u, v = current_path[i], current_path[i+1]
            current_cost += matrix[u][v]
            
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path

    print("\nHASIL OPTIMASI RUTE (BRUTE FORCE)")
    print(f"Jumlah kemungkinan rute yang diperiksa: {len(list(itertools.permutations(other_cities)))}")
    print(f"Rute Perjalanan Terpendek: {' -> '.join(map(str, best_path))}")
    print(f"Total Biaya Minimum: {min_cost}")

if __name__ == "__main__":
    solve_tsp_brute_force()