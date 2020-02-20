
#step 1: 

days_remaining = 0

# final solution, of form (chosen_library,chosen_library_books)
final_chosen_libraries = []

def find_next_best_library():

    library_ranking = []

    for library_number in range(dataset['nlib']):

        books_can_be_scanned = (days_remaining - dataset['libValues'][library_number]['lib_ndays']) * dataset['libValues'][library_number]['lib_nship']
        total_value_of_scanning = sum ([scores[book] for book in dataset['libValues'][library_number]['lib_books_ids']].sort( reverse=True)[:books_can_be_scanned] )

        ratio = total_value_of_scanning / dataset['libValues'][library_number]['lib_ndays']
        library_ranking.append((ratio, library_number))

    chosen_library = max (library_ranking)[1]
    chosen_library_books_can_be_scanned = (days_remaining - dataset['libValues'][chosen_library]['lib_ndays']) * dataset['libValues'][chosen_library]['lib_nship']
    chosen_library_books = [(scores[book],book) for book in dataset['libValues'][chosen_library]['lib_books_ids']].sort( reverse=True)[:chosen_library_books_can_be_scanned] )
    final_chosen_libraries.append((chosen_library,chosen_library_books))

    for book in library_books_data[chosen_library]:
        book_value_data[book] = 0

    days_remaining -= dataset['libValues'][library_number]['lib_ndays']

def solve(dataset):
    days_remaining = dataset['ndays']

    while (days_remaining > 0):
        find_next_best_library(dataset)

    solution = {
        'nlibs' : len(final_chosen_libraries)
        'libs' : []
    }

    for library in final_chosen_libraries:
        solution['libs'].append({'lib' : library[0], 'num_books': len(library[1]), 'books': library[1] })

    return (solution)



