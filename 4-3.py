# import math
import numpy as np
import matplotlib.pyplot as plt

j = np.complex(0, 1)
e = np.e
pi = np.pi

#continuous
x = np.arange(-5, 5, 0.01)
y1 = np.cos(np.pi/3*x+np.pi/4)
y2 = np.asarray([2*e**(n) for n in list(x)])
y = y1*y2
plt.plot(x,y)

#show
plt.show()
