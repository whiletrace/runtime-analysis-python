import random

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

    



# ********************execution****************
print(random_int_list(length, num_range))
