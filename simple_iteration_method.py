import numpy as np

# метод простых итераций, принимающий на вход квадратную матрицу A(np.array)
# Найти максимальное по модулю собственное число матрицы методом
# простой итерации с точностью eps=0.0001


def simple_iteration_method(A: np.array, eps=0.0001):
    # A  - это квадратная матрица
    n = A.shape[0]  # n - размерность матрицы
    x: list[np.array] = [np.ones(n)]  # вектор из единиц
    alpha: list[np.array] = []
    print("x[0] = ", x[0])
    # x[0] = np.ones((n))  # вектор из единиц
    while True:
        x.append(np.matmul(A, x[-1]))
        x[-1] = x[-1]/np.linalg.norm(x[-1])
        if np.linalg.norm(x[-1]-x[-2]) < eps:
            break

    # x[0] = np.ones((n)) # вектор из единиц


if __name__ == "__main__":
    a = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    print("a = ", a)
    simple_iteration_method(np.array(a))
