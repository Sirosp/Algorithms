import gen_random_numbers as rand

def selection_sort(arr):
    n = len(arr)
  
    for i in range(n):
        #Iterate over the range of the array
        max_index = 0
        for y in range(0,n - i):
            if arr[y] > arr[max_index]:
                max_index = y

        arr[max_index],arr[n - i - 1] =  arr[n-i-1], arr[max_index]
        
    return arr

arr = rand.random_list(10)

print(selection_sort(arr))