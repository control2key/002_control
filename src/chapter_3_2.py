from control.matlab import *

Np = [0, 1]
Dp = [1, 2, 3]

P = tf(Np, Dp)
Pss = tf2ss(P)
print(P)
print(Pss)
