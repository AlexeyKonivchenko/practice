# Задание 1 (индекс массы тела)

# Напишите программу, которая запрашивает у пользователя с клавиатуры его рост в сантиметрах, 
# его вес в килограммах (каждый показатель – с новой строки, в новом запросе) и выводит на экран сообщение вида:
#     Индекс массы тела: [значение].  
# где вместо `[значение]` подставляется посчитанное значение индекса массы тела. 


# height = int(input('Введите свой рост в сантиметрах: '))
# weight = int(input('Введите свой вес: '))

# index = weight/((height/100) * height/100)
# print(f'Индекс вашего тела равен {index} кг')




# задание 2 (питон)

# days = int(input('Введите число дней: '))
# mins = 1
# def minutes(days):
#     if days > 1:
#         mins += 3

# for i in range(days - 1):
#     mins += 3
# if days > 1:
#     print(f'За {days} дня(ей) ,питон принимал солнечные ванны {mins} минут')
# elif days < 1:
#     print('Некорректный ввод!')
# else:
#     print("Питон грелся только 1 минуту :'(")


# Задача 3 

# girls = ["Иветта", "Виолетта", "Кассандра", "Вирджиния", 
#          "Амелия", "Розамунда", "Янина", "Беатриса"]
# print(girls[1:5])
# print(girls[3:])
# print(girls[:2]+ girls[3:5])
# print(girls[2:3]+ girls[4:6])


# задача 4

# student = ('Иван Питонов', 2001, [8, 7, 7, 9, 6], True)
# name = student[0].split()
# print(f'студент: {name[1]}, {name[0]}')
# print(2020 - student[1])
# print(', '.join(str(i) for i in student[2]))
# print(sum(student[2])/ len(student[2]))
# if sum(student[2])/ len(student[2]) >=8:
#     print(True)
# else:
#     print(False)



# Задача 5
# example , points = [i for i in input().split()]
# points = int(points)
# summa = 0
# while example[0] != '0':
#     if example == 'б':
#         summa += points
#     elif example =='п':
#         summa += points * 1.5
#     elif example == 'с':
#         summa += points * 3
#     example = input().split()
#     if len(example) !=1:
#         points, example = int(example[1]), example[0],
# print(summa)


# Задача 6
# next = int(input())
# count = 0
# s = next(
# while next > 0:
#     next = int(input())
#     if next > s:
#         count +=1 
#     s = next
# print(count)

# Задача 7 

# s = input().split()
# m = 0
# for i  in s:
#     if len(i) > m:
#         m = len(i)
# print(m)

# Задача 8 

# stroka = [s.replace('"', '') for s in input().split()]
# a = ''
# for i in stroka:
#     a += i[0]

# print(f'"{a}"')