import numpy as np
from typing import Tuple


'''
1. Начинается с выбора начального ненулевого вектора x0.
2. Выбирается матрица А.
3. Выбирается значение teta приближённого собственного числа.
4. Производится итерационный процесс, который заключается в последовательном применении оператора А
 к вектору x для получения нового вектора x_k+1 = A * x_k.
5. Полученный вектор нормируется, т.е. делят на его длину, x_k+1 = x_k+1 / x_k+1.
6. Вычисляют погрешность ε = x_k+1 - x_k.
7. Если погрешность ε меньше выбранной точности, то итерационный процесс останавливается и найденный 
вектор x_k+1 считается собственным вектором матрицы А, соответствующим приближённому собственному числу teta.
8. Для получения следующего приближения собственного вектора используется полученный вектор x_k+1 в качестве 
начального вектора и повторяется весь процесс, начиная с шага 4.
9. Повторения процесса продолжаются до тех пор, пока не будет достигнута требуемая точность.
'''


def power_iteration(A: np.array, eps: float, max_iterations=10000) -> Tuple[float, np.ndarray]:
    """method of power iteration

    Args:
        A (np.array): исходная матрица
        eps (float): точность вычисления
        max_iterations (int, optional): максимальное количество итераций. Defaults to 10000.

    Returns:
        Tuple[float, np.ndarray]: возвращает собственное значение и собственный вектор
    """
    n = A.shape[0]
    x = np.random.rand(n)
    x /= np.linalg.norm(x)

    a = 0
    for i in range(max_iterations):
        y = A @ x
        a_new = np.dot(x, y) / np.dot(x, x)

        x_new = y / np.linalg.norm(y)
        if np.abs(a_new - a) < eps:
            print(f"iteration {i}")
            break
        a = a_new
        x = x_new
    else:
        print("max iteration had been reached")

    return a_new, x


if __name__ == "__main__":
    a = [[5, 6, -3],
         [-1, 0, 1],
         [1, 2, -1]]
    print("a = ", a)
    print(power_iteration(np.array(a), eps=0.001))
