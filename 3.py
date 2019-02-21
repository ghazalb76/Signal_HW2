# import math
import numpy as np
import matplotlib.pyplot as plt


y = input("signal?")
print(y)

#discrete
x = np.arange(-70.0, 70.0, 1)
plt.stem(x,y)

#show
plt.show()
