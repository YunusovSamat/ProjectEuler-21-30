"""
------------------------------- Задание -------------------------------
Используйте names.txt (щелкнуть правой кнопкой мыши и выбрать
'Save Link/Target As...'), текстовый файл размером 46 КБ, содержащий
более пяти тысяч имен. Начните с сортировки в алфавитном порядке. Затем
подсчитайте алфавитные значения каждого имени и умножьте это значение
на порядковый номер имени в отсортированном списке для получения
количества очков имени.

Например, если список отсортирован по алфавиту, имя COLIN
(алфавитное значение которого 3 + 15 + 12 + 9 + 14 = 53) является
938-ым в списке. Поэтому, имя COLIN получает 938 × 53 = 49714 очков.

Какова сумма очков имен в файле?
"""

import numpy as np


class TotalPoints:
    def __init__(self):
        self._names = np.array([])
        self._total_points = 0

    def read_file(self, path='p022_names.txt'):
        with open(path, 'r') as file:
            self._names = np.array(file.read().replace('\"', '').split(','))

    def sort_list(self):
        self._names.sort()

    def sum_alph_values(self, name):
        sum_values = 0
        for char in name:
            sum_values += ord(char) - 64
        return sum_values

    def set_total_points(self):
        for i in range(len(self._names)):
            self._total_points += i+1 * self.sum_alph_values(self._names[i])

    def get_total_points(self):
        return self._total_points

    def __str__(self):
        return str(self._total_points)
            

if __name__ == '__main__':
    points = TotalPoints()
    points.read_file()
    points.sort_list()
    points.set_total_points()
    print(__doc__)
    print('Ответ:', points)





