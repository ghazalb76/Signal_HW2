# import math
import numpy as np
import matplotlib.pyplot as plt


j = np.complex(0, 1)
e = np.e
pi = np.pi

#continuous
x = np.arange(0, 2*pi, 0.1)
y = 2*np.asarray([e**(n) for n in list(x)])
plt.plot(x,y)

#show
plt.show()
