'''Exactly_in_one
Write a function that takes two words word1 and word2
as arguments and returns True if the words have the same length and
differ in exactly 1 character and False otherwise.'''

'''Напишите функцию, которая принимает в качестве аргументов два слова word1 и word2
и возвращает значение True, если слова имеют одинаковую длину и отличаются
ровно в 1 символе и False в противном случае.'''

# function declaration
def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    if count == 1:
        return True
    else:
        return False

# reading the data
txt1 = input()
txt2 = input()

# calling the function
print(is_one_away(txt1, txt2))