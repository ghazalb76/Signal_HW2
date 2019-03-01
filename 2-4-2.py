import numpy as np
import matplotlib.pyplot as plt

#cos(9*x)
chart1 = plt.subplot(311)

#continuous
x = np.arange(-5, 5, 0.01)
y = np.cos(9*x)
plt.plot(x,y)

#discrete
x = np.arange(-5, 5, 1)
y = np.cos(9*x)
plt.stem(x,y)

#-------------------------------------#

#sin(2*np.pi*x)
chart2 = plt.subplot(312)

#continuous
x = np.arange(-5, 5, 0.01)
y = np.sin(2*np.pi*x)
plt.plot(x,y)

#discrete
x = np.arange(-5, 5, 1)
y = np.sin(2*np.pi*x)
plt.stem(x,y)

plt.show()