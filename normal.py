#Michael Lombardo
#100588642
#Midterm : Normal.py

import math
import numpy as np
import scipy
import scipy.linalg

def generateMatrix(size):
    A = scipy.zeros((size,size))          #Generate 0 matrix
    for i in range(size):    #Iterate through row
        for k in range(size):   #Iterate through column
            A[k,i] = int(np.random.randint(1,10))#Fill in the columns with random values
    return A

def normal(X):
    n = X.ndim
    V = scipy.zeros(n,n)
    for i in range(n):
        for j in range(n):
            V[i,j] = X[i]^(j)
    Vtrans = np.transpose(V)
    Norm = np.matmul(Vtrans,V)
    return Norm

X = generateMatrix(3)
print(normal(X))
