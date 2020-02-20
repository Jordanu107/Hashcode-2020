#### Code for Hash Code 2020
#### Hash Code practice problem - More pizza
#### Author - Jordan Ung <jordanung@protonmail.com>
#### Last edited: 20.02.20

#### https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt


# def find_optimal_slices(filename):
#     max_slices = 0
#     num_of_pizzas = 0
#     pizza_slices = []

#     with open(filename) as file:
#         # Read the maximum slices of pizza allowed and numbers of pizzas
#         max_slices, num_of_pizzas = [int(x) for x in next(file).split()]

#         # Read how many slices each pizza contains
#         pizza_slices = [int(x) for x in next(file).split()]

#     pizza_dict = {0:[]}

#     # Cycle through all the pizzas and generate all the possible slice amounts
#     for index in range(len(pizza_slices)):
#         current_slices = pizza_slices[index]
        
#         temp_dict = {}
#         for val in pizza_dict:

#             # Too many slices of pizza, don't need
#             if val + current_slices > max_slices:
#                 continue

#             # Optimal pizza slices achieved, printing results
#             elif val + current_slices == max_slices:
#                 # print(" + ".join(str(pizza_slices[i]) for i in (pizza_dict[val] + [index])))
#                 # total = 0
#                 # for i in (pizza_dict[val] + [index]):
#                 #     total += pizza_slices[i]
#                 # print(total)
#                 print(len(pizza_dict[val]) + 1)
#                 print(" ".join(str(i) for i in (pizza_dict[val] + [index])))
#                 return

#             # Check that we aren't adding redundant information
#             elif ((val + current_slices) not in pizza_dict):
#                 temp_dict[val + current_slices] = pizza_dict[val] + [index]


#         # Update our slice amount tracker
#         pizza_dict.update(temp_dict)

#     # The optimal number hasn't been achieved - find closest to optimal
#     pizza_indexes = sorted(pizza_dict.items(), key=lambda x:x[0])[-1][1]
#     print(len(pizza_indexes))
#     print(" ".join(str(index) for index in pizza_indexes))

import sys

def find_optimal_slices(filename):
    max_slices = 0
    num_of_pizzas = 0
    pizza_slices = []

    with open(filename) as file:
        # Read the maximum slices of pizza allowed and numbers of pizzas
        max_slices, num_of_pizzas = [int(x) for x in next(file).split()]

        # Read how many slices each pizza contains
        pizza_slices = [int(x) for x in next(file).split()]

    
    pizza_list = [ [0] * (max_slices + 1) for _ in range(num_of_pizzas)]

    # 'hard code' for the first column/item
    for capacity in range(max_slices+1):
        current_slice = pizza_slices[0]

        if capacity < current_slice:
            pizza_list[0][capacity] = 0
        else:
            pizza_list[0][capacity] = current_slice
       
        # elif capacity == current_slice:
        #     pizza_list[0][capacity] = current_slice
        # else:
        #     pizza_list[0][capacity] = pizza_list[0][capacity - 1]

    # Fill out the highest possible amount of pizza given the pizza slice
    # capacity and whether the current pizza is eaten or not

    for pizza in range(1, len(pizza_list)):
        current_slice = pizza_slices[pizza]

        # if (pizza == 1):
        #     print("curslice = " + current_slice)

        for capacity in range(max_slices + 1):

            # Capacity too small, just put what the largest could fit in capacity - 1
            if capacity < current_slice:
                # if (pizza == 1 ):
                    # print("capacity was less than current_slice" :)
                pizza_list[pizza][capacity] = pizza_list[pizza - 1][capacity]

            else:
                pizza_list[pizza][capacity] = max(pizza_list[pizza - 1][capacity], pizza_list[pizza - 1][capacity-current_slice] + current_slice)

            

            # # Just the right size for the pizza!
            # elif capacity == current_slice:
            #     pizza_list[pizza][capacity] = current_slice

            # # Have more capacity for pizza slices than the current slice of pizza
            # else:

            #     if pizza_list[pizza][capacity - current_slice] + current_slice <= max_slices:
            #         pizza_list[pizza][capacity] = max(pizza_list[pizza - 1][capacity],
            #                                           pizza_list[pizza - 1][capacity - current_slice] +
            #                                           current_slice)
            #     else:
            #         pizza_list[pizza][capacity] = pizza_list[pizza - 1][capacity]



    # # Back traverse through to find the pizzas that were consumed
    highest_pizza_value = pizza_list[-1][-1]
    current_column = max_slices
    pizzas_chosen = []


    # Don't look a tthe first pizza row, account for below
    for i in range(len(pizza_list) - 1, 0, -1):

        try:
            if pizza_list[i-1][current_column] != highest_pizza_value:
                # DID choose this pizza
                current_column = current_column - pizza_slices[i]
                highest_pizza_value = highest_pizza_value - pizza_slices[i]
                pizzas_chosen.append(i)
        except IndexError:
            print("error was" + str(i-1) + " " + str(current_column))
            print(pizzas_chosen)
        

    # now consider the first pizza
    if pizza_list[0][current_column] != 0:
        pizzas_chosen.append(0)

    total_score = 0
    for pizza in pizzas_chosen:
        total_score += pizza_slices[pizza]


    print(len(pizzas_chosen))
    print(" ".join(str(pizza_number) for pizza_number in pizzas_chosen))
    print("total score is" + str (total_score), file=sys.stderr)



# find_optimal_slices(FILE_NAME)
# find_optimal_slices('a_example.in')
find_optimal_slices('b_small.in')
# find_optimal_slices('c_medium.in')
# find_optimal_slices('d_quite_big.in')
# find_optimal_slices('e_also_big.in')
