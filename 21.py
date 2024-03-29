"""
------------------------------- Задание -------------------------------
Пусть d(n) определяется как сумма делителей n (числа меньше n,
делящие n нацело).
Если d(a) = b и d(b) = a, где a ≠ b, то a и b называются дружественной
парой, а каждое из чисел a и b - дружественным числом.

Например, делителями числа 220 являются 1, 2, 4, 5, 10, 11, 20, 22, 44,
55 и 110, поэтому d(220) = 284. Делители 284 - 1, 2, 4, 71, 142,
поэтому d(284) = 220.

Подсчитайте сумму всех дружественных чисел меньше 10000.
"""


class AmicableNumbers:
    def __init__(self):
        self.prime_numbers = []
        self.set_prime_numbers(10000)
        self.sum_div_list = [0, 0, 0]

    def set_prime_numbers(self, n):
        self.prime_numbers = list(range(3, n, 2))
        length = len(self.prime_numbers)
        for i, x in enumerate(self.prime_numbers):
            if x == 0:
                continue
            for j in range(i+x, length, x):
                self.prime_numbers[j] = 0
        self.prime_numbers = list(filter(None, self.prime_numbers))
        self.prime_numbers.insert(0, 2)

    def search_all_dividers(self, n):
        def enumeration_dividers(arr, a=1):
            a *= arr[0]
            div_sets.add(a)
            div_sets.add(n // a)
            for i in range(1, len(arr)):
                enumeration_dividers(arr[i:], a)

        prime_arr = []
        temp_n = n
        for b in self.prime_numbers:
            while temp_n % b == 0:
                prime_arr.append(b)
                temp_n = temp_n // b
            if temp_n == 1:
                break
        div_sets = set()
        enumeration_dividers(prime_arr)
        return div_sets - {n}

    def set_sum_div_list(self):
        for i in range(3, 10000):
            sum_div = sum(self.search_all_dividers(i))
            if sum_div != 1 and 10000 >= sum_div != i:
                self.sum_div_list.append(
                    sum(amicable_numbers.search_all_dividers(i)))
            else:
                self.sum_div_list.append(0)

    def get_sum_amicable_numbers(self):
        sum_amicable_numbers = 0
        for i in range(3, 10000):
            if self.sum_div_list[i] != 0:
                if self.sum_div_list[self.sum_div_list[i]] == i:
                    sum_amicable_numbers += i + self.sum_div_list[i]
                    self.sum_div_list[self.sum_div_list[i]] = 0
                    self.sum_div_list[i] = 0
        return sum_amicable_numbers


if __name__ == '__main__':
    amicable_numbers = AmicableNumbers()
    amicable_numbers.set_sum_div_list()
    print(__doc__)
    print('Ответ:', amicable_numbers.get_sum_amicable_numbers())
