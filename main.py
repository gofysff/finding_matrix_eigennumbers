import numpy as np
import methods.iteration_direct as iteration_direct
import methods.iteration_direct2 as iteration_direct2
import methods.iteration_reverse as iteration_reverse
import methods.iteration_power as iteration_power
import methods.hauseholder_method as hauseholder_method
import methods.leverre as leverre
import methods.fadeev as fadeev
import methods.danilevsky as danilevsky


if __name__ == '__main__':
    path_to_data = 'data2.txt'
    # code that reads data from file and creates matrix A (numpy array) of floats

    with open(path_to_data, 'r') as f:
        A = np.array([list(map(float, line.split()))
                     for line in f.readlines()])

    #  test 23 mathew data
    # A = np.array(data.matrixA)

    print('this is a matrix A')
    print(A)
    epsilon = 0.0001
    print('this is epsilon = ', epsilon, end='\n\n')

    print('this is a numpy eigenvalues')
    print(np.linalg.eigvals(A))

    # code that finds eigenvalues and eigenvectors of A
    # and prints them to stdout

    print('this is a leverre method example')
    print(leverre.leverre(A))
    print('\n\n')

    print('this is a fadeev method example')
    print(fadeev.fadeev(A))
    print('\n\n')

    print('this is a danilevsky method example')
    print(danilevsky.danilevsky(A))
    print('\n\n')

    print('this is a simple iteration example')
    print(iteration_power.power_iteration(A, eps=epsilon))
    print('\n\n')

    print('this is a direct iteration example')
    print(iteration_direct.direct_iteration(A, eps=epsilon))
    print('\n\n')

    print('this is a inverse iteration example')
    print(iteration_reverse.inverse_iteration(A, eps=epsilon))
    print('\n\n')

    print('this is a Hausholder method example')
    print(hauseholder_method.hauseholder_method(A, eps=epsilon))
