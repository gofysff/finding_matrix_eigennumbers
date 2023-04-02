'''
1. Выбрать начальное приближение для собственного числа матрицы.
2. Решить систему (A - λ*I)x = b, где A - исходная матрица, λ - приближение
 к собственному числу, I - единичная матрица, b - некоторый начальный вектор.
3. Нормировать полученный вектор x.
4. Обновить приближение к собственному числу: λ_new = (x^T*A*x)/(x^T*x),
 где x^T - транспонированный вектор x.
5. Если разность между новым и старым приближениями к собственному числу меньше
 некоторого порога, то закончить процесс. Иначе вернуться к шагу 2.

'''

from typing import Tuple
import numpy as np


def reverse_iteration(A: np.ndarray, eps: float, max_iterations=10000) -> Tuple[float, np.ndarray]:
    n: int = A.shape[0]
    # Выбор начального приближения для собственных чисел
    x = np.random.rand(n)
    alpha = max(x, key=abs)
    for i in range(max_iterations):
        # x_new = A @ x / alpha
        x_new = np.linalg.solve(A, x/alpha)

        alpha_new = max(x_new, key=abs)
        # проверка на условие остановки
        if abs(alpha - alpha_new) < eps:
            break
        # обновление приближения
        x = x_new
        alpha = alpha_new

    return 1/alpha, x


if __name__ == "__main__":
    a = [[5, 6, -3],
         [-1, 0, 1],
         [1, 2, -1]]
    print("a = ", a)

    print(reverse_iteration(np.array(a), eps=0.001))
    print(reverse_iteration(np.array(a), eps=0.001))
