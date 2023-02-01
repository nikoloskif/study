'''Function value
The input to the program is a natural number n, and then n
integers. Write a program that for each entered number x
outputs the value of the function f(x) = x ** 2 + 2x + 1, on a separate line'''

'''Значение функции
На вход программе подается натуральное число n, а затем n
целых чисел. Напишите программу, которая для каждого введенного числа x
выводит значение функции f(x) = x ** 2 + 2x + 1, на отдельной строке'''



num = int(input())
numbers = list()
array = list()
for i in range(1, num + 1):
    num1 = int(input())
    numbers.append(num1)
    f = num1 ** 2 + 2 * num1 + 1
    array.append(f)
print(*numbers, sep='\n')
print()
print(*array, sep='\n')
