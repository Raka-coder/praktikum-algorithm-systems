# Nama: [Raka Restu Saputra]
# NIM: [247006111172]

def subset_sum_brute_force(A, target):
    n = len(A)
    total_subsets = 2**n
    results = []
    
    for i in range(total_subsets):
        current_subset = []
        current_sum = 0
        for j in range(n):
            
            if (i >> j) & 1:
                current_subset.append(A[j])
                current_sum += A[j]
        
        if current_sum == target:
            results.append(current_subset)
            
    return results, total_subsets

A = [3, 5, 9, 12]
target = 17

solutions, checked = subset_sum_brute_force(A, target)

print(f"Subset yang memenuhi target: {solutions}")
print(f"Total subset yang diperiksa: {checked}")