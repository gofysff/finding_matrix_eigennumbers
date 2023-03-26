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


if __name__ == "__main__":
    a = [[5, 6, -3],
         [-1, 0, 1],
         [1, 2, -1]]
    print("a = ", a)

    print(simple_iteration(np.array(a), epsilon=0.001))
