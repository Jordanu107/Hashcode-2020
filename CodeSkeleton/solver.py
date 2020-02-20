days_remaining = 0

# final solution, of form (chosen_library,chosen_library_books)
final_chosen_libraries = []

def find_next_best_library(dataset):
    # print ('doing another round')
    # print(dataset)
    global days_remaining
    global final_chosen_libraries

    library_ranking = []

    for library_number in range(dataset['nlib']):

        books_can_be_scanned = ( days_remaining - dataset['libValues'][library_number]['lib_ndays']) * dataset['libValues'][library_number]['lib_nship']
        books = [dataset['scores'][book] for book in dataset['libValues'][library_number]['lib_books_ids']]
        books.sort( reverse=True)
        total_value_of_scanning = sum (books[:books_can_be_scanned] )

        ratio = total_value_of_scanning / dataset['libValues'][library_number]['lib_ndays']
        library_ranking.append((ratio, library_number))

    chosen_library = max (library_ranking)[1]
    chosen_library_books_can_be_scanned = ( days_remaining - dataset['libValues'][chosen_library]['lib_ndays']) * dataset['libValues'][chosen_library]['lib_nship']
    chosen_library_books = [(dataset['scores'][book],book) for book in dataset['libValues'][chosen_library]['lib_books_ids']]
    chosen_library_books.sort( reverse=True)
    chosen_library_books=chosen_library_books[:chosen_library_books_can_be_scanned]
    if (len(chosen_library_books) >0):
        final_chosen_libraries.append((chosen_library,chosen_library_books))

    days_remaining -= dataset['libValues'][library_number]['lib_ndays']

    return chosen_library

def solve(dataset):
    global days_remaining 
    global final_chosen_libraries
    days_remaining = dataset['ndays']

    while (days_remaining > 0):
        chosen_library = find_next_best_library(dataset)

        #set value of adding that book on as 0, since scanned already
        for book in dataset['libValues'][chosen_library]['lib_books_ids']:
            dataset['scores'][book] = 0

        # bit of a hack to ensure that we don't choose the same library again: can't just remove it form the list
        # since that would change the position of all other libraries in the list (index is important)
        dataset['libValues'][chosen_library]['lib_nbooks'] = 0
        dataset['libValues'][chosen_library]['lib_books_ids'] = []

        
    solution = {
        'nlibs' : len( final_chosen_libraries),
        'libs' : []
    }

    for library in final_chosen_libraries:
        solution['libs'].append({'lib' : library[0], 'num_books': len(library[1]), 'books': library[1] })

    print (solution)
    return (solution)



