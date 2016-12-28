import numpy as np
import math
from matplotlib import pyplot as plt

x0 = input("Initial x: ")
y0 = input("Initial y: ")
xf = input("To what value of x do you want me to approximate y? ")
h = input("h: ")
n = int((xf-x0)/h)
x = np.linspace(x0,xf,n+1)
y = np.zeros([n+1])
y[0] = y0

def Slope(x,y):
	return math.cos(x)

for i in range(1,n):
	y[i+1] = y[i] + Slope(x[i], y[i])*h

for i in range(n):
	print(x[i], y[i])

plt.plot(x,y, linestyle="-", marker = "o")
plt.xlabel("Value of x")
plt.ylabel("Value of y")
plt.title("Euler's Method h = " + str(h))
plt.show()
