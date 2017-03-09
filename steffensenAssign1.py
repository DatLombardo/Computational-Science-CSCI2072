#Authour: Michael Lombardo
#SID: 100588642
#Date: 1/24/2017
#Assignment 1 : Steffesen

import math

def func(x):  #Declaration of Function
  return math.exp((-x**2 + x)) - (0.5*x) - 1.0836
def deriv(x): #Declaration of Function's Derivative
  return (-2*x + 1 *math.exp((-x**2 +x))) - 0.5

def Steffensen(x, err, kMax):
    for i in range(kMax):
        y1 = x
        y2 = y1 + (-func(y1) / deriv(y1))  #Newton Step One
        y3 = y2 + (-func(y2) / deriv(y2)) #Newton Step Two
        x = y1 - (((y2-y1)**2)/(y3-(2*y2)+y1)) #"Steffesen Method"
        res = abs(func(x)) #Determine Residual
        if (res < err): #Test for Converence
            print("Converged!\n")
            break
        print("x: "+ str(x) + "\tResidual: " + str(res))

Steffensen(1.0, 0.0000000000001, 30) #Run Function
