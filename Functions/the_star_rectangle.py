'''The star rectangle
Write a draw_box() function that draws a 16x12 star box, as per the pattern.'''

'''Напишите функцию draw_box(), которая выводит звездный прямоугольник
с размерами 16 на 12 в соответствии с образцом'''


# function declaration
def draw_box():
    for i in range(1, 17):
        if i == 1 or i == 16:
            print('*' * 12)
        else:
            print('*' + ' ' * 10 + '*')

# main program
draw_box()  # function call
