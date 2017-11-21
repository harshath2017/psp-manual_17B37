def matrixmulti(X, Y):
    # X dimension is M x N
    # Y dimension is N x P
    M = len(X)
    N = len(X[0])
    P = len(Y[0])
    
    # resultant matrix dimension is M x P
    Z = [[0] * P  for row in range(M)]
    
    if  N != len(Y):  
        print ("Incorrect dimensions.")
        return

    for i in range(M):
        for j in range(P):
            for k in range(N):
                Z[i][j] += X[i][k] * Y[k][j]

    return Z

X = [1,2],[3,4]
Y = [2,1],[4,6]
print(matrixmulti(X,Y))
