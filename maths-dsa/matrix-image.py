def manipulate(matrix):
    new=[]
    for row in matrix:
        n_row=row[::-1]
        f_row=[1-x for x in n_row]
        new.append(f_row)
    return new


matrix=[[1,1,0],[1,0,1],[0,0,0]]
print(manipulate(matrix))

