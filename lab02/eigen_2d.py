#eigen value and eigen vector finding without linalg.eig

import numpy as np
a=np.matrix([[4,3],[-2,-3]])
print(a)
def sumOfDiagonals(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i][i]
    return sum

print('sum of diagonal values is',sumOfDiagonals([[4,3],[-2,-3]]))

print('determinent of a is ',np.linalg.det(a)) # computes determinent of matrix

print(a)



# computing roots of a characteristic equation
coeff=[1,-1,-6]
print('eigen values are',np.roots(coeff))

#eigen values are 3 and -2

b=np.matrix([[4,3],[-2,-3]])

c=np.matrix([[3,0],[0,3]])

z=b-c #A-3I
print('eigen vectors are',z)
p=np.matrix([[4,3],[-2,-3]])

q=np.matrix([[2,0],[0,2]])

y=p+q #A+2I
print('eigen vectors are',y)
# (1, -2) can be taken as an eigenvector associated with the eigenvalue -2, and (3, -1) as an eigenvector associated with the eigenvalue 3, as can be verified by multiplying them by A.


