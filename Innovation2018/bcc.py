import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = [2.87, 0, 0]
b = [0, 2.87, 0]
c = [0, 0, 2.87]
r = [[0, 0, 0], [0.5, 0.5, 0.5]]
M = [3, 3, 3]
# create crystal
AT = np.transpose([a, b, c])
XYZ = []
for u3 in range(M[2]):
  for u2 in range(M[1]):
    for u1 in range(M[0]):
      for x, y, z in r:
        xyz = np.dot(AT, [u1+x, u2+y, u3+z])
        XYZ.append(xyz)
# plot 3D
XYZ = np.array(XYZ)
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect((1,1,1))
ax.scatter(XYZ[:,0], XYZ[:,1], XYZ[:,2], s=500)
plt.show()

