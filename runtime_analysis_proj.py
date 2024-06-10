import random
from demos import quick_sort, bubble_sort, insertion_sort, mergesort, python_sort
from timer import Timer

length = 'enter a number for the length of the list '
num_range = 'what is the largest number represented '
run_times= 'how many times would you like this to run '

# handle input errors 
def get_input(prompt):
    while True:
       
        try:
            resp = int(input(prompt))
            break
        except ValueError:
            print('this needs to be a number please try again')
    return resp

handled_length = get_input(length)
handled_num_range =get_input(num_range)
handled_run_time = get_input(run_times)

# create random integer list generator
def random_int_list(length, num_range):
    random_list = []
    for i in range(length):
        rand = random.randint(0, num_range)
        random_list.append(rand)
    return random_list

#
   
# get user input for size and range of list


# 
def analyze_func(func_name, arr):
    t = Timer()
    t.start()
    func_name(arr)
    t.stop(func_name)

    # ********************execution****************

for num in range(handled_run_time):
    print("-"*40)
    print(f"Run: {num+1}")
    l = (random_int_list(handled_length, handled_num_range))
    print(l)
    print(handled_length)
    print(handled_num_range)
    analyze_func(quick_sort,l)
    analyze_func(bubble_sort,l.copy())
    analyze_func(insertion_sort,l)
    analyze_func(mergesort,l)
    analyze_func(python_sort,l)
    print("-"*40)