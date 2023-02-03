一个matrix 3*3, 每个格子上有0或者1, 可以对为1的格子进行反转，

反转就是它以及它的上下左右0 -- > 1， 1 -- > 0， 

问：有没有一种方式，能够使所有的格子都为0；如果有，请写出反转顺序

def check_all_zeros(curr_matrix):
    if sum(curr_matrix) == 0:
        return True
    else:
        return False

def flip_matrix_elem(curr_matrix, index, i):

    return flip_matrix

def traverse(matrix, index, i):
    if i == len(index):
        return False
    matrix = flip_matrix_elem(matrix, index, i)
    if check_all_zeros(matrix) == 0:
        return True
    traverse(index, i + 1)


def function(matrix):
    index = []
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 1:
                index.append([i, j])
    traverse(matrix, index, 0)


