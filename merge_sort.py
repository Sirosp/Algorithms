import gen_random_numbers as rand
import math
def merge_sort(arr):
   
    if(len(arr) == 1 or len(arr) == 0):
        return arr
    else:
        arr1 = arr[0:math.ceil(len(arr)/2)]
        arr2 = arr[math.ceil(len(arr)/2)::]
    divide1 = merge_sort(arr1)
    divide2 = merge_sort(arr2)
    merge_arr = merge(divide1,divide2)
    return merge_arr

def merge(arr1,arr2):
    if arr1 == None:
        return arr2
    elif arr2 == None:
        return arr1
    n1,n2 = len(arr1),len(arr2)
    merged_arr = []
    x,y = 0,0
    while True:
        if x == n1:
            for i in range(y,n2):
                merged_arr.append(arr2[i])
            break
        if y == n2:
            for i in range(x,n1):
                merged_arr.append(arr1[i])
            break
        
        if arr1[x] < arr2[y]:
            merged_arr.append(arr1[x])
            x += 1
        else:
            merged_arr.append(arr2[y])
            y += 1
    return merged_arr