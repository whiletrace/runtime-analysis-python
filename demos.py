
# selection_sort 
def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
   
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
            
    return smallest_index

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    
    return new_arr

# test 
print(selection_sort([100, 5, 67, 32, 1, 90, 4, 6, 12]))


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

    
# XXXXXXXXXXXX Program Execution XXXXXXXXXXXXXXXXXXX  # noqa: E305
l = [5, 8, 10, 23, 2, 3, 9, 7, 4, 1]  # noqa: E741
print(quick_sort(l))


# bubble sort 
def bubble_sort(arr):
    swap_hapened = True
    while swap_hapened:
        print('bubble_sort status: ' + str(arr))
        swap_hapened = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
               swap_hapened= True
               arr[i], arr[i+1] = arr[i+1], arr[i]
        

l = [ 6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
bubble_sort(l) 


# insertion sort
 def insertion_sort(arr):
    
    key = 1
    for num in range(key, len(arr)):
        if arr[key] < arr[key-1]:
            arr[key-1], arr[key] = arr[key], arr[key-1]
            print(' outer loop swap happened', arr)
            working_index = key - 1
    
            while arr[working_index] < arr[working_index - 1] and working_index != 0:
                arr[working_index-1], arr[working_index] = arr[working_index], arr[working_index- 1]
                print('inner loop swap happened ', arr)
                working_index -= 1
        key += 1
        print(arr)
   
l = [5, 2, 6, 1, 20, 32, 45, 1,  4, 8, 10, 7, 8, 9, 2]
insertion_sort(l)


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
        print(sorted_arr)
    while i < len(arr1): 
        sorted_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
        return sorted_arr


def divide_arr(arr):
    if len(arr) < 2:
        print(f"Base condition reached with {arr}")
        return arr[:]
    else:
        middle = len(arr)//2
        
        l1 = divide_arr(arr[:middle])
        l2 = divide_arr(arr[middle:])
        return merge_sorted(l1, l2)
      
# XXXXXXXXXXXX Program Execution XXXXXXXXXXXXXXXXXXX
l = [8, 6, 2, 5, 18, 101, 32, 34, 4, 59, 46, 23, 12, 10, 11, 99]    

print(divide_arr(l))
