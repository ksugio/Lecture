import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math as m

th = m.pi*30/180
a = [3.21, 0, 0]
b = [-3.21*m.sin(th), 3.21*m.cos(th), 0]
c = [0, 0, 5.21]
r = [[0, 0, 0], [2.0/3, 1.0/3, 0.5]]
M = [3, 3, 3]
# create crystal
AT = np.transpose(np.array([a, b, c]))
XYZ = []
for u3 in range(M[2]):
  for u2 in range(M[1]):
    for u1 in range(M[0]):
      for x, y, z in r:
        xyz = np.dot(AT, [u1+x, u2+y, u3+z])
        XYZ.append(xyz)
# plot 3D
XYZ = np.array(XYZ)
fig = plt.figure(figsize=plt.figaspect(1.0))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(XYZ[:,0], XYZ[:,1], XYZ[:,2], s=500)
ax.set_xlim([-5, 10])
ax.set_ylim([-1, 14])
ax.set_zlim([-1, 14])
plt.show()
