# Задание №3

## Make a function so that it splits the string into pairs of two characters.

# If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

# Examples:

# ```
# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']
# ```

# Given an array of integers, return a new array with each value doubled.

## For example:
# ```
# [1, 2, 3] --> [2, 4, 6]
# ```

# Цель - решить в одну строку.

# Подсказка: см. "if else в одну строку"




# A
def function(string):
    a = []
    b = len(string)
    for i in range(0, b, 2):
        if i + 1 < b:
            a.append(string[i:i + 2])
        else:
            a.append(string[i] + '_')
    return a
print(function(input()))


# B

print([int(i) * 2 for i in input().split()])