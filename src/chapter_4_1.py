from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np

T, K = 0.5, 1
P = tf([0, K], [T, 1])
y, t = step(P, np.arange(0, 5, 0.01))

fig, ax = plt.subplots()

ax.plot(t, y)
plt.grid()
plt.show()