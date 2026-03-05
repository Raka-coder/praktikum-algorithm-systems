def max_crossing_sum(A, low, mid, high):

    sum_left = -float('inf')
    curr_sum = 0
    for i in range(mid, low - 1, -1):
        curr_sum += A[i]
        if curr_sum > sum_left:
            sum_left = curr_sum
            
    sum_right = -float('inf')
    curr_sum = 0
    for i in range(mid + 1, high + 1):
        curr_sum += A[i]
        if curr_sum > sum_right:
            sum_right = curr_sum
            
    return sum_left + sum_right

def max_subarray(A, low, high):
    if low == high:
        return A[low]
    
    mid = (low + high) // 2
    
    left_max = max_subarray(A, low, mid)
    right_max = max_subarray(A, mid + 1, high)
    cross_max = max_crossing_sum(A, low, mid, high)
    
    return max(left_max, right_max, cross_max)

# Data Uji
data = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

result = max_subarray(data, 0, len(data) - 1)

print("Nama: Raka Restu Saputra")
print("NIM: 247006111172")
print(f"Array: {data}")
print(f"Jumlah Subarray Maksimum: {result}")