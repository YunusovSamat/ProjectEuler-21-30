"""
------------------------------- Задание -------------------------------
Единичная дробь имеет 1 в числителе. Десятичные представления единичных
дробей со знаменателями от 2 до 10 даны ниже:

1/2	=	0.5
1/3	=	0.(3)
1/4	=	0.25
1/5	=	0.2
1/6	=	0.1(6)
1/7	=	0.(142857)
1/8	=	0.125
1/9	=	0.(1)
1/10	=	0.1
Где 0.1(6) значит 0.166666..., и имеет повторяющуюся последовательность
из одной цифры. Заметим, что 1/7 имеет повторяющуюся последовательность
из 6 цифр.

Найдите значение d < 1000, для которого 1/d в десятичном виде содержит
самую длинную повторяющуюся последовательность цифр.
"""


def len_repeating_num(divider, number_of_decimal_places=1000):
    numerator = 1
    arr_mod = [numerator]
    for k in range(number_of_decimal_places):
        numerator *= 10
        while numerator < divider:
            numerator *= 10
            arr_mod.append(0)
        numerator %= divider
        if numerator in arr_mod:
            return len(arr_mod) - arr_mod.index(numerator)
        elif numerator == 0:
            break
        else:
            arr_mod.append(numerator)
    return 0


if __name__ == '__main__':
    len_repeat_max = 0
    d = 0
    for i in range(2, 1000):
        len_repeat_temp = len_repeating_num(i)
        if len_repeat_temp > len_repeat_max:
            len_repeat_max = len_repeat_temp
            d = i
    print(__doc__)
    print('Ответ:', d)


