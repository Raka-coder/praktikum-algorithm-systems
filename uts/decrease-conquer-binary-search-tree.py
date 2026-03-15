def binary_search_id(data, target):
    low = 0
    high = len(data) - 1
    steps = []
    
    while low <= high:
        mid = (low + high) // 2
        val = data[mid]
        steps.append((low, high, mid, val))
        
        if val == target:
            return mid, steps
        elif val < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1, steps

a, b, c = 1, 7, 2
n = 40 + 5*a + b
target = (a + b + c) * 4

dataset = [i * (a + 2) + c for i in range(1, n + 1)]

result_idx, history = binary_search_id(dataset, target)

print(f"Nama : Raka Restu Saputra")
print(f"NPM  : 247006111172\n")
print(f"a    : {a}, b: {b}, c: {c}")
print(f"n    : {n} data")
print(f"Target yang dicari: {target}")

print("\nDATASET ID BUKU LENGKAP:")
print("-" * 90)
print("Indeks | ID Buku |  | Indeks | ID Buku |  | Indeks | ID Buku |  | Indeks | ID Buku")
print("-" * 90)

for i in range(0, 52, 4):
    line = ""
    for j in range(4):
        idx = i + j
        if idx < 52:
            line += f"   {idx+1:3d}   |   {dataset[idx]:3d}   "
            if j < 3:
                line += "||"
    print(line)
print("-" * 90)

print("\nLANGKAH-LANGKAH BINARY SEARCH:")
print("-" * 70)
print(f"{'Iterasi':^8} | {'Low':^5} | {'High':^5} | {'Mid':^5} | {'A[Mid]':^8} | {'Keterangan':^20}")
print("-" * 70)

for i, (low, high, mid, val) in enumerate(history):
    low_display = low + 1
    high_display = high + 1
    mid_display = mid + 1
    
    if val == target:
        ket = f"{val} = {target} (ditemukan)"
    elif val < target:
        ket = f"{val} < {target} (ke kanan)"
    else:
        ket = f"{val} > {target} (ke kiri)"
    
    print(f"{i+1:^8} | {low_display:^5} | {high_display:^5} | {mid_display:^5} | {val:^8} | {ket:<20}")

print("-" * 70)

print("\nHASIL AKHIR:")
if result_idx != -1:
    print(f"Target {target} ditemukan!")
    print(f"Pada indeks ke-{result_idx + 1} (data ke-{result_idx + 1})")
    print(f"Nilai: {dataset[result_idx]}")
else:
    print(f"Target {target} tidak ditemukan dalam dataset.")
