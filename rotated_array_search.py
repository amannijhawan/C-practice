# Finding an element in a rotated sorted array
pivot_array = [21,25,26,27,20,21,22]

def find_pivot(array, low, high):
    if high < low:
        return -1
    elif low == high:
        return low
    else:
        mid = (low + high)/2
        if array[mid] > array[mid+1]:
            return mid+1
        elif array[mid] < array[mid-1]:
            return mid
        elif array[mid] > array[mid + 1]:
            return find_pivot(array,mid+1, high)
        else:
            return find_pivot(array,low, mid-1)

def search(pivot_array, item):
    array=pivot_array
    pivot = find_pivot(pivot_array,0, len(pivot_array))
    print "pivot %d" % pivot
    if array[pivot]<item<=array[-1]:
        return binary_search(item,pivot_array, pivot, len(pivot_array))
    elif array[0] <= item <array[pivot-1]:
        return binary_search(item,pivot_array, 0, pivot)
    else: 
        return pivot

def binary_search(item,array, low, high):
    print array, low, high
    if low == high:
       return low
    if low > high:
       return -1

    mid = (low + high)/2
    if  item == array[mid]:
        return mid
    elif item > array[mid]:
        return binary_search(item, array,mid+1, high)
    else:
        return binary_search(item, array,low, mid-1)

location = search(pivot_array, 25)    
if location !=-1:
   print pivot_array[location]        
