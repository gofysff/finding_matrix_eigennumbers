import numpy as np
import sympy as sp


def danilevsky(A):
    n = A.shape[0]
    for i in range(n-2, -1, -1):
        M = np.eye(n)
        for j in range(n):
            if (i != j):
                M[i][j] = (-A[i+1][j])/A[i+1][i]
            else:
                M[i][j] = 1/A[i+1][i]
        M_reverse = np.eye(n)
        for j in range(n):
            M_reverse[i][j] = A[i+1][j]
        A = np.matmul(M_reverse, np.matmul(A, M))

    res = np.zeros(n)
    for i in range((n)):
        res[i] = A[0][i]
    print(res)

    def func(x):  # функция для формирования функции
        result = (x**n)
        for i in range(1, n+1):
            result -= (x**(n-i))*res[i-1]
        print(result)
        return result
    x = sp.Symbol('x')  # превращает символ в переменную
    result = sp.solvers.solve(func(x), x)  # функция для решения уравнений
    return result


if __name__ == '__main__':

    # A=np.array([[2.2,1,0.5,2],[1,1.3,2,1],[0.5,2,0.5,1.6],[2,1,1.6,2]])
    A = np.array([[-5.496032, -4.153618, 11.60026057, 1.557029, -3.164633], [-2.225157, -0.193178, -19.97299538, -2.907853, 6.0289], [-3.626436, -6.880966, -
                                                                                                                                      6.903825654, -6.496388, -1.037427], [3.141419, 0.927751, 9.797346915, -1.489755, -2.778278], [-4.149118, -9.196849, 0.470804217, -8.367168, -7.911721]])
    print(danilevsky(A))
