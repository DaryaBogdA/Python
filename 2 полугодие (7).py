import random
def exercise9_5_1():
    matrix = [
        [11, 12, 13, 14, 15],
        [21, 22, 23, 24, 25],
        [31, 32, 33, 34, 35],
        [41, 42, 43, 44, 45],
        [51, 52, 53, 54, 55],
    ]

    for i in range(len(matrix)):
        matrix[i][i] = 0
    print(matrix)

# exercise9_5_1()

def exercise9_7_1():
    matrix = [
        [11, 12, 13, 14, 15],
        [21, 22, 23, 24, 25],
        [31, 32, 33, 34, 35],
        [41, 42, 43, 44, 45],
        [51, 52, 53, 54, 55],
    ]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j and i + j != len(matrix) - 1: 
                matrix[i][j] = 0

    print(matrix)

# exercise9_7_1()

def exercise10_4_1(text):
    words = text.split()
    random.shuffle(words)
    print(" ".join(words))

# exercise10_4_1("Я ехала в китай на самолете через токио в пустыню опка")


def exercise10_4_3():
    num_1 = int(input("Введите первое число"))
    num_2 = int(input("Введите второе число"))
    while num_2:
        num_1, num_2 = num_2, num_1 % num_2
        result = num_1

    print(result)

# exercise10_4_3()