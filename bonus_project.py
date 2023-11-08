import matplotlib.pyplot as plt
import numpy as np
import math

class MY_CONST(object):
    k = 2
    A = [1, 3, 5]

class MY_LINE(object):
    x = [0, 0, 0]
    y = [0, 0, 0]
    color = ['r', 'g', 'b']

fig, ax = plt.subplots()

n = 100 # number of points
for i in range (0, 3):
    # create a x vector
    MY_LINE.x[i] = np.linspace(0, MY_CONST.A[i], n)
    # compute y
    MY_LINE.y[i] = MY_LINE.x[i] ** (3 / 2) / (3 * math.sqrt(MY_CONST.A[i])) - math.sqrt(MY_CONST.A[i]) * (MY_LINE.x[i] ** (1 / 2)) + 2 * MY_CONST.A[i] / 3
    ax.plot(MY_LINE.x[i], MY_LINE.y[i], label = "A = {}".format(MY_CONST.A[i]), color = MY_LINE.color[i])
ax.legend()
ax.grid(True)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('$f(x)=x ^ 1.5 / (3 * math.sqrt(A)) - math.sqrt(A) * (x ^ 0.5) + 2 * A / 3$')
plt.show()  # just for py file