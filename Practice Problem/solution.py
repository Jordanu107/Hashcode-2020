#### Code for Hash Code 2020
#### Hash Code practice problem - More pizza
#### Author - Jordan Ung <jordanung@protonmail.com>
#### Last edited: 17.02.20

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

    pizza_dict = {0:[]}

    # Cycle through all the pizzas and generate all the possible slice amounts
    for index in range(len(pizza_slices)):
        current_slices = pizza_slices[index]
        
        temp_dict = {}
        for val in pizza_dict:

            # Optimal pizza slices achieved, printing results
            if val + current_slices == max_slices:
                # print(" + ".join(str(pizza_slices[i]) for i in (pizza_dict[val] + [index])))
                # total = 0
                # for i in (pizza_dict[val] + [index]):
                #     total += pizza_slices[i]
                # print(total)
                print(len(pizza_dict[val]) + 1)
                print(" ".join(str(i) for i in (pizza_dict[val] + [index])))
                return

            # Too many slices of pizza, don't need
            elif val + current_slices > max_slices:
                continue

            # Check that we aren't adding redundant information
            elif ((val + current_slices) not in pizza_dict):
                temp_dict[val + current_slices] = pizza_dict[val] + [index]


        # Update our slice amount tracker
        pizza_dict.update(temp_dict)

    # The optimal number hasn't been achieved - find closest to optimal
    pizza_indexes = sorted(pizza_dict.items(), key=lambda x:x[0])[-1][1]
    print(len(pizza_indexes))
    print(" ".join(str(index) for index in pizza_indexes))

# find_optimal_slices(FILE_NAME)
# find_optimal_slices('b_small.in')
# find_optimal_slices('c_medium.in')
find_optimal_slices('d_quite_big.in')
# find_optimal_slices('e_also_big.in')