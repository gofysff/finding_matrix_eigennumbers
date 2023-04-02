import numpy as np
import sympy as sp


def find_roots(poly_coeffs):
    n = len(poly_coeffs)

    x = sp.Symbol('x')
    ans = x**n
    for i in range(n):
        ans -= poly_coeffs[n-1-i]*x**i
    return sp.solve((-1)**n*ans, x)

# ! возможно придется удалить


def leverrier(matrix) -> np.array:
    '''Leverrier's method for finding eigenvalues of a matrix'''
    n = len(matrix)

    indexes = [i + 1 for i in range(n)]

    matrix_powers = [np.linalg.matrix_power(matrix, i + 1) for i in range(n)]
    trace_values = [np.trace(matrix_powers[i]) for i in range(n)]
    poly_coeffs = np.array((0, 0, 0, 0, 0))
    for i in range(n):
        poly_coeffs[i] = trace_values[i]
        for j in range(i):
            poly_coeffs[i] -= trace_values[i - j - 1]*poly_coeffs[j]
        poly_coeffs[i] = poly_coeffs[i]/(i+1)
    print("Indices:\n", indexes)
    print("Matrix:\n", matrix_powers[4])
    print("Trace Values:\n", trace_values)
    print("Poly Coefficients:\n", poly_coeffs)
    roots = np.array([sp.N(i) for i in find_roots(poly_coeffs)])
    print("Eigenvalues:\n", roots)
    return roots


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
    print("leverrier")
    leverrier(A)
