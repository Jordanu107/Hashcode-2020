def write(solution, filename):
    with open(filename, 'w') as fo:
        fo.write(str(len(solution))+'\n')

        for sol in solution:
            fo.write(str(sol[0])+ ' ' + str(len(sol[1])) + '\n')
            for book in sol[1]:
                fo.write(str(book) + ' ')
            fo.write('\n')



# solution = [
#   [library_ID, [book_ID, ...]],
#   [library_ID, [book_ID, ...]],
#   ...
# ]

# solution = [
#     [1, [5,2,3]],
#     [0, [0,1,2,3,4]]
# ]
