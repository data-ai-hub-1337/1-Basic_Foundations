# Linear Algebra Operations with NumPy

## Data Representation:

Scalars, Vectors, Matrices, and Tensors:

Scalar: A single numerical value represented by scalar = ```1```.

Vector: An array of numbers represented by vector = ```np.array([2, 3, 4])```. It has a shape of (3,) indicating three elements.

Matrix: A 2D array of numbers represented by matrix = ```np.array([[2, 3, 4], [5, 3, 4]])```. It has a shape of (2, 3) indicating two rows and three columns.

Tensor: A 3D array of numbers represented by tensor = ```np.array([[[2, 3, 4], [5, 3, 4]], [[8, 9, 5], [4, 8, 9]]])```. It has a shape of (2, 2, 3) indicating two matrices, each of size 2x3.

## Matrix and Vector Operations:

Basic Arithmetic Operations:

Addition: 
```matrix1 + matrix2```

Subtraction: 
```matrix1 - matrix2```

Multiplication: Element-wise multiplication 
- ```matrix1 * matrix2```

Division: Element-wise division 
- ```matrix1 / matrix2```

Advanced Operations:
Dot Product: Matrix multiplication 
- ```matrix1.dot(matrix2)```

Reshape: Reshaping a matrix 
- ```matrix2.reshape(2, 3)```

Transpose: Transposing a matrix - 
```matrix1.T```

Identity Matrix: 
```np.identity(3)``` creates a 3x3 identity matrix.

Inverse: Computing the inverse of a matrix - 
```np.linalg.inv(matrix1)```

Cross Product: Computing the cross product of two matrices - 
```np.cross(matrix1, matrix2)```

These operations demonstrate fundamental concepts in linear algebra and their implementation using the NumPy library in Python. 
Feel free to explore and experiment with different matrices and vectors to deepen your understanding of these mathematical operations.
