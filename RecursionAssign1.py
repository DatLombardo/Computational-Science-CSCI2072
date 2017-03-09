#Authour: Michael Lombardo
#SID: 100588642
#Date: 1/24/2017
#Assignment 1 : Recursion

import math
#Hardcoded Test Values, Converges at 18 iterations
maxIter = 20
prevX = 6
error = 0.00000001
residualErr = 0.0005

def func(x): #Function Definition
    return ((1/(2*math.pi))*(math.sin(math.pi*x))) - ((1/(2*math.pi))*(x**2)) + x

def iteration(intial, kMax, epsX, epsF):
    nextX = func(intial) #Obtain next x(k) value
    err = abs(nextX - intial) #Calculate error of x
    res = abs(func(nextX))  #Calculate residual
    print("x: " + str(nextX) + " res: " + str(res) + " err: " + str(err))
    if (err < epsX) or (res < epsF): #Check for break
        print("Converged!")
        return
    if (kMax == 0):   #Hit max iteration count
        return
    iteration(nextX, kMax-1, epsX, epsF) #Recursive Trace(call)

print("Initial Value: \t" + str(prevX))
iteration(prevX, maxIter, error, residualErr)
