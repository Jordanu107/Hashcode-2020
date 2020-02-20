def write(solution, filename):
    with open(filename, 'w') as fo:
        fo.write(str(solution['nlibs'])+'\n')
        libs_string = ""
        for lib in solution['libs']:
            libs_string += str(lib['lib']) +  " "
        fo.write(libs_string +'\n')
        for lib in solution['libs']:
            libs_books_string = ""
            for book in lib['books']:
                libs_books_string += str(book[1]) + " "
            fo.write(libs_books_string +'\n')

    return filename


# solution = [
#   [library_ID, [book_ID, ...]],
#   [library_ID, [book_ID, ...]],
#   ...
# ]

# solution = [
#     [1, [5,2,3]],
#     [0, [0,1,2,3,4]]
# ]
