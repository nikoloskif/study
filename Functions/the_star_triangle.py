'''The Star Triangle
Write the function draw_triangle(full, base), which takes two parameters:
fill – placeholder character;
base – the value of the base of the isosceles triangle, and then outputs it.
It is guaranteed that the base of the triangle is an odd number.'''

'''Напишите функцию draw_triangle(full, base), которая принимает два параметра:
fill – символ заполнитель;
base – величина основания равнобедренного треугольника, а затем выводит его.
Гарантируется, что основание треугольника – нечетное число.'''


# function declaration
def draw_triangle(fill, base):
    seredina = base // 2 + 1
    count = 0
    for i in range(1, base + 1):
        if i > seredina:
            count -= 1
        else:
            count += 1
        for _ in range(count):
            print(fill, end='')
        print()

# reading the data
fill = input()
base = int(input())

# calling the function
draw_triangle(fill, base)
