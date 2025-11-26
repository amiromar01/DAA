def counting_sort(arr):
    if len(arr) == 0:
        return arr
    
    max_val = max(arr)
    min_val = min(arr)
    range_vals = max_val - min_val + 1
    
    count = [0] * range_vals

    for num in arr:
        count[num - min_val] += 1
    
    index = 0
    for i in range(range_vals):
        while count[i] > 0:
            arr[index] = i + min_val
            count[i] -= 1
            index += 1
            
    return arr
print(counting_sort([4, 2, 2, 8, 3, 3, 1]))  # Output: [1, 2, 2, 3, 3, 4, 8]
