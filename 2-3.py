# import math
import numpy as np
import matplotlib.pyplot as plt


j = np.complex(0, 1)
e = np.e
pi = np.pi

#continuous
x = np.arange(0, 6, 0.1)
y = np.asarray([e**(j*pi*n/3)+e**(j*4*pi*n/3) for n in list(x)])
plt.plot(x,y)

#discrete
x = np.arange(0, 6, 1)
y = np.asarray([e**(j*pi*n/3)+e**(j*4*pi*n/3) for n in list(x)])
plt.stem(x,y)

#show
plt.show()
