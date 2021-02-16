import numpy as np
import math as m

def Fg(h, k, l, r):
  fg = complex(0, 0)
  for x, y, z in r:
    th = 2.0*m.pi*(h*x+k*y+l*z)
    fg += complex(m.cos(th), m.sin(th))
  return abs(fg)

def TwoTheta(gd, Lam):
  sth = Lam*gd/2
  if sth <= 1:
    return 2*m.asin(sth)*180/m.pi
  else:
    return -1

def RLPV(a, b, c):
  V = np.dot(a, np.cross(b, c))
  aa = np.cross(b, c)/V
  ba = np.cross(c, a)/V
  ca = np.cross(a, b)/V
  return [aa, ba, ca]

a = [4.05, 0, 0]
b = [0, 4.05, 0]
c = [0, 0, 4.05]
r = [[0, 0, 0], [0.5, 0.5, 0], [0.5, 0, 0.5], [0, 0.5, 0.5]]
HKL = [[0, 5], [0, 5], [0, 5]]
Lam = 1.54
# create Table
rlpv = RLPV(a, b, c)
AT = np.transpose(rlpv)
Dspace = []
for l in range(HKL[2][0], HKL[2][1]+1):
  for k in range(HKL[1][0], HKL[1][1]+1):
    for h in range(HKL[0][0], HKL[0][1]+1):
      g = np.dot(AT, [h, k, l])
      gd = m.sqrt(g[0]*g[0]+g[1]*g[1]+g[2]*g[2])
      tt = TwoTheta(gd, Lam)
      fg = Fg(h, k, l, r)
      if gd > 0 and tt > 0 and fg > 1.0e-6:
        Dspace.append([tt, h, k, l, 1.0/gd])
# print Table
print('2th, h, k, l, d')
for tt, h, k, l, d in sorted(Dspace):
  print('%.3f, %d, %d, %d, %.3f' % (tt, h, k, l, d))


