def sq_matrix(n):
    for i in range(0,n*n,n):
        for j in range(1,n+1):
            print("{0:>2}".format(j+i), end=" ")
        print()

sq_matrix(5)