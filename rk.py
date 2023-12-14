import numpy as np
import math
import scipy as s 

x0 = 0
xn = 2
n= 4

h = (xn-x0)/n
def f(x,y):
    return y*(1+x**2)
x = [x0 + i*h for i in range(n+1)]
y = [1]

for i in range(n):
    k1 = h*f(x[i],y[i])
    k2 = h*f(x[i]+h,y[i]+k1)
    yapprox = y[i] + (k1+k2)/2
    y.append(yapprox)

yexact = [s.exp(x[i]+x[i]**2) for i in range(n+1)]
print(yexact)
print(y)


