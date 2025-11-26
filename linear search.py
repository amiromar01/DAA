def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i  
    return -1        
    
arr = [10, 25, 7, 14, 9]
key = 14
print("Element found at index:", linear_search(arr, key))
