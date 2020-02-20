def score(solution, dataset):
    print("---------- Scoring ----------")
    current_time = 0
    books_scanned = []
    with open(solution) as file:
        # Read number of libraries to be signed up for scanning
        num_of_libraries = [int(x) for x in next(file).split()][0]

        time_allowed = dataset['ndays']
        for lib in range(num_of_libraries):
            library_id, books_per_day = [int(x) for x in next(file).split()]
            book_order = [int(x) for x in next(file).split()]
            print(dataset['libValues'][library_id]['lib_ndays'])
            current_time += dataset['libValues'][library_id]['lib_ndays']

            # Library has enough time to sign up and scan through all of it's books
            if ((dataset['libValues'][library_id]['lib_nbooks'] / books_per_day) + current_time +
                dataset['libValues'][library_id]['lib_ndays']) <= time_allowed:
                books_scanned += dataset['libValues'][library_id]['lib_books_ids']

            # Library won't have enough time to scan all, if any books...
            else:
                scanned_books = time_allowed - current_time - dataset['libValues'][library_id]['lib_ndays']
                books_scanned += book_order[:scanned_books]

        books_scanned = list(set(books_scanned))
        scoring_list = [dataset['scores'][x] for x in books_scanned]

        print("The total value obtained is: {}".format(sum(scoring_list)))
        print("The amount of unique books scanned is: {}".format(len(books_scanned)))
        print(" ".join(str(x) for x in books_scanned))

# Assume solution file will be of format:
# <number of libraries signed up for scanning>
# <id of first library to be signed up and how many it will send per day e.g. 1 3>
# <order of the books being scanned from first library to be scanned e.g. 5 2 3>
# <id of second library...>
# <order of the books scanned at library two...>
