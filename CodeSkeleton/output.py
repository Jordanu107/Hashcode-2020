def write(solution, filename):
    with open(filename, 'w') as fo:
        fo.write(str(len(solution))+'\n')
        for elt in solution:
            fo.write(str(elt)+' ')