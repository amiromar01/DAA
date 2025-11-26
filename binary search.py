def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1  
    return -1
arr = [2, 5, 7, 10, 14, 20]
key = 10
print("Element found at index:", binary_search(arr, key))
