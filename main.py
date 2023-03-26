import numpy as np
import iteration_direct
import iteration_reverse
import iteration_simple

if __name__ == '__main__':
    path_to_data = 'data.txt'
    # code that reads data from file and creates matrix A (numpy array) of floats

    with open(path_to_data, 'r') as f:
        A = np.array([list(map(float, line.split()))
                     for line in f.readlines()])
    print(A)

    # code that finds eigenvalues and eigenvectors of A
    # and prints them to stdout

    #!  метод простых итераций уходит в бесконечность на моих данных
    #! матрица с такими данными как в файле data.txt:

    # print('this is a simple iteration example')
    # print(iteration_simple.simple_iteration(A, eps=0.0001))
    print('this is a direct iteration example')
    print(iteration_direct.direct_iteration(A, eps=0.0001))
    print('this is a reverse iteration example')
    print(iteration_reverse.reverse_iteration(A, eps=0.0001))
