# import math
import numpy as np
import matplotlib.pyplot as plt


#continuous
x = np.arange(0, 3/2, 0.01)
y1 = np.sin(2*np.pi/3*x)
y1 = abs(y1)
y2 = np.cos(4*np.pi/3*x)
y = y1+y2
plt.plot(x,y)

#discrete
x = np.arange(0, 3/2, 1)
y1 = np.sin(2*np.pi/3*x)
y1 = abs(y1)
y2 = np.cos(4*np.pi/3*x)
y = y1+y2
plt.stem(x,y)

#show
plt.show()
