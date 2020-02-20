# dataset = {
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
            'nbooks' = nbooks
            'nlib' = nlib
            'ndays' = ndays
            'scores' = scores
            'libValues' = []
        }

        for j in range(nlib):
            lib_nbooks, lib_ndays, lib_nship = map(int, fi.readline().split())
            lib_books_id = list(map(int, fi.readline().split()))
            dataset['libValues'].append ( [lib_nbooks, lib_ndays, lib_nship, lib_books_id])
        
        return dataset 
