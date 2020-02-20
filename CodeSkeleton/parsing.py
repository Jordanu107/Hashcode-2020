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

# dataset = { this is the sample input
#     'nbooks': 6
#     'nlib': 2
#     'ndays': 7
#     'scores': [1, 2, 3, 6, 5, 4]
#     '0': [5, 2, 2, [0, 1, 2, 3, 4]] 
#     '1': [4, 3, 1, [3, 2, 5, 0]]
# }

def parse(filename):
    with open(filename, 'r') as fi:
        nbooks, nlib, ndays = map(int, fi.readline().split())
        scores = list(map(int, fi.readline().split()))

        dataset = {
            'nbooks' : nbooks,
            'nlib' : nlib,
            'ndays' : ndays,
            'scores' : scores,
            'libValues' : []
        }

        for j in range(nlib):
            lib_nbooks, lib_ndays, lib_nship = map(int, fi.readline().split())
            lib_books_ids = list(map(int, fi.readline().split()))
            dataset['libValues'].append ( {
                'lib_nbooks' : lib_nbooks, 'lib_ndays' : lib_ndays, 'lib_nship':lib_nship, 'lib_books_ids': lib_books_ids})
        
        return dataset
