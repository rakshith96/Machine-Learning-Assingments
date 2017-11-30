from scipy import linalg
import numpy as np
Data=np.array([[4.9,3.0,1.4,0.2],
	[4.7,3.2,1.3,0.2],
	[4.6,3.1,1.5,0.2],
	[5.0,3.6,1.4,0.2],
	[5.4,3.9,1.7,0.4],
	[4.6,3.4,1.4,0.3],
	[5.0,3.4,1.5,0.2],
	[4.4,2.9,1.4,0.2],
	[4.9,3.1,1.5,0.1],
	[5.4,3.7,1.5,0.2]])
print(" ")
print("The given Original Matrix is")
print(" ")
print(Data)

[m,n] = Data.shape
print(" ")
print("Original Matrix Shape is")
print(" ")
print("m : ", m,' ',"n : ", n)


data_mul_dataTranspose = Data.dot(Data.T)
dataTranspose_mul_data = (Data.T).dot(Data)


data_mul_dataTranspose_eigenvalues, data_mul_dataTranspose_eigenvectors = np.linalg.eig(data_mul_dataTranspose)
dataTranspose_mul_data_eigenvalues, dataTranspose_mul_data_eigenvectors = np.linalg.eig(dataTranspose_mul_data)

U = data_mul_dataTranspose_eigenvectors
V = dataTranspose_mul_data_eigenvectors
#S = np.diag(np.sqrt(data_mul_dataTranspose_eigenvalues)) #Dimensionality is higher
S = np.diag(np.sqrt(dataTranspose_mul_data_eigenvalues))
zeros = np.zeros(Data.shape, dtype = np.float32)
#print(S)
zeros[:S.shape[0], :S.shape[1]] = S
S = zeros

print(U, '\n')
print(V, '\n')
print(S, '\n')

print('Verification with original matrix\n')
verify = U.dot(S).dot(V.T)
print(verify)






