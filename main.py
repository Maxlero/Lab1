"""
    Автор: Орел Максим
    Группа: КБ-161
    Вариант: 11
    Дата создания: 18/02/2018
    Python Version: 3.6
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import derivative

# Constants
accuracy = 0.00001
iterations = 0
a = -0.5
b = 0


def draw(function_f, x1, x2, y1, y2, x_left, x_right):
    x = np.arange(x_left, x_right, 0.01)

    plt.plot(x, function_f(x))
    plt.axis([x1, x2, y1, y2])
    plt.grid(True)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()


def f(x):
    return np.exp(-x) - 5 * x ** 2 + 10 * x


def diff_f(point):
    return derivative(f, point, dx=1e-6)


def max_diff(a, b):
    step = 0.01  # шаг
    max_value = 0  # максимальное значение
    array = np.arange(a, b + step, step)
    for i in array:
        if abs(diff_f(i)) > abs(max_value):
            max_value = diff_f(i)
    return max_value


def g(x, l):
    return x - l * f(x)


def bisection(left, right):
    global iterations
    global accuracy

    x = (left + right) / 2
    if f(x) != 0 and abs(f(x)) > accuracy:
        iterations += 1
        if f(left) * f(x) < 0:
            bisection(left, x)
        else:
            bisection(x, right)
    else:
        print("Корень: " + str("%.9f" % x))
        print("Количество итераций: " + str(iterations))
        print("Проверка: f(x) = " + str("%.2e" % f(x)) +
              " <= " + str(accuracy))


def iteration(x0, l):
    global iterations
    global accuracy

    if f(x0) != 0 and abs(f(x0)) > accuracy:
        iterations += 1
        x = g(x0, l)
        iteration(x, l)
    else:
        print("Корень: " + str("%.9f" % x0))
        print("Количество итераций: " + str(iterations))
        print("Проверка: f(x) = " + str("%.2e" % f(x0)) +
              " <= " + str(accuracy))


def k(x):
    return x - f(x) / diff_f(x)


def newton(x0):
    global iterations
    global accuracy

    if f(x0) != 0 and abs(f(x0)) > accuracy:
        iterations += 1
        x = k(x0)
        newton(x)
    else:
        print("Корень: " + str("%.9f" % x0))
        print("Количество итераций: " + str(iterations))
        print("Проверка: f(x) = " + str("%.2e" % f(x0)) +
              " <= " + str(accuracy))


def enter_values():
    while True:
        try:
            a = float(input("Введите левый промежуток: "))
            b = float(input("Введите правый промежуток: "))

            # Сделаем проверку, если ли корень на промежутке
            if f(a) * f(b) < 0:
                print("Кажется на промежутке [" + str(a) + ", " + str(b) + "] есть один или несколько корней.")
                break
            else:
                print("Кажется на введенном промежутке нет корня. Попробуйте еще раз..")

        except ValueError:
            print("Кажется с промежутком что-то не так. Попробуйте другой..")

    return a, b


if __name__ == "__main__":
    # TODO rename files
    ####################################################################################################################
    print("___________________________________________________________________________________________________________")
    print("Подготовительные действия:")
    ####################################################################################################################

    # нарисуем функцию
    draw(f, -10, 10, -100, 100, -10, 10)

    # введем промежуток
    a, b = enter_values()
    # a, b = -0.5, 0

    # за начальное приближение возьмем середину отрезка
    x0 = (a + b) / 2

    ####################################################################################################################
    print("___________________________________________________________________________________________________________")
    print("Метод деления пополам:")
    ####################################################################################################################
    try:
        iterations = 0
        bisection(a, b)
    except:
        print("Что-то пошло не так.. Возможно, на промежутке несколько корней.")
    ####################################################################################################################
    print("___________________________________________________________________________________________________________")
    print("Метод итераций:")
    ####################################################################################################################
    try:
        # нарисуем производную на промежутке [a, b]
        draw(diff_f, -25, 25, -25, 25, a, b)

        # найдем l = 1 / M = 1 / max|f'(x)| on [a, b]
        l = 1 / max_diff(a, b)

        iterations = 0
        iteration(x0, l)
    except:
        print("Что-то пошло не так.. Возможно, на промежутке несколько корней.")
    # ####################################################################################################################
    print("___________________________________________________________________________________________________________")
    print("Метод Ньютона:")
    # ####################################################################################################################
    try:
        iterations = 0
        newton(x0)
    except:
        print("Что-то пошло не так.. Возможно, на промежутке несколько корней.")
