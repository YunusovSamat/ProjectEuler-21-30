import math

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

position = 1000000-1
answer = str()
factorials = list()
for i in range(len(numbers)):
    factorials.append(math.factorial(i))

for factorial in factorials[::-1]:
    index = position // factorial
    position = position % factorial
    answer += str(numbers[index])
    numbers.pop(index)

print(answer)
