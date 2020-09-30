
import numpy
import matplotlib.pyplot as mp

if __name__ == '__main__':
    coeff_list = [
        [1, 1, 1, 0, 0, 0, 0, 0, 0],
        [1, 2, 3, -1, 0, 0, 0, 0, 0],
        [0, 2, 6, 0, -2, 0, 0, 0, 0],
        [0, 0, 0, 2, 4, 8, 0, 0, 0],
        [0, 0, 0, 1, 4, 12, -1, 0, 0],
        [0, 0, 0, 0, 2, 12, 0, -2, 0],
        [0, 0, 0, 0, 0, 0, 3, 9, 27],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 18]
    ]
    b_list = [-1, 0, 0, 3/4, 0, 0, -7/4, 0, 0]

    A = numpy.array(coeff_list)
    B = numpy.array(b_list)
    X = numpy.linalg.inv(A).dot(B)

    x = numpy.linspace(0, 6)
    x0_1 = numpy.linspace(0, 1)
    x1_3 = numpy.linspace(1, 3)
    x3_6 = numpy.linspace(3, 6)

    p1 = 1      + (X[0] * (x - 0)) + (X[1] * (x - 0) ** 2) + (X[2] * (x - 0) ** 3) #0-1
    p2 = 0      + (X[3] * (x - 1)) + (X[4] * (x - 1) ** 2) + (X[5] * (x - 1) ** 3) #1-3
    p3 = 3/4    + (X[6] * (x - 3)) + (X[7] * (x - 3) ** 2) + (X[8] * (x - 3) ** 3) #3-6

    p0_1 = 1      + (X[0] * (x0_1 - 0)) + (X[1] * (x0_1 - 0) ** 2) + (X[2] * (x0_1 - 0) ** 3) #0-1
    p1_3 = 0      + (X[3] * (x1_3 - 1)) + (X[4] * (x1_3 - 1) ** 2) + (X[5] * (x1_3 - 1) ** 3) #1-3
    p3_6 = 3/4    + (X[6] * (x3_6 - 3)) + (X[7] * (x3_6 - 3) ** 2) + (X[8] * (x3_6 - 3) ** 3) #3-6

    mp.plot(x0_1, p0_1, color="purple", linewidth=5, alpha=0.5)
    mp.plot(x1_3, p1_3, color="purple", linewidth=5, alpha=0.5)
    mp.plot(x3_6, p3_6, color="purple", linewidth=5, alpha=0.5)

    mp.plot(x, p1, color = "red")
    mp.plot(x, p2, color = "green")
    mp.plot(x, p3, color = "blue")
    mp.xlabel("t")
    mp.ylabel("g(t)")

    mp.ylim(-3, 3)

    mp.show()
    print(X)


