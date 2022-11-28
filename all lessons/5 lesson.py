# word = input('Vvedite: ')

# if word.isdigit():  #Оператор ветвления
#     word = int(word)
#     print('digit')
# elif word.isalpha():
#     print('word')
# elif word.isalnum():
#     print('letters and numbers')
# else:
#     print('Lox')

# numbers = [1, 2]
#
# if not numbers:
#     pass

# number = 4
# is_even = 'нечетное' if number % 2 else 'четное'  #Тернарный оператор
#
# if number % 2:    #Проверка на четность
#     is_even = False
# else:
#     is_even = True
# text = 'hello'
# res = 'слово' if text.isalpha else 'число' if text.isdigit() else 'не слово' #Тернарный оператор
# # if text.isalpha():
# #     res = 'слово'
# # else:
# #     res = 'не слово'
# print(res)

#Булева алгебра

# text = 'hello'
#
# if text.isalpha() or text.isalnum() and text.islower():
#     pass
# if text.isalpha() and text.isalnum():
#     pass


# x = True                #Оч клёвая задачка по таблице истинности
# y = False
# z = False
# if not x or y:
#     print(1)
# elif not x or not y and z:
#     print(2)
# elif not x or not y and z:
#     print(3)
# else:
#     print(4)

#Циклы

# for i in range(1, 10, 2):
#     i **= 2
#     print(i)

# numbers = [2, 5, 3, 5, 6, 9]

 #итерация по индексам(для строк, списков, кортежей)
# for i in range(len(numbers)):
#     print(numbers[1])

#итерация по элементам(для люой коллекции)
# for number in numbers:
#     print(number)

#итерация по упорядоченной коллекции(строка, список, кортеж)
# for i, val in enumerate(numbers): #Возвращает кортеж с 2-мя эл-ми(индекс, значение на этом индексе)
    # print(i, val)
    # print(f'на индексе: {i} значение: {val}')
    # print({i: val})

# По словарям

# data = {
#     'name': 'vasya',
#     'email': 'vasya@info.com'
#}

# for key in data: #Итерация по ключам
#     print(key)
# for key in data.values(): #По значению
#     print(key)
# for key, val in data.items(): #по ключам и значениям
#     print(key, val)

# numbers = [4, 6, 0, 3, 7, 4, 0]
# for number in numbers:
#     if not number:  #if number == 0
#         continue
#     number **= 2
#     print(number)

# numbers = [4, 6, 0, 3, 7, 4, 0]
# for i, number in enumerate(numbers):
#     if number == 0:
#         continue  #переходит сразу  к слдующей итерации
#     numbers[i] = number ** 2
#     print(numbers)

# numbers = [4, 6, 0, 3, 7, 4, 0]
# for i, number in enumerate(numbers):
#     if number == 0:
#         break   #прерывает выполнение цикла
#     numbers[i] = number ** 2
# else:
#     print('закончился самостоятельно')
# print(numbers)

# n = 100
# while n:
#     n -= 1
#     print(n)

# users = {
#     1: {
#         'name': 'name1',
#         'email': 'email1'
#     },
#
#     2: {
#                 'name': 'name2',
#                 'email': 'email2'
#     }
# }

# for _ in range(10):
#     print('hello world!')
#     print(_)


