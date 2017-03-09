#Michael Lombardo
#100588642
#Assignment 2

import math
import numpy as np
import scipy
import scipy.linalg
import time
import matplotlib.pyplot as plt

#Generate full matrix, didn't bother making it only upper triangular
#as it would not effect the caluclation.
def generateMatrix(size):
    A = scipy.zeros((size,size))          #Generate 0 matrix
    for i in range(size):    #Iterate through row
        for k in range(size):   #Iterate through column
            A[k,i] = int(np.random.randint(1,10))#Fill in the columns with random values
    return A
#Genereate single vector as x value
def generateVector(size):
    A = scipy.zeros((size,1))          #Generate 0 matrix
    for i in range(size):
        A[i,0] = int(np.random.randint(1,10))  #Fill in the columns with random value
    return A

#Function Definition
def tridagMatvec(aMat,bMat,cMat,xVec,n):
    y = scipy.zeros((n,1))   #Initiatize Answer Vector
    for k in range(0,n):
        if (k == (n-1)):   #Reached bottom right, remove b and c
            y[k] = (aMat[k]*xVec[k])
        elif (k == (n-2)):   #Step before bottom right, remove c
            y[k] = (aMat[k]*xVec[k] + bMat[k]*xVec[k])
        else:       #Any other case which no vectors are ommitted
            y[k] = (aMat[k]*xVec[k] + bMat[k]*xVec[k] + cMat[k]*xVec[k])
    return y

#Hardcoded Size Value
size = 10
A = generateMatrix(size)
#Fill Empty Vectors
a =[0]*size
b=[0]*(size-1)
c=[0]*(size-2)
x = generateVector(size)
for i in range(size):
        if (i == (size-2)): #Last step which c is ommitted
            a[i] = A[i,i]
            b[i] = A[i,i+1]
        elif (i == size-1): #Arrived at bottom right corner
            a[i] = A[i,i]
        else:   #Normal step, all vectors included.

            a[i] = A[i,i]
            b[i] = A[i,i+1]
            c[i] = A[i,i+2]
#I commented out all of the matrixes and vectors to avoid terminal spam.
#print(a)
#print(b)
#print(c)
#print(A)
x = generateVector(size)
#print(x)
yAns = tridagMatvec(a,b,c,x,size)
print(yAns)

timearr = [0]*4
timearr2 = [0]*4
#Run algorthims for times.
for i in range(1,4):
    newSize = size**i
    A = generateMatrix(newSize)
    #Fill Empty Vectors
    a =[0]*newSize
    b=[0]*(newSize-1)
    c=[0]*(newSize-2)
    x = generateVector(newSize)
    for j in range(newSize):
            if (j == (newSize-2)): #Last step which c is ommitted
                a[j] = A[j,j]
                b[j] = A[j,j+1]
            elif (j == newSize-1): #Arrived at bottom right corner
                a[j] = A[j,j]
            else:   #Normal step, all vectors included.
                a[i] = A[j,j]
                b[i] = A[j,j+1]
                c[i] = A[j,j+2]
    start = time.time()*1000   #Conver time to Miliseconds
    y1Ans = tridagMatvec(a,b,c,x,newSize)
    end = time.time()*1000
    timearr[i] = end - start

    start = time.time()*1000
    y2Ans = np.matmul(A,x)
    end = time.time()*1000
    timearr2[i] = end - start
for i in range(4):
    print("\nTime in Miliseconds\n10^" + str(i+1)
    + "\nMy Algorithm: " + str(timearr[i])+ "\tBuilt in: " + str(timearr2[i]))

#I was only able to compute up to 10^4 on my Ubuntu VM without having memory
#issues.
xvalues = range(1,5) #Set Range
plt.plot(xvalues, timearr, '-', xvalues, timearr2, 'g^')  #Call plot

plt.yscale('log') #Change to log
plt.show          #Display
