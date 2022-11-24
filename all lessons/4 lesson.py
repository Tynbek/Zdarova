# lst = ['hello', 1234, True]               #Список
# numbers = [i+2 for i in range(1, 101)]      # Генератор списка
# print(numbers)
# print(lst[0]) #вывод по индексу
# print(lst[:2])  # вывод по индексам
# print(list('hello'))  # функция для создания списка

words = ['hello', 'world', 'python']
print(words[1][4])      # Обращение к символу элемента списка

# numbers = [1, 2, 3, 4]
# lst = [numbers, 5, 6, 7]
# numbers.append(5)     #Метод довления в конец
# print(lst)

# numbers = [1, 2, 3, 4, 5]
# del numbers[2]
# print(numbers)

# numbers = [1, 2, 3, 4, 5]
# a = numbers.pop(2)
# print(numbers)
# print(a)

# numbers = [1, '2', 3, 4, '2', 3, 5]
# numbers.remove('2')
# print(numbers)

# numbers = [1, 2, 3 ,4]
# numbers.append([5, 6, 7])
# print(numbers)
# numbers.insert(1, 'new element')
# print(numbers)

# numbers = [1, 2, [3, 4]]
# # numbers.extend([5, 6, 7])
# numbers[2].append(5)
# numbers[2][0] = 'hello'
# print(numbers)

# words = ['hello', 'python', 'hello']
# print(words.count('hello'))

# words = ['key', 'hello', 'hi', 'python']
# words.sort(key=len, reverse=True)
# sort_words = sorted(words, key=len, reverse=True)
# print(words)
# print(sort_words)
# words.reverse()
# print(words)
# rev_words = words[::-1]
# print(rev_words)
# c = [5, 6]
# a = [1, 2, 3, 4, c]
# b = a.copy()
# a.append(5)
# a[4].append(7)
# print(a)
# print(b)

# a = [6, 7]
# numbers = (1, 2, 3, 4, 5, a)
# a.append(8)
# print(numbers)

# letters = tuple('hello')
# print(letters)

# s1 = {1, 2, 3, 4, 5}
# s2 = {5, 6, 7, 8}
# print(s1.isdisjoint(s2))

# s1 = {1, 2, 3, 4, 5}
# s2 = {2, 3, 5}
# print(s2.issubset(s1))
# print(s1.issuperset(s2))

# some_set = {'hello', 'hi,', 'bye', 'goodbye'}
# some_set.add('privet')
# print(some_set)
# number = [1, 2, 3, 4, 5]
# s = set(number)
# print(s)

# number = {1, 2, 3, 4, 5}
# number = number.pop()
# print(number)

# s1 = {1, 2, 3, 8, 4}
# s2 = {3, 4, 5}
# s3 = {6, 7, 8, 4, 3}
# s3 = frozenset(s3)
# s3 = set(s3)
# print(s3)
# s1 &= s2 & s3
# s1.intersection_update(s2, s3)
# print(s1)
# s1 |= s2 | s3
# s1.update(s2, s3)
# print(s1 & s2 & s3)
# s4 = s1.difference(s2, s3)
# s5 = s1 - s2 - s3
# print(s4)
# print(s5)
# s4 = s2.union(s1, s3)
# s5 = s1 | s2 | s3
# print(s4)
# print(s5)
#
# user.update({'age': 35, 'language': 'ru'})
# print(user)
# print(user.setdefault('languages', 'ru'))
# print(user)
# age = user.pop('languages', None)
# print(user)
# print(age)
# age = user.popitem()
# print(user)
# print(age)
# keys = list(user.values())
# print(keys)
# print(list(user.items()))
# data = [
#     ('name', ['alex', 'pavel'])
# ]
# print(dict(data))
# user = {
#     'name': 'alex',
#     'city': 'Minsk',
#     'age': 26,
# }
# user['age'] = [user['age'], 35]
# print(user)
# new_user = user | {'age': 35, 'language': 'ru'}
# print(user)
# print(new_user)

# numbers1 = [1, 2, 3, 4]
# numbers2 = [4, 5, 6]
# numbers3 = sum(numbers1 + numbers2)
# print(numbers1)
# print(numbers2)
# print(numbers3)

