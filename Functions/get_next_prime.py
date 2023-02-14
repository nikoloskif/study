'''Next Prime
Write a function that takes a natural number
as an argument and returns the first prime number
greater than the entered number'''

'''Напишите функцию, которая принимает
в качестве аргумента натуральное число
и возвращает первое простое число большее введенного числа'''

# function declaration
def get_next_prime(num):
    num += 1
    for i in range(2, num):
        if num % i == 0:
            return get_next_prime(num)
    return num

# reading the data
n = int(input())

# calling the function
print(get_next_prime(n))
