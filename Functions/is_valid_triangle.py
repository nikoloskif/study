'''The is_valid_triangle
Write  function, which takes three natural numbers as arguments,
and returns True if there is a non-degenerate triangle
with sides side1, side2, side3 and False otherwise.'''

'''Напишите функцию, которая принимает в качестве аргументов
три натуральных числа и возвращает значение True,
если существует невырожденный треугольник со сторонами side1, side2,
side3 и False в противном случае.'''


def is_valid_triangle(side1, side2, side3):
    if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
        return True
    else:
        return False

a, b, c = int(input()), int(input()), int(input())

print(is_valid_triangle(a, b, c))
