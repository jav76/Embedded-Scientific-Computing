import scipy.special as sp
import numpy
import matplotlib.pyplot as mp

"""
Approximate the zero order first kind bessel function
on the interval [0, 10] using a natural cubic spline
using interpolation points 
{0, 2.40482555769577, 3.83170597020751, 5.52007811028631, 7.01558666981561, 8.65372791291101, 10}
"""

x = numpy.linspace(0, 10)

y = sp.jv(0, x)

xVals = [0,                 #0
         2.40482555769577,  #1
         3.83170597020751,  #2
         5.52007811028631,  #3
         7.01558666981561,  #4
         8.65372791291101,  #5
         10                 #6
]

yVals = [
    sp.jv(0, xVals[0]),
    sp.jv(0, xVals[1]),
    sp.jv(0, xVals[2]),
    sp.jv(0, xVals[3]),
    sp.jv(0, xVals[4]),
    sp.jv(0, xVals[5]),
    sp.jv(0, xVals[6]),
]

deltaXVals = [
    xVals[1] - xVals[0],
    xVals[2] - xVals[1],
    xVals[3] - xVals[2],
    xVals[4] - xVals[3],
    xVals[5] - xVals[4],
    xVals[6] - xVals[5]
]

deltaYVals = [
    yVals[1] - yVals[0],
    yVals[2] - yVals[1],
    yVals[3] - yVals[2],
    yVals[4] - yVals[3],
    yVals[5] - yVals[4],
    yVals[6] - yVals[5]
]

coeff_list = [
    #b0                     c0                      d0                      b1                      c1                      d1                      b2                      c2                      d2                      b3                      c3                      d3                      b4                      c4                      d4                      b5                      c5                      d5
    [deltaXVals[0],         deltaXVals[0] ** 2,     deltaXVals[0] ** 3,     0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0],
    [1,                     2 * deltaXVals[0],      3 * deltaXVals[0] ** 2, -1,                     0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0],
    [0,                     2,                      6 * deltaXVals[0],      0,                      -2,                     0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0],

    [0,                     0,                      0,                      deltaXVals[1],          deltaXVals[1] ** 2,     deltaXVals[1] ** 3,     0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0],
    [0,                     0,                      0,                      1,                      2 * deltaXVals[1],      3 * deltaXVals[1] ** 2, -1,                     0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0],
    [0,                     0,                      0,                      0,                      2,                      6 * deltaXVals[1],      0,                      -2,                     0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0],

    [0,                     0,                      0,                      0,                      0,                      0,                      deltaXVals[2],          deltaXVals[2] ** 2,     deltaXVals[2] ** 3,     0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0],
    [0,                     0,                      0,                      0,                      0,                      0,                      1,                      2 * deltaXVals[2],      3 * deltaXVals[2] ** 2, -1,                     0,                      0,                      0,                      0,                      0,                      0,                      0,                      0],
    [0,                     0,                      0,                      0,                      0,                      0,                      0,                      2,                      6 * deltaXVals[2],      0,                      -2,                     0,                      0,                      0,                      0,                      0,                      0,                      0],

    [0,                     0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      deltaXVals[3],          deltaXVals[3] ** 2,     deltaXVals[3] ** 3,     0,                      0,                      0,                      0,                      0,                      0],
    [0,                     0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      1,                      2 * deltaXVals[3],      3 * deltaXVals[3] ** 2, -1,                     0,                      0,                      0,                      0,                      0],
    [0,                     0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      2,                      6 * deltaXVals[3],      0,                      -2,                     0,                      0,                      0,                      0],

    [0,                     0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      deltaXVals[4],          deltaXVals[4] ** 2,     deltaXVals[4] ** 3,     0,                      0,                      0],
    [0,                     0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      1,                      2 * deltaXVals[4],      3 * deltaXVals[4] ** 2, -1,                     0,                      0],
    [0,                     0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      2,                      6 * deltaXVals[4],      0,                      -2,                     0],

    [0,                     0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      deltaXVals[5],          deltaXVals[5] ** 2,     deltaXVals[5] ** 3],
    [0,                     2,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0],
    [0,                     0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      0,                      2,                      18]
]

b_list = [
    deltaYVals[0],
    0,
    0,
    deltaYVals[1],
    0,
    0,
    deltaYVals[2],
    0,
    0,
    deltaYVals[3],
    0,
    0,
    deltaYVals[4],
    0,
    0,
    deltaYVals[5],
    0,
    0
]

A = numpy.array(coeff_list)
B = numpy.array(b_list)
X = numpy.linalg.inv(A).dot(B)

if __name__ == '__main__':

    x0_1 = numpy.linspace(xVals[0], xVals[1])
    x1_2 = numpy.linspace(xVals[1], xVals[2])
    x2_3 = numpy.linspace(xVals[2], xVals[3])
    x3_4 = numpy.linspace(xVals[3], xVals[4])
    x4_5 = numpy.linspace(xVals[4], xVals[5])
    x5_6 = numpy.linspace(xVals[5], xVals[6])

    p0_1 = sp.jv(0, xVals[0]) +     (X[0] * (x0_1 - xVals[0])) +        (X[1] * (x0_1 - xVals[0]) ** 2) +       (X[2] * (x0_1 - xVals[0]) ** 3)
    print("yval: " + str(sp.jv(0, xVals[0])) + " xval: " + str(xVals[0]) + " b: " + str(X[0]) + " c: " + str(X[1]) + " d: " + str(X[2]))

    p1_2 = sp.jv(0, xVals[1]) +     (X[3] * (x1_2 - xVals[1])) +        (X[4] * (x1_2 - xVals[1]) ** 2) +       (X[5] * (x1_2 - xVals[1]) ** 3)
    print("yval: " + str(sp.jv(0, xVals[1])) + " xval: " + str(xVals[1]) + " b: " + str(X[3]) + " c: " + str(X[4]) + " d: " + str(X[5]))

    p2_3 = sp.jv(0, xVals[2]) +     (X[6] * (x2_3 - xVals[2])) +        (X[7] * (x2_3 - xVals[2]) ** 2) +       (X[8] * (x2_3 - xVals[2]) ** 3)
    print("yval: " + str(sp.jv(0, xVals[2])) + " xval: " + str(xVals[2]) + " b: " + str(X[6]) + " c: " + str(X[7]) + " d: " + str(X[8]))

    p3_4 = sp.jv(0, xVals[3]) +     (X[9] * (x3_4 - xVals[3])) +        (X[10] * (x3_4 - xVals[3]) ** 2) +      (X[11] * (x3_4 - xVals[3]) ** 3)
    print("yval: " + str(sp.jv(0, xVals[3])) + " xval: " + str(xVals[3]) + " b: " + str(X[9]) + " c: " + str(X[10]) + " d: " + str(X[11]))

    p4_5 = sp.jv(0, xVals[4]) +     (X[12] * (x4_5 - xVals[4])) +       (X[13] * (x4_5 - xVals[4]) ** 2) +      (X[14] * (x4_5 - xVals[4]) ** 3)
    print("yval: " + str(sp.jv(0, xVals[4])) + " xval: " + str(xVals[4]) + " b: " + str(X[12]) + " c: " + str(X[13]) + " d: " + str(X[14]))

    p5_6 = sp.jv(0, xVals[5]) +     (X[15] * (x5_6 - xVals[5])) +       (X[16] * (x5_6 - xVals[5]) ** 2) +      (X[17] * (x5_6 - xVals[5]) ** 3)
    print("yval: " + str(sp.jv(0, xVals[5])) + " xval: " + str(xVals[5]) + " b: " + str(X[15]) + " c: " + str(X[16]) + " d: " + str(X[17]))



    p0Plot, = mp.plot(x0_1, p0_1, color="blue", linewidth = 3, ls="dashed", label="p0")
    p1Plot, = mp.plot(x1_2, p1_2, color="green", linewidth = 3, ls="dashed", label="p1")
    p2Plot, = mp.plot(x2_3, p2_3, color="red", linewidth = 3, ls="dashed", label="p2")
    p3Plot, = mp.plot(x3_4, p3_4, color="cyan", linewidth = 3, ls="dashed", label="p3")
    p4Plot, = mp.plot(x4_5, p4_5, color="magenta", linewidth=3, ls="dashed", label="p4")
    p5Plot, = mp.plot(x5_6, p5_6, color="yellow", linewidth=3, ls="dashed", label="p5")

    J0, = mp.plot(x, y, color="black", linewidth=1, alpha=1, label="$J_0$")

    mp.xlabel("x")
    mp.ylabel("y")
    mp.title("Cubic Splines for 0 order first kind bessel function")
    mp.legend(handles=[p0Plot, p1Plot, p2Plot, p3Plot, p4Plot, p5Plot, J0])

    mp.ylim(-0.5, 1.25)
    mp.show()