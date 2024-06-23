def binary(list, num):
    low = 0
    hight = len(list)-1
    while low <= hight:
        mid = round((low+hight)/2)
        if num == list[mid]:
            return mid
        elif num < list[mid]:
            hight = mid-1
        else:
            low = mid+1
    
mylist = [1,2,3,4,5]
print(binary(mylist,5))