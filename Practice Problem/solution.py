#### Code for Hash Code 2020
#### Hash Code practice problem - More pizza
#### Author - Jordan Ung <jordanung@protonmail.com>
#### Last edited: 16.02.20

FILE_NAME = 'a_example.in'

def find_optimal_slices(filename):
    max_slices = 0
    num_of_pizzas = 0
    pizza_slices = []

    with open(filename) as file:
        # Read the maximum slices of pizza allowed and numbers of pizzas
        max_slices, num_of_pizzas = [int(x) for x in next(file).split()]

        # Read how many slices each pizza contains
        for line in file:
            pizza_slices += [int(x) for x in line.split()]

    pizza_dict = {}

    # Cycle through all the pizzas and generate all the possible slice amounts
    for index in range(len(pizza_slices)):
        current_slices = pizza_slices[index]
        
        temp_dict = {}
        for val in pizza_dict:
            # Check that we aren't adding redundant information
            if ((val + current_slices) not in pizza_dict) and \
                val + current_slices < max_slices:
                temp_dict[val + current_slices] = pizza_dict[val] + [index]

        if current_slices not in pizza_dict:
            temp_dict[current_slices] = [index]

        # Update our slice amount tracker
        pizza_dict.update(temp_dict)

        # Check if the optimal maximum slices of pizza has been achieved
        if max_slices in pizza_dict:
            print(len(pizza_dict[max_slices]))
            print(" ".join(str(index) for index in pizza_dict[max_slices]))
            return

    # The optimal number hasn't been achieved - find closest to optimal
    pizza_indexes = sorted(pizza_dict.items(), key=lambda x:x[0])[-1][1]
    print(len(pizza_indexes))
    print(" ".join(str(index) for index in pizza_indexes))

# find_optimal_slices(FILE_NAME)
# find_optimal_slices('b_small.in')
# find_optimal_slices('c_medium.in')
find_optimal_slices('d_quite_big.in')
# find_optimal_slices('e_also_big.in')