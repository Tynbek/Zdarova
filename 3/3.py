# Пользователь вводит Имя, Возраст и Город, сформировать
# приветственное сообщение путем форматирования 3-мя способам

#1 Способ
# name = input('Enter your name: ')                         #Не очень понимаю как это через конкатенацию провернуть
# age = input('Enter your age: ')                           # Ток так смог
# town = input('Enter your town: ')
# greeting = 'HELLO! '
# full = greeting + name + ' ' + age + ' ' + town
# print(input(full))

#2 Способ

# name = input('Enter your name: ')
# age = input('Enter your age: ')
# town = input('Enter your town: ')
#
# text = 'Hello {}, age {}, town {}'.format(name, age, town)
# print(text, end=' bye:)')

#3 Способ

# name = input('Enter your name: ')
# age = input('Enter your age: ')
# town = input('Enter your town: ')
#
# text = f'Hello {name}, age {age}, town {town}'
# print(text)
