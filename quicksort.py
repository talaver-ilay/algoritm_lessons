def quicksort(array):
    if len(array) < 2:
        return array
    else:
        base = array[0]
        less = [i for i in array[1:] if i < base]
        greater = [i for i in array[1:] if i > base]
        return quicksort(less) + [base] + quicksort(greater)
    
print(quicksort([90,23,775,223,2,3,4,31,363,765,30]))
