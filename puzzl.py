import numpy

mat = [[1, 4, 0, 3],
        [0, 0, 4, 0],
        [3, 0, 0, 0],
        [0, 0, 3, 2]]


def possible(row, column, number):
    global mat

    for i in range(0, 4):
        if mat[row][i] == number:
            return False

    for i in range(0, 4):
        if mat[i][column] == number:
            return False
#float divition
    x = (column // 2) * 2
    y = (row // 2) * 2
    for i in range(0, 2):
        for j in range(0, 2):
            if mat[y + i][x + j] == number:
                return False

    return True


def solve():
    global mat
    for row in range(0, 4):
        for column in range(0, 4):
            if mat[row][column] == 0:
                for number in range(1, 5):
                    if possible(row, column, number):
                        mat[row][column] = number
                        solve()
                        mat[row][column] = 0

                return

    print(numpy.matrix(mat))


solve()







