from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        i = len(self.matrix[0])
        for j in self.matrix:
            if len(j) != i:
                raise ValueError('fail initialization matrix')
    
    def __str__(self):
        result = ''
        for item in self.matrix:
            result += f'| {" ".join(map(str, item))} |\n'
        return result.rstrip('\n')
    
    def __add__(self, other):
        sum_matrix = []
        tmp = []
        for i in range(len(self.matrix)):
            for vol_1, vol_2 in zip(self.matrix[i], other.matrix[i]):
                tmp.append(vol_1 + vol_2)
            sum_matrix.append(tmp)
            tmp = []
        result = ''
        for item in sum_matrix:
            result += f'| {" ".join(map(str, item))} |\n'
        return result.rstrip('\n')


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """
