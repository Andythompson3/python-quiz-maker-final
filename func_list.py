import random

def rand_num(size):
    num_list = []
    for _ in range(size):
        num = random.randint(1, 30)  # Generates a random integer between 1 and 30 (inclusive)
        num_list.append(num)
    
    return (num_list)

