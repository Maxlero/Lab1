"""
    File name: main.py
    Author: Maxlero
    Variant: 11
    Date created: 18/02/2018
    Python Version: 3.6
"""

import matplotlib.pyplot as plt
import numpy as np

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


if __name__ == "__main__":
    draw()

    a = -0.5
    b = 0

    iterations = 0
    bisection(a, b)
