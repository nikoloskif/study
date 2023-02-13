'''Find all
Write a function that takes two arguments: a string and a character and
returns a list containing all the locations of that character in the string.'''

'''Напишите функцию, которая принимает два аргумента: строку и символ и
возвращает список, содержащий все местоположения этого символа в строке.'''


# function declaration
def find_all(target, symbol):
    return [i for i in range(len(target)) if symbol in target[i]]

# reading the data
s = input()
char = input()

# calling the function
print(find_all(s, char))
