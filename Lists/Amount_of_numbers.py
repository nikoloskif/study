'''Amount of numbers
The program receives two integers a and b (a≤b) as input.
Write a program that counts the number of numbers between a and b
inclusive whose cube ends in 4 or 9.'''

'''На вход программе подаются два целых числа a и b (a≤b).
Напишите программу, которая подсчитывает количество чисел в диапазоне от a до b
включительно, куб которых оканчивается на 4 или 9.'''


a, b = int(input()), int(input())
counter = 0
for i in range(a, b + 1):
    if (i ** 3) % 10 == 4 or (i ** 3) % 10 == 9:
        counter = counter + 1
print(counter)
