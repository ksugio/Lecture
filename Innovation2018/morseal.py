import numpy as np
import matplotlib.pyplot as plt

D = 0.2703
A = 1.1646
r0 = 3.253
# plot
R = np.linspace(0, 10, 101)
Ur = D*np.exp(-2*A*(R-r0))-2*D*np.exp(-A*(R-r0))
Fr = -2*A*D*np.exp(-2*A*(R-r0))+2*A*D*np.exp(-A*(R-r0))
plt.plot(R, Ur)
plt.plot(R, Fr)
plt.ylim([-0.5, 1])
plt.xlabel('r')
plt.ylabel('U(r), F(r)')
plt.show()
