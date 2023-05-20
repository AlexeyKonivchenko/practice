# Задание №2

## Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.

# For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, 
# and occurs first in the string.

# As an added challenge, upper- and lowercase letters are considered the same character, 
# but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

# If a string contains all repeating characters, it should return an empty string ("") or None



def first_non_repeating_letter(a):
    b = [0] * len(a)
    c = None
    for i in range(len(a)):
        b[i] = a[i:i +1]
    for i in b:
        if (b.count(i.upper())) == 1 and (b.count(i.lower())) == 0 or (b.count(i.upper())) == 0 and (b.count(i.lower())) == 1:
            c = i
            break
    return c
print(first_non_repeating_letter(input()))

# Твое решение действительно работает
# Но давай попробуем сделать его короче
# Моё решение:
def first_non_repeating_letter(string):
    for i in list(string.lower()):
        if list(string.lower()).count(i) == 1:
            return list(string)[list(string.lower()).index(i)]
    return ''
# Проанализируй где ты можешь сократить свой код
# Как сказал мой ревьювер на курсах от Яндекс.Практикума:
# "мы же не индусы, которым платят за количество строк"
# Хотя, в случае Билли...
# ХПАХПАХАПХАПХАПХ
