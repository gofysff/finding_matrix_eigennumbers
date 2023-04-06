'''
Метод прямых итераций для поиска собственных чисел матрицы является одним из численных методов, 
используемых для нахождения собственных значений и собственных векторов матрицы.

Он основывается на идее последовательного применения оператора, который является переходом от
текущего приближения к следующему. Первоначально, выбирается некоторый вектор, который будет использоваться
в качестве начального приближения собственного вектора. Далее, на каждой итерации, этот вектор умножается на матрицу
и нормализуется, чтобы получить новый приближённый собственный вектор. Аналогичным образом определяется приближение
собственного числа, то есть отношение нормы нового вектора к норме предыдущего.

Формально, алгоритм метода прямых итераций выглядит следующим образом:

1. Выбирается начальный (ненулевой) вектор x(0) и выбирается допустимая погрешность eps.
2. На каждой итерации k вычисляются следующие значения:
   a. y(k) = A * x(k-1)
   b. lambda(k) = ||y(k)|| / ||x(k-1)||
   c. x(k) = y(k) / ||y(k)||
3. Если ||lambda(k) - lambda(k-1)|| < eps, то алгоритм останавливается. В противном случае, переходим к следующей итерации.

Здесь A — исходная матрица, ||x|| — норма вектора x. В итоге, метод прямых итераций сходится к максимальному собственному значению матрицы A, при условии, что оно является единственным по модулю. Если требуется нахождение нескольких собственных значений, метод может быть модифицирован, например, путём применения сдвига или отложенной итерации.'''


from typing import Tuple
import numpy as np


def direct_iteration(A: np.ndarray, eps: float) -> Tuple[float, np.ndarray]:
    """
    Метод прямых итераций для нахождения максимального по модулю собственного значения и соответствующего ему собственного вектора.

    :param A: исходная матрица размера (n, n)
    :param eps: допустимая погрешность
    :return: собственное значение и собственный вектор
    """
    n = A.shape[0]  # размерность матрицы
    x = np.random.rand(n)  # начальное приближение
    lambda_previous = 0  # предыдущее собственное значение

    # итерационный процесс
    while True:
        y = np.dot(A, x)  # умножаем на матрицу
        # находим новое собственное значение
        lambda_ = np.linalg.norm(y) / np.linalg.norm(x)
        x = y / np.linalg.norm(y)  # нормализуем вектор
        if abs(lambda_ - lambda_previous) < eps:  # проверка на достижение точности
            break
        lambda_previous = lambda_  # обновляем предыдущее значение

    return lambda_, x  # возвращаем найденные собственное значение и собственный вектор


if __name__ == "__main__":
    a = [[5, 6, -3],
         [-1, 0, 1],
         [1, 2, -1]]
    print("a = ", a)

    print(direct_iteration(np.array(a), eps=0.0001))
