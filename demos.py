
# selection_sort 
def selection_sort (arr):
    marker = 0
    while marker < len(arr):
        for num in range(marker, len(arr)):
            if arr[num] < arr[marker]:
                arr[marker], arr[num] = arr[num], arr[marker]
        marker +=1
    return arr


# quicksort 
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
    return quick_sort(smaller) + equal + quick_sort(larger)


# bubble sort 
def bubble_sort(arr):
    swap_hapened = True
    while swap_hapened:
        swap_hapened = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
               swap_hapened= True
               arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
        

# insertion sort
def insertion_sort(arr):
    key = 1
    for num in range(key, len(arr)):
        if arr[key] < arr[key-1]:
            arr[key-1], arr[key] = arr[key], arr[key-1]
            working_index = key - 1
            while arr[working_index] < arr[working_index - 1] and working_index != 0:
                arr[working_index-1], arr[working_index] = arr[working_index], arr[working_index- 1]
                working_index -= 1
        key += 1
    return arr
   

#merge sort
def merge_sorted(arr1, arr2):
    sorted_arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1  
        else:
            sorted_arr.append(arr2[j])
            j += 1
    while i < len(arr1): 
        sorted_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
    return sorted_arr


def mergesort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr)//2
       
        l1 = mergesort(arr[:middle])
        l2 = mergesort(arr[middle:])
        return merge_sorted(l1, l2)
      
def python_sort(arr):
    return arr.sort()
