"""
------------------------------- Задание -------------------------------
Начиная с числа 1 и двигаясь дальше вправо по часовой стрелке,
образуется следующая спираль 5 на 5:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

Можно убедиться, что сумма чисел в диагоналях равна 101.
Какова сумма чисел в диагоналях спирали 1001 на 1001, образованной
таким же способом?
"""


def print_table(n=7):
    table = [[0 for j in range(n)] for i in range(n)]
    i, j = 0, n - 1
    num = n ** 2
    while table[i][j] == 0:
        while (j >= 0) and (table[i][j] == 0):
            table[i][j] = num
            num -= 1
            j -= 1
        i += 1
        j += 1
        while (i < n) and (table[i][j] == 0):
            table[i][j] = num
            num -= 1
            i += 1
        i -= 1
        j += 1
        while (j < n) and (table[i][j] == 0):
            table[i][j] = num
            num -= 1
            j += 1
        i -= 1
        j -= 1
        while table[i][j] == 0:
            table[i][j] = num
            num -= 1
            i -= 1
        i += 1
        j -= 1

    for i in range(len(table)):
        for j in range(len(table[i])):
            print('{0:^3}'.format(table[i][j]), end='')
        print()


def sum_diagonals(table_len):
    num = 1
    summa = num
    gap = 2
    for i in range(int((table_len - 1) / 2)):
        for j in range(4):
            num += gap
            summa += num
        gap += 2
    return summa


if __name__ == '__main__':
    print(sum_diagonals(1001))
