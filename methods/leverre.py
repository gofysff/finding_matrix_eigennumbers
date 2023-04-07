import numpy as np
import sympy as sp


def leverre(A):
    n = A.shape[0]  # размер матрицы
    B = A  # создаем дубликат для дальнейшего возведния в степень
    SpAk = np.zeros((n))  # создаем массив для Sp
    sum = 0
    for j in range(n):
        sum += A[j][j]
    SpAk[0] = sum  # первый элемент sp
    pk = np.zeros((n))  # создаем массив для pk
    pk[0] = SpAk[0]  # первый элемент pk
    # print(A)
    for i in range(1, n):
        A = np.matmul(A, B)  # умножение матриц
        sum = 0
        for j in range(n):
            sum += A[j][j]
        SpAk[i] = sum
        sum = 0
        for j in range(1, i+1):
            sum -= pk[j-1]*SpAk[i-j]
        print(sum)
        pk[i] = (SpAk[i]+sum)/(i+1)
    print(f'\n\np(leverrie) is {pk}\n\n')

    def func(x):  # функция для формирования функции
        result = (x**n)-pk[n-1]
        for i in range(1, n):
            result -= (x**(n-i))*pk[i-1]
        return result*((-1)**n)
    x = sp.Symbol('x')  # превращает символ в переменную
    result = sp.solvers.solve(func(x), x)  # функция для решения уравнений

    return result


if __name__ == '__main__':
    A = np.array(([5, 6, 3], [-1, 0, 1], [1, 2, -1]))
    print(leverre(A))
