import numpy as np
import matplotlib.pyplot as plot
from math import exp
from numpy.linalg import inv

def nX(xval):
    if abs(xval) >= 1:
        return 0
    return exp(1 / (abs(xval) ** 2 - 1))
X = []
F = []
for i in range(-50, 51):
    Xi = [1]
    F.append(nX(i/50))
    for j in range(1, 11):
        Xi.append((i/50) ** j)
    X.append(Xi)

X = np.array(X)
F = np.array(F)

XTX = np.matmul(np.transpose(X), X)

XTF = np.matmul(np.transpose(X), F)

A = np.matmul(inv(XTX), XTF)

if __name__ == '__main__':
    x = np.linspace(-1, 1, 101)
    P10 = A[0] + A[1] * x ** 1 + A[2] * x ** 2 + A[3] * x ** 3 + A[4] * x ** 4 + A[5] * x ** 5 + A[6] * x ** 6 + A[7] * x ** 7 + A[8] * x ** 8 + A[9] * x ** 9 + A[10] * x ** 10
    print(A)
    vals = []
    for i in range(-50, 51):
        vals.append(nX(i / 50))
    N_plot, = plot.plot(x, vals, color="black", label="$\eta$(x)", alpha = 0.75)
    P10_plot, = plot.plot(x, P10, ls = "dashed", color = "red", label = "$P_{10,101}(x)$")


    plot.xlabel("x")
    plot.ylabel("y")
    plot.title("10th Order Least Squares Approximation for $\eta$(x) with 101 Fitting Points")
    plot.legend(handles = [P10_plot, N_plot])
    plot.show()
