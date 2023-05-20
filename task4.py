# Задание №4

# You are given an array (which will have a length of at least 3, but could be very large) containing integers.
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.

# ## Write a method that takes the array as an argument and returns this "outlier" N.

# Examples:
# ```
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)
# ```
# ```
# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)
# ```

def find_outlier(arr):
    num_even = 0
    num_odd = 0
    last_even = None
    last_odd = None

    for num in arr:
        if num % 2 == 0:
            num_even += 1
            last_even = num
        else:
            num_odd += 1
            last_odd = num

        if num_even > 0 and num_odd > 0:
            break

    return last_even if num_even == 1 else last_odd
print(find_outlier([int(i) for i in input().split()]))

# Интересная имплементация временных переменных last_even и last_odd. Прям навеяло одну из задач прошлого комплекта.
# Молодец!

# Также можно решить через словари:
def find_outlier(integers):
    evens = []
    odds = []
    even_counter = 0
    for integer in integers:
        if integer%2 == 0:
            evens.append(integer)
        else:
            odds.append(integer)
    if len(evens) > 1:
        return odds[0]
    return evens[0]
