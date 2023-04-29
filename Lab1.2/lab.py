from math import *
import matplotlib.pyplot as plt


def f(x: float) -> float:
    """
    Функция
    """
    return cos(x + pi / 4)


def derrivative(x, n):
    """
    Функция, вычисляющая n-ую производную функции
    """
    return cos(x + pi / 4 * (2 * n + 1))


def taylor_series(x: float, n: int) -> float:
    """
    Функция, вычисляющая ряд Тейлора
    """
    return sum(derrivative(0, i) * (x ** i) / factorial(i) for i in range(n + 1))


def graphic_picture():
    """
    Функция для построения графика
    Возвращает 5 картинок:
    - график функции
    - график первой производной
    - график второй производной
    - график третьей производной
    - все графики на одном графике
    """
    f_x = plt.figure(figsize=(10, 10))
    plt.grid()
    interval = 628
    x = [x / 100 for x in range(-interval, interval)]
    y = [f(x) for x in x]
    plt.plot(x, y)
    plt.title("График f(x)")
    plt.savefig('f(x).png')
    d_dx1 = plt.figure(figsize=(10, 10))
    plt.grid()
    plt.plot([x / 100 for x in range(-interval, interval)],
             [taylor_series(x / 100, 1) for x in range(-interval, interval)])
    plt.title("График до первого члена ряда Тейлора")
    plt.savefig('taylor1.png')
    d_dx2 = plt.figure(figsize=(10, 10))
    plt.grid()
    plt.plot([x / 100 for x in range(-interval, interval)],
             [taylor_series(x / 100, 2) for x in range(-interval, interval)])
    plt.title("График до второго члена ряда Тейлора")
    plt.savefig('taylor2.png')
    d_dx3 = plt.figure(figsize=(10, 10))
    plt.grid()
    plt.plot([x / 100 for x in range(-interval, interval)],
             [taylor_series(x / 100, 3) for x in range(-interval, interval)])
    plt.title("График до третьего члена ряда Тейлора")
    plt.savefig('taylor3.png')
    all = plt.figure(figsize=(10, 10))
    interval = 628
    plt.grid()
    plt.plot([x / 100 for x in range(-interval, interval)], [f(x / 100) for x in range(-interval, interval)])
    plt.plot([x / 100 for x in range(-interval, interval)],
             [taylor_series(x / 100, 1) for x in range(-interval, interval)])
    plt.plot([x / 100 for x in range(-interval, interval)],
             [taylor_series(x / 100, 2) for x in range(-interval, interval)])
    plt.plot([x / 100 for x in range(-interval, interval)],
             [taylor_series(x / 100, 3) for x in range(-interval, interval)])
    plt.title("График f(x) и первых трех членов ряда Тейлора")
    plt.savefig('all.png')


def check_workability(a, n, delta):
    """
    Функция, проверяющая погрешность ряда Тейлора
    """
    return f"taylor_series({a}, {n}) = {taylor_series(a, n)} f(a) = {f(a)}\ndelta = {taylor_series(a, n) - f(a)} \n{taylor_series(a, n) - f(a) < delta}\n"


if __name__ == '__main__':
    """
    Выполнение программы
    """
    graphic_picture()
    n1 = 2
    n2 = 3
    a = -0.05
    delta1 = 0.001
    delta2 = 0.000001
    print(check_workability(a, n1, delta1))
    print(check_workability(a, n2, delta2))
