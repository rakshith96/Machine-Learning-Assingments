
#eigen value and eigen vector finding without linalg.eig

import numpy as np
a=np.matrix([[8,-6,2],[-6,7,-4],[2,-4,3]])
print(a)
def sumOfDiagonals(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i][i]
    return sum

print('sum of diagonal values is',sumOfDiagonals([[8,-6,2],[-6,7,-4],[2,-4,3]]))

print('determinent of a is ',np.linalg.det(a)) # computes determinent of matrix

print(a)



# computing roots of a characteristic equation
coeff=[1,-18,45]
print('eigen values are',np.roots(coeff))

#eigen values are 15 and 3

b=np.matrix([[8,-6,2],[-6,7,-4],[2,-4,3]])

c=np.matrix([[15,0,0],[0,15,0],[0,0,15]])

z=b-c #A-3I
print('eigen vectors are',z)
p=np.matrix([[8,-6,2],[-6,7,-4],[2,-4,3]])

q=np.matrix([[3,0,0],[0,3,0],[0,0,3]])

y=p+q #A+2I
print('eigen vectors are',y)
# (1, -2) can be taken as an eigenvector associated with the eigenvalue -2, and (3, -1) as an eigenvector associated with the eigenvalue 3, as can be verified by multiplying them by A.


