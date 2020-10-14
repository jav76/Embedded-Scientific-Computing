import numpy as np
import matplotlib.pyplot as plot
import math

fittingPoints = 11
interval = [-1, 1]
lambdas = []
xVals = []
x = np.linspace(interval[0], interval[1], 1000)

def getXVals(n):
    dif = interval[1] - interval[0]
    for i in range(0, n):
        xVals.append(math.cos( (i * math.pi / (fittingPoints - 1) )))
        #print(xVals[i])

def funct(xVal):
    return np.exp(np.power(xVal * -1, 2.))

def getLambdas(n):
    for i in range(0, n):
        if i == 0 or i == (n - 1):
            l = math.pow(-1, i) * 0.5
        else:
            l = math.pow(-1, i)
        lambdas.append(l)
        #print(l)

def getBarycentric(n):
    num = 0
    den = 0
    for i in range(0, n):
        num = num + ( lambdas[i] * funct(xVals[i]) ) / ( x - xVals[i] )
        print(str(lambdas[i] * funct(xVals[i])) + " / (x - " + str(xVals[i]) + ")")
        den = den +  lambdas[i] / ( x - xVals[i] )
        print(str(lambdas[i]) + " / (x - " + str(xVals[i]) + ")")
    return num / den

getXVals(fittingPoints)
getLambdas(fittingPoints)

p = getBarycentric(fittingPoints)


error = True

if not error:

    f_plot, = plot.plot(x, funct(x), linewidth=1, color="black", label="f(x)")
    p_plot, = plot.plot(x, p, linewidth=1, ls="dashed", color="red", label="$P_{10}(x)$")
    plot.xlabel("x")
    plot.ylabel("y")
    plot.title("Barycentric Approximation of the Gaussian Function")
    plot.legend(handles = [f_plot, p_plot])
    plot.show()

else:

    error_plot, = plot.plot(x, funct(x) - p, label="Error")
    plot.xlabel("x")
    plot.ylabel("y")
    plot.title("Error of Barycentric Approximation")
    plot.legend(handles=[error_plot])
    plot.show()
