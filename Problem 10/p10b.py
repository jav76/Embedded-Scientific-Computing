import numpy as np
import matplotlib.pyplot as plot
from math import exp
from numpy.linalg import inv
import scipy.special as sp

X = []
F = []
for i in range(0, 1000):
    Xi = [1]
    F.append(sp.jv(0, i/100))
    for j in range(1, 9):
        Xi.append((i/100) ** j)
    X.append(Xi)

X = np.array(X)
F = np.array(F)

XTX = np.matmul(np.transpose(X), X)

XTF = np.matmul(np.transpose(X), F)

A = np.matmul(inv(XTX), XTF)

if __name__ == '__main__':
    x = np.linspace(0, 10, 1001)
    P10 = A[0] + A[1] * x ** 1 + A[2] * x ** 2 + A[3] * x ** 3 + A[4] * x ** 4 + A[5] * x ** 5 + A[6] * x ** 6 + A[7] * x ** 7 + A[8] * x ** 8
    print(A)

    J0_plot, = plot.plot(x, sp.jv(0, x), color="black", label="$J_0$(x)", alpha = 0.75)
    P8_plot, = plot.plot(x, P10, ls = "dashed", color = "red", label = "$P_{8,1001}(x)$")

    #plot.ylim(-0.5, 20)
    plot.xlabel("x")
    plot.ylabel("y")
    plot.title("8th Order Least Squares Approximation for $J_0$(x) with 1001 Fitting Points")
    plot.legend(handles = [P8_plot, J0_plot])
    plot.show()
