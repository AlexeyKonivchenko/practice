# Задание №1

# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!

# Here's the deal:

# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.
# Examples
# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false



hashtags = input().split()
tag = '#'
if len(hashtags) < 140 and len(hashtags) != 0:
    for i in hashtags:
        tag += i.title()
    print(tag)
else:
    print(False)
   
# Реши через функцию
# def generate_hashtag(x):
# КОД ТУТ
# print(generate_hashtag(x))

#При решении через функцию:
# 1) Возвращай результат
# 2) Попробуй избавиться от else, согласно советам, которые я давал в прошлом комплекте задач
# Доп:
# 3) Попробуй сделать return через услоовие if-else в строку:
# ретурн Неправильно если условие иначе Хэштег
