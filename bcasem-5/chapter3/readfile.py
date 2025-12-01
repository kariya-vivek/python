import numpy as np
import pylab as plt

data = np.loadtxt('fakedata.txt')
plt.plot(data[:,0], data[:,1], 'ro')  # 'ro' means red circles

plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0.0, 10)
plt.show()

