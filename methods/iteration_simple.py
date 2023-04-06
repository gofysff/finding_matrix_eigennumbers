from ast import Tuple

import numpy as np


def simple_iteration(A: np.ndarray, epsilon: float) -> Tuple[float, np.ndarray]:
    """
    Метод простых итераций для вычисления приближенного собственного вектора и соответствующего ему собственного значения
    матрицы A

    :param A: квадратная матрица
    :type A: np.ndarray

    :param epsilon: точность вычисления
    :type epsilon: float

    :return: приближенный собственный вектор и собственное значение матрицы A
    :rtype: Tuple[np.ndarray, float]
    """
    n = A.shape[0]  # размерность матрицы А
    x = np.random.rand(n)  # начальный ненулевой вектор
    x /= np.linalg.norm(x)  # нормирование начального вектора

    while True:

        x_new = A @ x  # умножение матрицы А на текущий вектор x
        x_new /= np.linalg.norm(x_new)  # нормирование нового вектора
        epsilon_cur = np.linalg.norm(x_new - x)  # вычисление погрешности
        if epsilon_cur < epsilon:  # проверка достижения требуемой точности

            # возврат собственного значения и собственного вектора
            return x_new @ A @ x_new / (x_new @ x_new), x_new
        x = x_new  # обновление текущего вектора для следующей итерации
