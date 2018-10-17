import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = [4.05, 0, 0]
b = [0, 4.05, 0]
c = [0, 0, 4.05]
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
plt.show()
