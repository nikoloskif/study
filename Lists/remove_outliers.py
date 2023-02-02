'''Remove outliers.
When analyzing data collected as part of a scientific experiment,
it can be useful to remove the largest and smallest values.

The input to the program is a natural number n,
and then n different natural numbers.
Write a program that removes the smallest and
largest value from the specified numbers,
and then outputs the remaining numbers each on a separate line,
without changing their order.'''

'''При анализе данных, собранных в рамках научного эксперимента,
может быть полезно удалить самые большие и самые маленькие значения.

Входным сигналом для программы является натуральное число n,
а затем n различных натуральных чисел.
Напишите программу, которая удаляет наименьшее и
наибольшее значение из указанных чисел,
а затем выводит оставшиеся числа каждое в отдельной строке,
не меняя их порядок".'''


digit = int(input())
outlier = list()
for i in range(digit):
    digit1 = int(input())
    outlier.append(digit1)
del outlier[outlier.index(min(outlier))]
del outlier[outlier.index(max(outlier))]
print(*outlier, sep='\n')
