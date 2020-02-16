#### Code for Hash Code 2020
#### Hash Code practice problem - More pizza
#### Author - Jordan Ung <jordanung@protonmail.com>
#### Last edited: 16.02.20

FILE_NAME = 'b_small.in'

def find_optimal_slices(filename):
    max_slices = 0
    num_of_pizzas = 0
    pizza_slices = []

    with open(filename) as f:
        max_slices, num_of_pizzas = [int(x) for x in next(f).split()] # read first line
        for line in f: # read rest of lines
            pizza_slices += [int(x) for x in line.split()]

    pizza_dict = {}
    for index in range(len(pizza_slices)):
        current_slices = pizza_slices[index]
        
        temp_dict = {}
        for val in pizza_dict:
            if ((val + current_slices) not in pizza_dict) and \
                val + current_slices < max_slices:
                temp_dict[val + current_slices] = pizza_dict[val] + [index]

        if current_slices not in pizza_dict:
            temp_dict[current_slices] = [index]

        pizza_dict.update(temp_dict)

        # Check if the optimal maximum slices of pizza has been achieved
        if max_slices in pizza_dict:
            print(len(pizza_dict[max_slices]))
            print(" ".join(str(index) for index in pizza_dict[max_slices]))
            return

    # Printing the closest to the optimal maximum slices
    pizza_indexes = sorted(pizza_dict.items(), key=lambda x:x[0])[-1][1]
    print(len(pizza_indexes))
    print(" ".join(str(index) for index in pizza_indexes))

find_optimal_slices(FILE_NAME)