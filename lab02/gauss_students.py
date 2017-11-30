import numpy as np

def Gauss(A, b):
    '''
    Gaussian elimination with no pivoting.
    % input: A is an n x n nonsingular matrix
    %        b is an n x 1 vector
    % output: x is the solution of Ax=b.
    
    '''
    n =  len(A)
    if b.size != n:
        raise ValueError("Invalid argument: incompatible sizes between A & b.", b.size, n)
    for pivot_row in range(n-1):
        for row in range(pivot_row+1, n):
            multiplier = A[row][pivot_row]/A[pivot_row][pivot_row]
            #the only one in this column since the rest are zero
            A[row][pivot_row] = multiplier
            for col in range(pivot_row + 1, n):
                A[row][col] = A[row][col] - multiplier*A[pivot_row][col]
            #Equation solution column
            b[row] = b[row] - multiplier*b[pivot_row]
    print('REUSLTS AFTER GUASSIAN ELIMINATION')
    print('--------------------------------------')
    print(A)
    print(b)
    x = np.zeros(n)
    #print 'before',x
    k = n-1
    x[k] = b[k]/A[k,k]
    #print 'b value is ',b[k]
    while k >= 0:
        x[k] = (b[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
        k = k-1
    return x

if __name__ == "__main__":
    A = np.array([[2,-3,0],[4,-5,1],[2,-1,-3]])
    b =  np.array([[3],[7],[5]])
    print(Gauss(np.copy(A), np.copy(b)))
