def binary_search(A, low, high, target):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if A[mid] == target:
        return mid
    elif target < A[mid]:
        return binary_search(A, low, mid - 1, target)
    else:
        return binary_search(A, mid + 1, high, target)

data = [3, 7, 10, 15, 18, 23, 29, 35]
target = 23

result = binary_search(data, 0, len(data) - 1, target)

print("Nama: Raka Restu Saputra")
print("NIM: 247006111172 \n")
print(f"Array: {data}")
print(f"Target: {target}")
if result != -1:
    print(f"Hasil: Target ditemukan pada indeks {result}")
else:
    print("Hasil: Target tidak ditemukan")