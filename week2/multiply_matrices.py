def brute_force_matrix_mul(x, y):
    assert len(x[0]) == len(y)
    z = [[0 for _ in range(len(y[0]))] for _ in range(len(x))]
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(x[0])):
                z[i][j] += x[i][k] * y[k][j]
    return z

assert brute_force_matrix_mul([[1,2],[3,4]], [[1,2],[3,4]]) == [[7, 10], [15, 22]]
assert brute_force_matrix_mul([[1,2]], [[1,2],[3,4]]) == [[7, 10]]

def split_matrix(matrix):
    """
    split the input matrix to 4 quarters
    """
    length1 = len(matrix)
    length2 = len(matrix[0])
    matrix1, matrix2, matrix3, matrix4 = [[]], [[]], [[]], [[]]
    for i in range(length1):
        for j in range(length2):
            
    pass

def add_matrix(matrix1, matrix2):
    assert len(matrix1) == len(matrix2)
    assert len(matrix1[0]) == len(matrix2[0])
    result = list(matrix1)
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result

assert add_matrix([[1,2],[3,4]], [[1,2],[3,4]]) == [[2, 4], [6, 8]]
assert add_matrix([[1,2], [1,2]], [[1,2],[3,4]]) == [[2, 4], [4, 6]]

def strassen_subcubic_matrix_mul(x, y):
    pass
