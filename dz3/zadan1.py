a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def matrix(x):
    for i in range(len(x)):
        [print(x[k][i], end=' ') for k in range(len(x))]
        print()


matrix(a)