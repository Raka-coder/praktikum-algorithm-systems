def find_max_crossing_subarray(arr, low, mid, high):

    left_sum = -float('inf')
    current_sum = 0
    for i in range(mid, low - 1, -1):
        current_sum += arr[i]
        if current_sum > left_sum:
            left_sum = current_sum
            
    right_sum = -float('inf')
    current_sum = 0
    for i in range(mid + 1, high + 1):
        current_sum += arr[i]
        if current_sum > right_sum:
            right_sum = current_sum
            
    return left_sum + right_sum

def find_maximum_subarray(arr, low, high):
    if low == high:
        return arr[low]
    
    mid = (low + high) // 2
    
    left_max = find_maximum_subarray(arr, low, mid)
    right_max = find_maximum_subarray(arr, mid + 1, high)
    cross_max = find_max_crossing_subarray(arr, low, mid, high)
    
    return max(left_max, right_max, cross_max)

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_sum = find_maximum_subarray(nums, 0, len(nums) - 1)

print("Nama: Raka Restu Saputra")
print("NIM: 247006111172 \n")
print(f"Array: {nums}")
print(f"Maximum Subarray Sum: {max_sum}")