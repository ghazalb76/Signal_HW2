# import math
import numpy as np
import matplotlib.pyplot as plt


j = np.complex(0, 1)
e = np.e

#continuous
x = np.arange(-40.0, 40.0, 0.1)
y = np.asarray([e**(j*3/7*n) for n in list(x)])
plt.plot(x,y)

#discrete
x = np.arange(-70.0, 70.0, 1)
y = np.asarray([e**(j*3/7*n) for n in list(x)])
plt.stem(x,y)

#show
plt.show()
