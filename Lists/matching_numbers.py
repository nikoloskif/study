'''Matching numbers
The input to the program is a string of text containing natural numbers.
A list of numbers is formed from this string.
Write a program that calculates how many pairs of elements equal
to each other in the resulting list. It is assumed that any two elements equal
to each other form one pair, which must be counted.'''

'''На вход программе подается строка текста,
содержащая натуральные числа. Из данной строки формируется список чисел.
Напишите программу, которая подсчитывает, сколько в полученном списке пар элементов,
равных друг другу. Считается, что любые два элемента,
равные друг другу образуют одну пару, которую необходимо посчитать.'''


text = input().split()
count = 0
for i in range(len(text)):
    for j in range(i + 1, len(text)):
        if text[i] == text[j]:
            count += 1
print(count)
