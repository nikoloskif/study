'''Sums of two
The input to the program is a natural number n ≥2, and then n integers.
Write a program that creates a list of the specified numbers consisting
of sums of neighboring numbers.'''

'''На вход программе подается натуральное число n≥2, а затем n целых чисел.
Напишите программу, которая создает из указанных чисел список,
состоящий из сумм соседних чисел.'''


num = int(input())
lists1 = list()
lists2 = list()
for i in range(num):
    digit = int(input())
    lists1.append(digit)
for j in range(len(lists1) - 1):
    lists2.append(lists1[j] + lists1[j + 1])
print(lists2)
