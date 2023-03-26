import numpy as np


def leverre(A: np.array):
    n = A.shape[0]
    B = A
    SpAk = np.zeros((n))
    summa = 0
    for j in range(n):
        summa += A[j][j]
    SpAk[0] = summa
    pk = np.zeros((n))
    pk[0] = SpAk[0]
    print(A)
    for i in range(1, n):
        A = np.matmul(A, B)
        summa = 0
        for j in range(n):
            summa += A[j][j]
        SpAk[i] = summa
        summa = 0
        for j in range(1, i+1):
            summa -= pk[j-1]*SpAk[i-j]
        print(summa)
        pk[i] = (SpAk[i]+summa)/(i+1)
    print(A)
    print("\n", SpAk)
    print("\n", pk)


if __name__ == '__main__':

    A = np.array(([5, 6, 3], [-1, 0, 1], [1, 2, -1]))
    leverre(A)
