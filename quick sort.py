def quick_sort(arr):
    arr = arr[:] 
    _quick_sort(arr, 0, len(arr) - 1)
    return arr

def _quick_sort(a, low, high):
    if low < high:
        p = partition(a, low, high)
        _quick_sort(a, low, p - 1)
        _quick_sort(a, p + 1, high)

def partition(a, low, high):
    pivot = a[high]
    i = low

    for j in range(low, high):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1

    a[i], a[high] = a[high], a[i]
    return i

print(quick_sort([3,6,8,10,1,2,1])) # Output: [1, 1, 2, 3, 6, 8, 10]