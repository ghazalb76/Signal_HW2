import numpy as np
import matplotlib.pyplot as plt
import math


print("Please enter the array of x:")
x = list(map(int, input().split()))
print("Please enter the array of y:")
y = list(map(int, input().split()))

f = dict(zip(x, y))
fo = [(f[i] - f[-i])/2 for i in x]
fe = [(f[i] + f[-i])/2 for i in x]

# original signal
chart1 = plt.subplot(311)
plt.plot(x, y)

# odd part of signal
chart2 = plt.subplot(312)
plt.plot(x, fo)

# even part of signal
chart3 = plt.subplot(313)
plt.plot(x, fe)

plt.show()
