# Пользователь вводит Имя, Возраст и Город, сформировать
# приветственное сообщение путем форматирования 3-мя способам

#1 Способ
# name = input('Enter your name: ')                             #Не очень понимаю как это через конкатенацию провернуть
# age = input('Enter your age: ')                               # Ток так смог
# town = input('Enter your town: ')
# full_info = "Hello " + name + ' ' + 'you ' + age + ' ' + 'you are from ' + town
# print(input(full_info))

#2 Способ

name = input('Enter your name: ')                                       #Для чего тут нужно именовать? По типу
age = input('Enter your age: ')                                         #name=name и тд
town = input('Enter your town: ')

text = 'Hello {name}, you {age}, you are from {town}'.format(name=name, age=age, town=town)
print(text, end=' bye:)')

#3 Способ

# name = input('Enter your name: ')
# age = input('Enter your age: ')
# town = input('Enter your town: ')
# text = f'Hello {name}, you {age}, you are from {town}'
# print(text)
