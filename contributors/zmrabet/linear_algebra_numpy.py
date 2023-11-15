
#pip3 install numpy
#pip3 install pandas

import numpy as np
import pandas as pd

# ------------- Data Representation ------------- :

scalar = 1
vector = np.array([2,3,4])
matrix = np.array([[2,3,4],[5,3,4]])
tensor = np.array([[[2,3,4], [5,3,4]], [[8,9,5],[4,8,9]]])

print("Vector Shape : ", vector.shape)
print("Matrix Shape : ", matrix.shape)
print("Tensor Shape : ", tensor.shape)

print(f"Vector :\n{vector}\n")
print("----------------------")
print(f"Matrix :\n{matrix}\n")
print("----------------------")
print(f"Tensor :\n{tensor}\n")

# ------------- Matrix and Vector Operations : -------------

matrix1 = np.array([[10,10,12],[1,1,2]])
matrix2 = np.array([[9,7,4], [6,6,2]])

#Addition
print(f"addition : \n{matrix1 + matrix2}\n")

#Subtraction
print(f"subtraction : \n{matrix1 - matrix2}\n")

#Multiplication
print(f"multiplication : \n{matrix1 * matrix2}\n")

#Division
print(f"division : \n{matrix1 / matrix2}\n")

#Dot Product
matrix1 = np.array([[10,10,12],[1,1,2]])
matrix2 = np.array([[9,7], [6,6], [4,2]])
print(f"dot product : \n{matrix1.dot(matrix2)}\n")

#Reshape
print(f"reshape : \n{matrix2.reshape(2,3)}\n")

#Transpose
print(f"transpose : \n{matrix1.T}\n")

#identity
print(f"identity : \n{np.identity(3)}\n")

#inverse
"""
  There are two things to take into consideration with matrix inverse:
  1) the order of the matrix and matrix inverse does not matter even though
     most matrix dot products are different when the order changes;
  2) not all matrices have an inverse.
"""
matrix1 = np.array([[1, 1, 1], [0, 0, 2], [2, 0, 3]])
print(f"inverse :\n{np.linalg.inv(matrix1)}\n")

