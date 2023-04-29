import numpy as np
import matplotlib.pyplot as plt

f = lambda x: np.sin(2 * x) ** 2
a, b = [0, 2 * np.pi]
n = 10

# MODE = "SHOW"
MODE = "SAVE"


def plot_integral(f, a, b, n, method='left'):
    """
    @param f: функция, которую нужно интегрировать
    @param a: левая граница отрезка
    @param b: правая граница отрезка
    @param n: число разбиений
    @param method: метод, который нужно использовать
    @return I: значение интегральной суммы
    Вычисляет интегральную сумму функции f на отрезке [a, b]
    при заданном числе n разбиений
    с помощью одного из методов(left, right, midpoint, random, trapezoidal).
    Строит график функции f на отрезке [a, b] и добавляет на этот график прямоугольники, которые
    соответствуют выбранной интегральной сумме."""
    # добавляем график функции
    x = np.linspace(a, b, 1000)
    y = f(x)
    plt.plot(x, y)
    plt.gcf().set_size_inches(15, 9)
    length_of_segment = (b - a) / n
    x_points = np.linspace(a, b, n + 1)
    if method == 'left':
        x_points = x_points[:-1]
        y_points = f(x_points)
        for i in range(n):
            rect = plt.Rectangle((x_points[i], 0), length_of_segment, y_points[i], facecolor='blue', alpha=0.3)
            plt.gca().add_patch(rect)
    elif method == 'right':
        x_points = x_points[1:]
        y_points = f(x_points)
        for i in range(n):
            rect = plt.Rectangle((x_points[i] - length_of_segment, 0), length_of_segment, y_points[i], facecolor='blue',
                                 alpha=0.3)
            plt.gca().add_patch(rect)
    elif method == 'midpoint':
        x_points = x_points[:-1] + length_of_segment / 2
        y_points = f(x_points)
        for i in range(n):
            rect = plt.Rectangle((x_points[i] - length_of_segment / 2, 0), length_of_segment, y_points[i],
                                 facecolor='blue', alpha=0.3)
            plt.gca().add_patch(rect)
    elif method == 'random':
        xx_points = x_points[:-1] + np.random.uniform(0, length_of_segment, size=n)
        x_points = x_points[:-1] + length_of_segment / 2
        y_points = f(xx_points)
        for i in range(n):
            rect = plt.Rectangle((x_points[i] - length_of_segment, 0), length_of_segment, y_points[i], facecolor='blue',
                                 alpha=0.3)
            plt.gca().add_patch(rect)
    elif method == 'trapezoidal':
        x_points = np.linspace(a, b, n + 1)
        y_points = f(x_points)
        for i in range(n):
            plt.plot([x_points[i], x_points[i + 1]], [y_points[i], y_points[i + 1]], 'b-', lw=2)
        plt.fill_between(x_points, y_points, alpha=0.3)
    else:
        raise ValueError(f'Unknown method: {method}')
    if method != 'trapezoidal':
        I = np.sum(y_points) * length_of_segment
        plt.title(f'The way of selecting equipment: {method}; Partitioning into {n} parts; I = {I:.16f}')
    else:
        I = np.sum((y_points[1:] + y_points[:-1]) * length_of_segment / 2)
        plt.title(f'Trapezoidal rule; Partitioning into {n} parts; I = {I:.16f}')
    plt.xlabel('x')
    plt.ylabel('y')
    if MODE == "SAVE":
        plt.savefig(f"{n}_{method}.png")
    if MODE == "SHOW":
        plt.show()
    plt.close()
    return I


def compare_with_pi(x):
    return x - np.pi


def pretty_print(x):
    return f'{x:.16f} {compare_with_pi(x)}'


def main():
    print(f"{np.pi:.16f}")
    print(f"Integral of (sin(2x))^2 from {a} to {b} with {n} segments using different methods:")
    for method in ['left', 'right', 'midpoint', 'random', 'trapezoidal']:
        I = plot_integral(f, a, b, n, method=method)
        print(f'{method}: {I:.16f} {compare_with_pi(I):.16f}')


def create_a_table_row_for_latex(methods, ns):
    # Выбор оснащения & Левое & Среднее & Правое & Случайное & Трапециальное\\
    #  \hline
    #  n = 10 & 3.141593 & 3.141593 & 3.141593 & 3.207766 & 3.141593\\
    for n in ns:
        methods_results = []
        for method in methods:
            I = plot_integral(f, a, b, n, method=method)
            comparing_with_pi = I - np.pi
            methods_results.append(f'{I:.16f}')
            print(f'{n} & {method} & {I:.16f} & {comparing_with_pi:.16f} \\\\')
        print(f'n = {n} & {" & ".join(methods_results)} \\\\')
    # return f'{method} & {n} & {I:.16f} & {compare_with_pi:.16f} \\\\'


if __name__ == '__main__':
    # main()
    print(f"{np.pi:.20f}")
    needed_methods = ['left', 'midpoint', 'right', 'random', 'trapezoidal']
    all_ns = [25, 50, 100, 1000]
    # all_ns = [10]
    create_a_table_row_for_latex(needed_methods, all_ns)
    # 3.14159265358979311600
    # 3.1415926535897936