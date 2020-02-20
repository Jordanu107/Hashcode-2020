
#step 1: 

days_remaining = 0

final_chosen_libraries = []

def find_next_best_library():

    library_ranking = []

    for library_number in range(dataset['nlib']):

        books_can_be_scanned = (days_remaining - dataset['libValues'][library_number][1]) * dataset['libValues'][library_number][2]
        total_value_of_scanning = sum ([book_value_data for book in library_books_data[library_number]].sort( reverse=True)[:books_can_be_scanned] )

        ratio = total_value_of_scanning / library_time_to_open_data
        library_ranking.append((ratio, library_number))

    chosen_library = max (library_ranking)[1]

    final_chosen_libraries.append(chosen_library)

    for book in library_books_data[chosen_library]:
        book_value_data[book] = 0

    days_remaining -= library_days_to_open_data[library_number]

def solve(dataset):
    days_remaining = dataset['ndays']

    while (days_remaining > 0):
        find_next_best_library(dataset)



