import gen_random_numbers as rand

def insertion_sort(arr):
    """
    Move element until it reaches 0 or its sorted 
    position.
    """
    n = len(arr)
    for i in range(n):  
        min_index = i
        for k in range(i - 1,-1,-1):  
            if arr[k] > arr[min_index]:
               arr[k], arr[min_index] = arr[min_index], arr[k]
               min_index = k
            else:
                break
    return arr 
