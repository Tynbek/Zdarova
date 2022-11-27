
# lst = ['hello', 1234, True]               #Список
# numbers = [i+2 for i in range(1, 101)]      # Генератор списка
# print(numbers)
# print(lst[0]) #вывод по индексу
# print(lst[:2])  # вывод по индексам
# print(list('hello'))  # функция для создания списка

# words = ['hello', 'world', 'python']
# print(words[1][4])      # Обращение к символу элемента списка
# numbers = [1, 2, 3, 4]
# lst = [numbers, 5, 6, 7]
# # numbers.append(5)     #Метод, добавляет строго 1 элемент в конец указанного списка
# print(lst)

# numbers = [1, 2, 3, 4, 5]
# del numbers[0:2]                #Конструкция, удаление по индексу(срезу) безвозвратно
# print(numbers)

# numbers = [1, 2, 3, 4, 5]
# a = numbers.pop(2)     #Метод, вырезает и помещает в переменную, только по конкретному индексу
# print(numbers)
# print(a)

# numbers = [1, '2', 3, 4, '2', 3, 5]
# numbers.remove('2')             #Удаление по значению, удаляется именно первое значение
# print(numbers)

# numbers = [1, 2, 3, 4]
# print(2 in numbers)       #Проверка на вхождения и не вхождени
# print(5 in numbers)

# numbers = [1, 2, 3 ,4]
# numbers.append([5, 6, 7])     #Метод, добавляет строго 1 элемент в конец указанного списка
# print(numbers)

# numbers = [1, 2, 3, 4]
# numbers.insert(1, 'new element')    #Вставка по индексу строго 1-го элемента, но не удаляет элемент на который вставляем
# print(numbers)

# numbers = [1, 2, [3, 4]]
# numbers.extend([5, 6, 7]) #Добавялет как самостоятельные элементы в список, принимает строго коллекцию
# print(numbers)

# numbers = [1, 2, [3, 4]]
# numbers[-1].append(5)   #Обращение по индексу с заменой элемента
# numbers[2][0] = 'hello'
# print(numbers)

# numbers = [1, 2, 3]
# a = numbers.index(2) #Чтобы узнать индекс элемента в списке по его значению(ValueError сли нету)
# print(a)

# words = ['hello', 'python', 'hello', 1, 1, 2, 3]
# print(words.count('python')) #Подсчитывает количество конкретных элементов в списке(0, если нету)

# words = ['key', 'hello', 'hi', 'python']
# words.sort(key=len, reverse=True)   #Сортирует по лексико граф знач по умолч(reverse - в обратном порядке, key=len - сортируем по длине)
# sort_words = sorted(words, key=len, reverse=True) #Делает отсортированную копию списка, сам список остаётся без изменений
# print(words)
# print(sort_words)

# words = ['key', 'hello', 'hi', 'python']
# # rev_words = words[::-1]     #Разворот списка не изменив самого списка
# # print(words)
# # print(rev_words)
# words.reverse() #Разворачивает сам список
# print(words)

# words = ['key', 'hello', 'hi', 'python']
# words.clear()   #Удаляет все элементы и списка
# print(words)

# a = [1, 2, 3, 4]
# b = a  #Это не являетс копированием, у списка просто 2 ссылки теперь
# a.append(5)
# print(b)

        #Способы как именно скопировать список
#1 Поверностное копирование
# a = [1, 2, 3, 4]
# b = list(a)
# a.append(5)
# print(b)

#2 Поверностное копирование
# a = [1, 2, 3, 4]
# b = a[:]
# a.append(5)
# print(b)

# #3 Поверностное копирование
# a = [1, 2, 3, 4]
# b = a.copy()
# a.append(5)
# print(b)

# c = [5, 6]
# a = [1, 2, 3, 4, c]
# b = a.copy()
# a.append(5)
# a[4].append(7)  #Таким вот образом только вставится, т.к. список в списке хранится в виде ссылки
# print(a)
# print(b)


# a = [6, 7]
# numbers = (1, 2, 3, 4, 5, a) #Список в кортеже хранится в виде ссылки, следоват сам список изменяем
# a.append(8)
# print(numbers)

# letters = tuple('hello')  #Приведение к кортежу
# print(letters)

# number = [1, 2, 3, 4, 5]
# s = set(number) #Множество рандомно расставляет элементы
# print(s)

# s1 = {1, 2, 3, 4, 5}
# s2 = {5, 6, 7, 8}
# print(s1.isdisjoint(s2)) #Проверка на наличие общих элементов между 2-мя ножествами

# s1 = {1, 2, 3, 4, 5}
# s2 = {2, 3, 5}
# print(s2.issubset(s1)) #Проверка на подмножество
# print(s1.issuperset(s2))

# set1 = {1, 2, 3}
# set2 = {3, 2, 1}
# print(set1 == set2) #Сравнение множеств на одинаковые элементы


# some_set = {'hello', 'hi,', 'bye', 'goodbye'}
# some_set.add('privet') #Добавляет выбранный элемент рандомно в множество
# print(some_set)

# set1 = {'hello', 'hi,', 'bye', 'goodbye'}
# set1 = set1.remove('hi') #удаление, если нету  keyerror
# # set1 = set1.discard('hi')#удаление если есть
# # set1 = set1.pop('hi')#удаление
# print(set1)

# set1 = {1, 2, 3}
# set1.clear()    #удаляет все элементы множ
# print(set1)

# set1 = {1, 2, 3}
# set1.copy() #Копирует
# print(set1)

# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# s3 = {6, 7, 8, 4}
# s4 = s2.union(s1, s3) #Объединение всех 3 множ, без дубликатов
# s5 = s1 | s2 | s3   #Объединение всех 3 множ, без дубликатов
# print(s4)
# print(s5)

# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# s3 = {6, 7, 8, 4}
# s4 = s1.difference(s2, s3) #Находит уникальные элементы s1 по отношению к s2, s3
# s5 = s1 - s2 - s3 #Находит уникальные элементы s1 по отношению к s2, s3
# print(s4)
# print(s5)

# s1 = {1, 2, 3}
# s2 = {3, 4, 5, 2, 1}
# s3 = {6, 7, 8, 4, 1, 2}
# s4 = s1.intersection(s2, s3) #Общие во всех 3
# s5 = s1 & s2 & s3 #Общие во всех 3
# print(s4)
# print(s5)


# s1 = {1, 2, 3, 9}
# s2 = {3, 4, 5, 2, 1}
# s3 = {6, 7, 8, 4, 1, 2}
# s4 = s1.symmetric_difference(s2) # Элементы которые есть во всех трёх
# s5 = s1 ^ s2
# print(s4)
# print(s5)

# s1 = {1, 2, 3, 9}
# s2 = {3, 4, 5, 2, 1}
# s3 = {6, 7, 8, 4, 1, 2}
# s1.update(s2, s3) # s1 результат объединения всех 3-ех
# s1 |= s2 | s3
# print(s1)

# s1 = {1, 2, 3, 9}
# s2 = {3, 4, 5, 2, 1}
# s3 = {6, 7, 8, 4, 1, 2}
# s1.intersection_update(s2, s3) # Элементы которые есть во всех трёх
# s1 &= s2 & s3
# print(s1)

# s1 = {1, 2, 3, 9}
# s2 = {3, 4, 5, 2, 1}
# s3 = {6, 7, 8, 4, 1, 2}
# # s1.symmetric_difference_update(s2) # Элементы которые есть во всех трёх, но не являются общими
# s1 ^= s2
# print(s1)

# s1 = {1, 2, 3, 9}
# s2 = {3, 4, 5, 2, 1}
# s3 = {6, 7, 8, 4, 1, 2}
# s3 = frozenset(s3)  #Неизменное множество
# print(s1, s2, s3)

# user = {              #Словарь
#     'name': 'alex',
#     'city': 'Minsk',
#     'age': 26,
}
# user['age'] = 35 #Можно потом обратиться и поменять

# user['languages'] = ['ru', 'en'] #Обращаемся по несуществующему ключу, чтобы его объявить

# print(user['languages'][0]) #выводим первый элемент списка

# print(user.get('languages', 'ru')) #Метод позволяющий получить значение по ключу, по умолч None(поменял его на 'ru)

# print(user.setdefault('languages', 'ru')) #Объявит ключ 'languages' со значением 'ru'
# print(user)

# age = user.pop('age') # Удаляет ключ и вырезается в переменную age
#
# age = user.pop('languages', None) #Ошибку по умолчанию заменяет на None
# print(user)
# print(age)

# age = user.popitem() # Удаляет и возвращает пару ключ значение в виде кортежа в переменную age
# print(user)
# print(age)

# keys = user.keys() #Получаем список ключей в кортеже
# keys = list(user.keys()) #Таким образом можем получить полноценный список ключей
# print(keys)

# values = user.values() #Получаем список значений ключей в кортеже
# values = list(user.values()) #Таким образом можем получить полноценный список значений
# print(values)

# print(list(user)) #Любые действия как и итерация происходит по ключам

# items = user.items()  #Чтобы получить все пары ключ-значение
# items = list(user.items())  #Сделать самостоятельные пары ключ-значение
# print(items)

# data = [                                #Создание словарика через список(коллекция коллекций по 2 эл-та)
#     ('name', ['alex', 'pavel'])
# ]
# print(dict(data))

# user.update({'age': 35, 'language': 'ru'})  #Обновляем словарь элементами из другого словаря
# print(user)

# new_user = user | {'age': 35, 'language': 'ru'} #2 способ обновления словаря
# print(user)
# print(new_user)

# user['age'] = [user['age'], 35] #увеличение значений ключа
# print(user)

# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]
# numbers3 = numbers1 + numbers2
# numbers3 = sum(numbers1 + numbers2)
# print(numbers1)
# print(numbers2)
# print(numbers3)


