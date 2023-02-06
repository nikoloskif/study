'''Swap min and max
The input to the program is a string of text containing various natural numbers.
A list of numbers is formed from this string.
Write a program that swaps the minimum and maximum elements of this list.'''

'''На вход программе подается строка текста,
содержащая различные натуральные числа.
Из данной строки формируется список чисел.
Напишите программу, которая меняет местами минимальный и максимальный элемент этого списка.'''


text = input().split()
digits = list()
for i in text:
    digits.append(int(i))
x = digits.index(max(digits))
y = digits.index(min(digits))
digits[x], digits[y] = digits[y], digits[x]
print(*digits)
