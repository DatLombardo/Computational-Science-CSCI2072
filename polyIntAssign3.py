#Michael Lombardo
#100588642
#Assignment 3

import time
import math
import numpy as np
import scipy
import scipy.linalg

def generateVector(size):
    A = scipy.zeros((size,1))          #Generate 0 matrix
    for i in range(size):
        A[i,0] = i
    return A

def poly_int(X,Y):
    V = scipy.zeros((len(X),len(Y)))
    #Iterate through Row
    for i in range(len(X)):
        #Iterate through column
        for j in range(len(Y)):
            #Check if in column 1, if so always 1.
            if (j == 0):
                V[i,j] = 1
            if (i == j):
                total = 1
                #Use for the product
                for l in range(j):
                    total = total * (X[j] - X[l])
                V[i,j] = total
            elif (i > j):
                total = 1
                for l in range(0,j+1):
                    if (l == 0):
                        total = total * X[j+1]
                    else:
                        total = total * (X[j+1] - X[l])
                V[i,j] = total
    A = scipy.linalg.solve_triangular(V,Y)
    return A

size = 150
#For simplicity of a triangular matrix, solved using a sequence of values.
xMat = generateVector(size)
yMat = generateVector(size)

start = time.time()*1000
a = poly_int(xMat, yMat)
end = time.time()*1000
total = end - start


print("Size: " + str(size) + "\tTime in ms: " + str(total))
