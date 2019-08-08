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
    print(points)





