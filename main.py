import numpy as np
import iteration_direct
import iteration_reverse
import iteration_power
import hauseholder_method

if __name__ == '__main__':
    path_to_data = 'data.txt'
    # code that reads data from file and creates matrix A (numpy array) of floats

    with open(path_to_data, 'r') as f:
        A = np.array([list(map(float, line.split()))
                     for line in f.readlines()])
    print(A)

    epsilon = 0.0001
    # code that finds eigenvalues and eigenvectors of A
    # and prints them to stdout

    print('this is a simple iteration example')
    print(iteration_power.power_iteration(A, eps=epsilon))

    print('this is a direct iteration example')
    print(iteration_direct.direct_iteration(A, eps=epsilon))

    print('this is a reverse iteration example')
    print(iteration_reverse.reverse_iteration(A, eps=epsilon))

    print('this is a Hausholder method example')
    print(hauseholder_method.hauseholder_method(A, eps=epsilon))
