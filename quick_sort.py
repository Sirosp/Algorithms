import gen_random_numbers as rand

def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    pivot_index = n//2
    pivot_val = arr[pivot_index]
    arr[n-1], arr[pivot_index] = arr[pivot_index], arr[n-1]

    left_pivot = 0
    right_pivot = n-2
  
    while left_pivot <= right_pivot:

        while left_pivot <= right_pivot and arr[left_pivot] < pivot_val:
            left_pivot += 1

        while left_pivot <= right_pivot and arr[right_pivot] > pivot_val:
            right_pivot -= 1
        
        if left_pivot < right_pivot:
            arr[left_pivot], arr[right_pivot] = arr[right_pivot], arr[left_pivot]
            left_pivot += 1
            right_pivot -= 1
    
    arr[left_pivot], arr[n-1] = arr[n-1], arr[left_pivot]

    left_part = quick_sort(arr[:left_pivot])
    right_part = quick_sort(arr[left_pivot + 1:])

    return left_part + [pivot_val] + right_part


arr = rand.random_list(10)

print(quick_sort(arr))