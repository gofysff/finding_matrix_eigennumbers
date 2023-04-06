
import numpy as np
import sympy as sp


def fadeev(A):
    n = A.shape[0]  # Размер матрицы
    # Создаем массив для элементов K - он будет считается как сумма главной диагонали
    k = np.zeros((n))
    k[0] = np.trace(A)
    E = np.eye(n)  # Создаем единичную матрицу
    B = A-k[0]*E

    for i in range(1, n):
        # Создали матрицу для хранения промежуточных вычислений
        A_tmp = np.dot(A, B)
        k[i] = (np.trace(A_tmp))/(i+1)
        B = A_tmp-k[i]*E

    def func(x):  # функция для формирования функции
        result = (x**n)-k[n-1]
        for i in range(1, n):
            result -= (x**(n-i))*k[i-1]
        return result*((-1)**n)
    x = sp.Symbol('x')  # превращает символ в переменную
    result = sp.solvers.solve(func(x), x)  # функция для решения уравнений
    return result


if __name__ == '__main__':

    A = np.array(([5, 6, 3], [-1, 0, 1], [1, 2, -1]))
    print(fadeev(A))
