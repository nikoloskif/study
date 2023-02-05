'''All at once
Complete the above code so that it:
1. Replaced the second element of the list with 17
2. Added the numbers 4, 5 and 6 to the end of the list
3. Deleted the first item in the list
4. Doubled the list
5. Inserted the number 25 at index 3
6. Output a list using the print() function'''


numbers = [8, 9, 10, 11]
numbers[1] = 17
numbers.extend([4, 5, 6])
del numbers[0]
numbers *= 2
numbers.insert(3, 25)
print(numbers)
