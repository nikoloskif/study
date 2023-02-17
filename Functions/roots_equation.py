'''The roots of the equation
Write a function that takes as arguments three integers a, b, c –
the coefficients of the quadratic equation a(x**2) + bx + c = 0
and returns its roots in ascending order.'''

'''Напишите функцию, которая принимает в качестве аргументов
три целых числа a, b, c – коэффициенты квадратного уравнения
a(x**2) + bx + c = 0 и возвращает его корни в порядке возрастания.'''


# function declaration
def solve(a, b, c):
    from math import sqrt
    d = b ** 2 - 4 * a * c
    x1 = (-b - d ** 0.5) / (2 * a)
    x2 = (-b + d ** 0.5) / (2 * a)
    return min(x1, x2), max(x1, x2)

# reading the data
a, b, c = int(input()), int(input()), int(input())

# calling the function
x1, x2 = solve(a, b, c)
print(x1, x2)