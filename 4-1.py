# import math
import numpy as np
import matplotlib.pyplot as plt


#continuous
x = np.arange(-5, 5, 0.01)
y = np.cos(np.pi/3*x+np.pi/4)
plt.plot(x,y)

#show
plt.show()
