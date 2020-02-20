# dataset = {
    # 'nbooks' = number of books in total
    # 'nlib' = number of libraries in total
    # 'days' = number of days available
    # 'scores' = a list of scores with its index corresponding to the book number
    # (so scores = [1, 2, 3] means book 0 has score 1 etc)

    # every (key, value) pair after this represent a library
    # 'lib_id': [lib_nbooks, lib_signup, lib_ship, [lib_books]]
    # example:
    #     '0': [5, 2, 2, [0, 1, 2, 3, 4]]
    # library 0 has 5 books, takes 2 days to signup, ship 2 books per day,
    # library 0 has books indexed 0, 1, 2, 3, 4
    #     (use this same index to find its score in scores list from line 6)
# }

# solution = [
#   [library_ID, [book_ID, ...]],
#   [library_ID, [book_ID, ...]],
#   ...
# ]

# solution = [
#     [1, [5,2,3]],
#     [0, [0,1,2,3,4]]
# ]


def solve(dataset):
    solution = [[1, [5, 2, 3]], [0, [0, 1, 2, 3, 4]]]
    current_time = 0
    available_libs = [x for x in range(dataset['nlib'])]

    # for lib in range(dataset['nlib']):
    #     current_library = dataset[lib]
    #
    #     if current_time +

    return solution
