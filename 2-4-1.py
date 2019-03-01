import numpy as np
import matplotlib.pyplot as plt


#continuous
x = np.arange(-5, 5, 0.01)
y1 = np.cos(9*x)
y2 = np.sin(2*np.pi*x)
y = y1+y2
plt.plot(x,y)

#discrete
x = np.arange(-5, 5, 1)
y1 = np.cos(9*x)
y2 = np.sin(2*np.pi*x)
y = y1+y2
plt.stem(x,y)

#show
plt.show()
