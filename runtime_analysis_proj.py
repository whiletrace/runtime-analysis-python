import random
from demos import quick_sort, bubble_sort, insertion_sort, mergesort
from timer import Timer
# part 1 create random integer list generator
def random_int_list(length, num_range):
    
    # create a list 
    random_list = []
     # create n number of random integers
    for i in range(length):
        rand = random.randint(0, num_range)
        # place random integers in the list 
        random_list.append(rand)
    # return the list     
    return random_list
   
# part 2 get user input for size and ranget of list

length = int(input('how many items would you like in the list '))
num_range = int(input("what is the highest number represented in the list "))
run_times = int(input("How many timew do you want to run? "))

def analyze_func(func_name, arr):
    t = Timer()
    t.start()
    func_name(arr)
    t.stop(func_name)

    # ********************execution****************

for num in range(run_times):
    print("-"*40)
    print(f"Run: {num+1}")
    l = (random_int_list(length, num_range))
    analyze_func(quick_sort,l)
    analyze_func(bubble_sort,l.copy())
    analyze_func(insertion_sort,l)
    analyze_func(mergesort,l)
    print("-"*40)