# first_name = 'alex'
# age, city = 42, 'Minsk'                                                   #Обьявлениме 2-ух переменных
# print(first_name, age, city, end=' конец строки ', sep='---')          # необязательыне аргументы принта: end(то чем закончится принт, по умолчанию  там \n и sep(разделитель по умолчанию пробел, смысл указывать только если мин 2 значения указано)
# print(city)                                                                #Функция принт


# l_name = input('Enter last name: ')                   #Ввод данных с клавиатуры
# print(True+True)

# age = input('enter age: ')
# age = int(age)                                        #Приведение к инту(отбрасывает дробную часть, строки можем приводить к инту но только если из цифр)
# print(age)
#
# googol = 1_000_000_000_000_000
# print(googol)

# a = 2
# b = 3
# a += b                                              #Оператор обновления
# a /= b
# print(a)

# a = 5
# b = 2
# a = a == b
# print(a)

# a = 3.565454545
# a = round(a, 3)                               #Фунция round для округления с указанной точностью(нечетные окргуляет вверх, четные вниз)
# print(a)
# a = 23.56
# b = 24.56
# print(round(a))
# print(round(b))
# a = '3.45'
# a = float(a)                                  # приводит к дробному
# print(a)


# a = 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1
# print(round(a))

# a = -5
# a = abs(a)                                       # Модуль, откидывает минус
# print(a)

# a = 2.0
# print(a.is_integer())                            # Метод для дробных чисел, проверяет целое ли оно число, True или False

# text = 'helloworld'
# print(text)

# a = 2.0
# a = 5.454
# a = str(True)
# print(a)

# print('hello\'world')

# f_name = 'Morgan'
# l_name = ' Freeman'
# full_name = f_name + ' ' + l_name
# print(full_name)

# f_name = 'Morgan'
# print((f_name + ' ') * 3)             #Правильный порядок, математика

# text = 'hello world'
# symbol = text[::-1]                     #Срезы(слево направо с 0 отсчёт, последний не учитывается)
# print(symbol)

# text = 'qwerty'
# print(text[:3] + text[3:])

# text = 'hello world'
# a = len(text)
# print(a)
# text = r'hello\nworld'
# print(text)
# name = 'Alex'
# age = 35
                                                                #Форматирование строк
# text = 'Hello %s, age %d' % (name, age)                       # по процентам
# text2 = 'Hello {name}, age {age}'.format(name=name, age=age)  # формат(крайняк)
# text3 = f'Hello {name}, age {age}'                            # эфкой(мастхэв)
# print(text)
# print(text2)
# print(text3)

# text = 'hello world python pycharm'
# words = text.split(' ', maxsplit=1)                               # Метод split делит строку на список строк по указанному разделителю(есть дополнительный не обязательный аргумент maxsplit - количество разбиений)
# text2 = '.-.-'.join(words)                                      # Объединение списка строк с указанным разделителем, обратное split
# print(words)
# print(text2)

# text = 'hello python hello world python'
# a = text.find('python', 7, 12)                      #Метод, находит индекс и указывает первое значение, можно указать диапазон( если не найдёт выдаст -1)
# b = text.rfind('python', 0, 20)                   # Поиск с конца, а не с начала как у find
# a = text.index('python')                          #Метод в отличие от find, вместо -1(если не найдет) выдает ошибку ValueError
# b = text.rindex('python')                         #Метод в отличие от rfind, вместо -1(если не найдет) выдает ошибку ValueError
# print(text.count('Python'))                       #Метод, указывает количество вхождений подстроки в строку, можно указать диапазон
# print(text.count(' ')+1)    # Указывает количество слов в предложении
# print(a)
# print(b)

# text = 'hello python world python pycharm'
# print(text.partition('python'))                     #Метод Разбиение через первый шаблон в виде кортежа
# print(text.rpartition('python'))                  #Метод Разбиение по последнему шаблону

# text = 'hello java java, java'
# # text = text.replace('java', 'python', 2)          #Метод Замена чего-то на что-то, можно просто удалить(заменить на пустую строку)
# print(text.isdigit()) # только из цифр
# print(text.isalpha()) # только из букв
# print(text.isalnum()) # только из цифр и/или букв
# print(text.isidentifier()) # могла ли бы она быть именем переменной
# print(text.isspace()) # из пробелов и табуляций

# text = 'Hello Python'
# print(text.startswith('Hell'))  # првоерка начинается ли на это строка
# print(text.endswith('hon'))     # на то что заканчивается на укзанную подстроку

# text = 'HELLO PYTHON'
# text = text.islower()
# text = text.isupper()
# text = text.istitle()
# text = text.lower() #делает буквы маленькими
# print(text)
# text = text.upper() #делает буквы большими
# print(text)
# text = text.title() # делает первую букву кажд слова большой
# print(text)
# text = text.capitalize() # делает только первую букву большой
# print(text)
# text = text.swapcase() # инвертирует регистр, маленьк-большие, больш-маленькие
# print(text)

# text = 'hello\tpython'
# # text = text.expandtabs(15)       # Заменяет табуляции на пробелы, кривовато работает
# # print(text)
#
# # text = ' .-=+-hello.=+-python+-=-.'
# # print(text.lstrip('.=+-')) # убирает все проб симолы по умолч, либо то что выберем слево от строки
# # print(text.rstrip('.=+-')) # справа от строки
# # print(text.strip('.=+-'))  # и слева и справа
# print(text.removeprefix('hell'))  # удаляет на то что начинается
# print(text.removeprefix('rld'))   # удаляет на то что заканчивается
# print(text.removeprefix('rld').removesuffix('rld'))    # можно одновременно

# text = 'hello<b> python</b> world</b>'
# text = text.replace('<b>', '').replace('</b>', '')
# print(text)

# text = 'hello'
# text = text.center(13, '-') # центрует символы по умолч пробелы, либо на что-то своё
# print(text)

# text = 'hello'
# text = text.zfill(10) # заполняет нулями пустые места
# print(text)

# text = 'hello'
# text1 = text.ljust(10, '-') # дописывает тире справа
# text2 = text.rjust(10, '-') # дописывает тире слева
# print(text1)
# print(text2)



# text = 'hello python'
# print('java' in text)         # проверка на вхождение и не вхождение
