def insertion_sort(arr):
    total_steps = 0
    print(f"Data Awal: {arr}")
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        total_steps += 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
        print(f"Step {total_steps}: Sisipkan {key}, Array: {arr}")
        
    return arr, total_steps

data = [8, 3, 5, 2, 9, 1]

print("\nNama : Raka Restu Saputra")
print("NIM  : 247006111172\n")
sorted_data, total_iterations = insertion_sort(data)
print(f"\nHasil Sorting: {sorted_data}")
print(f"Total iterasi penyisipan: {total_iterations}")