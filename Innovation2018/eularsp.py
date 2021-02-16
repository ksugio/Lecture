import numpy as np
import matplotlib.pyplot as plt

def Force(r):
  k = 2.1
  r0 = 3.253
  return -k*(r-r0)

dt = 0.1
nloop = 300
M = 1
t = 0
r = 3.0
v = 0
R = []
T = []
# Eular method
for i in range(nloop):
  v = v + dt*Force(r)/M
  r = r + dt*v
  t = t + dt
  R.append(r)
  T.append(t)
# plot
print(np.mean(R))
plt.plot(T, R)
plt.xlabel('t')
plt.ylabel('r')
plt.show()
