import gen_random_numbers as rand
def bubble_sort(lis):
    n = len(lis)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j] 
                swapped = True
        if not swapped:
            break   
    return lis

