import random
import pandas as pd
import matplotlib.pyplot as plt


class Sort:
    def __init__(self):
        self.iter_binary = 0
        self.iter_sequential = 0
        self.elements = [3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56]
        self.df = pd.DataFrame(columns=['length', 'iter_binary', 'iter_sequential'])
        pass

    def selection_sort(self, nums):
        print(f'Before {nums}')
        for i in range(len(nums)):
            lowest_value_index = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[lowest_value_index]:
                    lowest_value_index = j

            nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
        print(f'After {nums}')

    def sequential(self, x):
        iterations = 0
        for iterations, element in enumerate(self.elements):
            if element == x:
                break
        self.iter_sequential = iterations
        return iterations, len(self.elements)

    def binary(self, x):
        elements_copy = self.elements.copy()
        elements_copy.sort()
        while len(elements_copy) > 1:
            index = int(len(elements_copy) / 2)
            if elements_copy[index] == x:
                break
            elif elements_copy[index] > x:
                elements_copy = elements_copy[:index]
            elif elements_copy[index] < x:
                elements_copy = elements_copy[index:]
            self.iter_binary += 1

    def analisis_big_o(self):
        for i in range(1000):
            for _ in range(100):
                self.elements.append(random.randint(0, 1000))
            x = int(len(self.elements) * 0.75)
            self.binary(x)
            self.sequential(x)
            data = dict(length=[len(self.elements)],
                        iter_binary=[self.iter_binary],
                        iter_sequential=[self.iter_sequential])

            self.df = self.df.append(pd.DataFrame(data, index=None), ignore_index=True)
        print(self.df)
        self.plot_analisis_big_o(self.df)

    def plot_analisis_big_o(self, df):
        df.plot(kind='line', x='length', y=['iter_binary', 'iter_sequential'],
                figsize=(6, 4),
                title='Nº de procesos',
                xlabel='length', ylabel='nº procesos',
                fontsize=10, rot=0)
        plt.savefig('plot_num_procesos.jpg')


if __name__ == '__main__':
    s = Sort()
    s.analisis_big_o()
    s.selection_sort([3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56])
    s.binary(875)
    s.sequential(875)
