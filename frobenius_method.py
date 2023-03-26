import numpy as np


# метод Фаддеева, принимающий на вход квадратную матрицу A(np.array)
# И находящий собственнные числа, собственные векторы и обратную матрицу
# методом Фаддеева, а также делающий проверку для обратной матрицы
def frobenius_method(A: np.array):

    #! НЕ УВЕРЕН, ЧТО РАБОТАЕТ
    #!  НЕ ТЕСТИЛ
    # A  - это квадратная матрица
    n = A.shape[0]  # n - размерность матрицы
    # B - это квадратная матрица, которая будет использоваться для вычисления
    # следующей степени матрицы A
    # A_current - это квадратная матрица, которая будет использоваться для вычисления A_
    A_current = A.copy()
    # SpAi - это вектор, который будет содержать значения следов матриц A_i
    # след - это сумма элементов на главной диагонали
    SpAk = np.zeros((n))
    summa = 0
    for j in range(n):
        summa += A_current[j][j]
    SpAk[0] = summa
    # np.eye(n) - единичная матрица размера n
    B_current = A_current-np.eye(n)*SpAk[0]

    for i in range(1, n):
        A_current = np.matmul(A_current, A)  # np.matm
        summa = 0
        for j in range(n):
            summa += A_current[j][j]
        SpAk[i-1] = summa
        B_current = np.matmul(B_current, A)-np.eye(n)*SpAk[i-1]
