"""
    File name: main.py
    Author: Maxlero
    Variant: 11
    Date created: 18/02/2018
    Python Version: 3.6
"""

import matplotlib.pyplot as plt
import numpy as np
from sympy import diff, symbols, exp

# Constants
accuracy = 0.00001
iterations = 0


def f(x):
    return np.exp(-x) - 5 * x ** 2 + 10 * x


def bisection(left, right):
    global iterations
    global accuracy

    if f(left) * f(right) < 0:
        x = (left + right) / 2
        if f(x) != 0 and abs(f(x)) > accuracy:
            iterations += 1
            if f(left) * f(x) < 0:
                bisection(left, x)
            else:
                bisection(x, right)
        else:
            print(str(iterations) + " iterations; x = " + str("%.9f" % x) +
                  "; f(x) = " + str("%.9f" % f(x)) +
                  " <= " + str("%.5f" % accuracy))
    else:
        print("No root on [" + str(left) + ", " + str(right) + "].")


def draw():
    x = np.arange(-5.0, 5.0, 0.1)

    plt.plot(x, f(x))
    plt.axis([-2, 4, -2, 7])
    plt.grid(True)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()


def draw2():
    # f(x) = x
    # f(x) = - e^(-x) / 10 + x^2 / 2
    x = np.arange(-5.0, 5.0, 0.1)

    plt.plot(x, x)
    plt.plot(x, -np.exp(-x) / 10 + x ** 2 / 2)
    plt.axis([-2, 4, -2, 7])
    plt.grid(True)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()


def draw3():
    # f'(x) = - e^(-x) - 10 * x + 10
    # f'(x) > 0 on [-0.5, 0]
    x = np.arange(-0.5, 0, 0.01)

    plt.plot(x, - np.exp(-x) - 10 * x + 10)
    plt.axis([-2, 2, -1, 15])
    plt.grid(True)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()


def g(x):
    # M = max|f'(x)| on [a, b]
    M = abs(- np.exp(0.5) - 10 * (-0.5) + 10)
    l = 1 / M
    return x - l * (np.exp(-x) - 5 * x ** 2 + 10 * x)


def iteration(x0):
    global iterations
    global accuracy

    if abs(f(x0)) > accuracy:
        iterations += 1
        x = g(x0)
        iteration(x)
    else:
        print(str(iterations) + " iterations; x = " + str("%.9f" % x0) +
              "; f(x) = " + str("%.9f" % f(x0)) +
              " <= " + str("%.5f" % accuracy))


def k(x):
    # f(x) = e^(-x) - 5 * x^2 + 10 * x
    # f'(x) = - e^(-x) - 10 * x + 10
    return x - f(x) / (-np.exp(-x) - 10 * x + 10)


def newton(x0):
    global iterations
    global accuracy

    if abs(f(x0)) > accuracy:
        iterations += 1
        x = k(x0)
        newton(x)
    else:
        print(str(iterations) + " iterations; x = " + str("%.9f" % x0) +
              "; f(x) = " + str("%.9f" % f(x0)) +
              " <= " + str("%.5f" % accuracy))


if __name__ == "__main__":
    draw()
    a = -0.5
    b = 0

    ####################################################################################################################
    # bisection method
    ####################################################################################################################

    iterations = 0
    bisection(a, b)

    ####################################################################################################################
    # iteration method
    ####################################################################################################################

    # f(x) = e^(-x) - 5 * x^2 + 10 * x
    draw2()

    # f'(x) = - e^(-x) - 10 * x + 10
    # x = symbols('x')
    # print(diff(exp(-x) - 5 * x ** 2 + 10 * x))
    draw3()

    # next x = g(x) = x - l * f(x) = x - l * (e^(-x) - 5 * x^2 + 10 * x)
    iterations = 0
    x0 = -.25
    iteration(x0)

    ####################################################################################################################
    # Newton method
    ####################################################################################################################

    # x = x0 - f(x0)/f'(x0)
    iterations = 0
    x0 = -.25
    newton(x0)
