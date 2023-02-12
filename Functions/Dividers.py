'''Dividers
The program accepts a natural number as input and
must return a list of all divisors of this number,
as well as the number of divisors.'''

'''Программа принимает на вход натуральное число и
должна возвратить список всех делителей данного числа,
а также количество делителей.'''

# declaring functions
def get_factors(num):
    return [i for i in range(1, num + 1) if num % i == 0]

def numbers_of_factors(num):
    return len(get_factors(num))

# reading the data
n = int(input())

# calling functions
print(*get_factors(n))
print(numbers_of_factors(n))
