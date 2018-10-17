import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math as m

th = m.pi*30/180
a = [3.21, 0, 0]
b = [-3.21*m.sin(th), 3.21*m.cos(th), 0]
c = [0, 0, 5.21]
r = [[0, 0, 0], [2.0/3, 1.0/3, 0.5]]
HKL = [[-2, 2], [-2, 2], [-2, 2]]
# create RL primitive vector
V = np.dot(a, np.cross(b, c))
aa = np.cross(b, c)/V
ba = np.cross(c, a)/V
ca = np.cross(a, b)/V
# create RL
AT = np.transpose([aa, ba, ca])
Ghkl = []
for l in range(HKL[2][0], HKL[2][1]+1):
  for k in range(HKL[1][0], HKL[1][1]+1):
    for h in range(HKL[0][0], HKL[0][1]+1):
      ghkl = np.dot(AT, [h, k, l])
      Ghkl.append(ghkl)
# plot 3D
Ghkl = np.array(Ghkl)
fig = plt.figure(figsize=plt.figaspect(1.0))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(Ghkl[:,0], Ghkl[:,1], Ghkl[:,2], s=100)
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1.5, 1.5])
plt.show()
