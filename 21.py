class FriendlyNumbers:
    def __init__(self):
        self.prime_numbers = []
        self.set_prime_numbers(10000)

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


if __name__ == '__main__':
    friendly_numbers = FriendlyNumbers()
    sum_div_list = []
    for i in range(3, 10000):
        sum_div_list.append(sum(friendly_numbers.search_all_dividers(i)))
    print(sum_div_list)
