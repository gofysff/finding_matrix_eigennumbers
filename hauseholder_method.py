import numpy as np


def get_basis_vector(index: int, size: int) -> np.ndarray:
    """Возвращает базисный вектор размера size с единицей на позиции index"""
    vector = np.zeros(size)
    vector[index] = 1
    return vector


def hauseholder_method(A: np.array, eps: float) -> np.array:
    """Метод Хаусхолдера"""

    n: int = A.shape[0]
    R: np.array = A.copy()
    B: np.array = A.copy()
    Q: np.array = np.eye(n)
    for i in range(n-1):
        # Получаем вектор x
        x = np.copy(R)[:, i]
        # Обнуляем все элементы вектора x, кроме i-го
        for j in range(i):
            x[j] = 0
        # Получаем вектор u = x - ||x|| * e_i
        u = x - np.linalg.norm(x) * get_basis_vector(i, n)
        # Получаем матрицу P = I - 2uu^T/||u||^2 и умножаем ее на Q и R
        P = np.eye(n) - ((2 * u).reshape(n, 1) @ u.reshape(1, n)) / \
            (np.linalg.norm(u)**2)
        Q = Q @ P
        R = P @ R
        B = R @ Q
    # Проверяем, что все элементы на главной диагонали матрицы B не отличаются от элементов на главной
    #  диагонали матрицы A более, чем на eps и если да, то вызываем функцию hauseholder_method с матрицей B
    alpha = np.linalg.norm([B[i, i] - A[i, i] for i in range(n)])
    if alpha >= eps:
        return hauseholder_method(B, eps)
    return [B[i, i] for i in range(n)]
