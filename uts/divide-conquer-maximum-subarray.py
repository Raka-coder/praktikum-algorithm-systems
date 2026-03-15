def find_max_crossing_subarray(A, low, mid, high):
    left_sum = -float('inf')
    total = 0
    max_left = mid
    for i in range(mid, low - 1, -1):
        total += A[i]
        if total > left_sum:
            left_sum = total
            max_left = i
            
    right_sum = -float('inf')
    total = 0
    max_right = mid + 1
    for j in range(mid + 1, high + 1):
        total += A[j]
        if total > right_sum:
            right_sum = total
            max_right = j
            
    return (max_left, max_right, left_sum + right_sum)

def find_max_subarray(A, low, high):
    if high == low:
        return (low, high, A[low])
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_max_subarray(A, low, mid)
        right_low, right_high, right_sum = find_max_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)
        
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)

a, b, c = 1, 7, 2
n = 10 + a + b
dataset = []
for i in range(1, n + 1):
    val = (i * a * b - c * i) % 40 - 10
    dataset.append(val)

low_idx, high_idx, max_profit = find_max_subarray(dataset, 0, len(dataset) - 1)

print(f"Nama : Raka Restu Saputra")
print(f"NPM  : 247006111172\n")
print(f"a    : {a}, b: {b}, c: {c}")
print(f"n    : {n} data")

print("\nDATASET PERUBAHAN KEUNTUNGAN:")
print("-" * 100)
print("i      :", end=" ")
for i in range(1, n + 1):
    print(f"{i:4d}", end=" ")
print()
print("P(i)   :", end=" ")
for val in dataset:
    print(f"{val:4d}", end=" ")
print()
print("-" * 100)

print("\nHASIL SUBARRAY MAKSIMUM:")
print(f"Indeks awal      : {low_idx} (data ke-{low_idx + 1})")
print(f"Indeks akhir     : {high_idx} (data ke-{high_idx + 1})")
print(f"Panjang subarray : {high_idx - low_idx + 1} elemen")
print(f"Elemen subarray  : {dataset[low_idx : high_idx + 1]}")
print(f"Total keuntungan : {max_profit}")