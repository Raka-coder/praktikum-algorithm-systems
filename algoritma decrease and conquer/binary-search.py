def binary_search(arr, low, high, target, steps=0):
    steps += 1
    if low > high:
        print(f" Step {steps}: Target tidak ditemukan.")
        return -1, steps
    
    mid = (low + high) // 2
    print(f" Step {steps}: cari di index [{low}-{high}], Mid index: {mid} (Nilai: {arr[mid]})")
    
    if arr[mid] == target:
        return mid, steps
    elif target < arr[mid]:
        return binary_search(arr, low, mid - 1, target, steps)
    else:
        return binary_search(arr, mid + 1, high, target, steps)

arr = [3, 7, 10, 15, 18, 23, 29]
target = 18

print("Nama : Raka Restu Saputra")
print("NIM  : 247006111172\n")
print(f"Target: {target}")
result, total_steps = binary_search(arr, 0, len(arr) - 1, target)
print(f"\nIndex ditemukan: {result}")
print(f"Total langkah pencarian: {total_steps}")