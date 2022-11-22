# first_name = 'alex'
# age, city = 42, 'Minsk'
#
# print(first_name, age, city, end=' конец строки ', sep='---')
# print(city)


# l_name = input('Enter last name: ')
# print(True+True)

# age = input('enter age: ')
# age = int(age)
# print(age)
#
# googol = 1_000_000_000_000_000
# print(googol)

# a = 5
# b = 2
# a = a % b
# print(a)

# a = 3.565454545
# a = round(a, 3)
# print(a)
# a = 23.56
# b = 24.56
# print(round(a))
# print(round(b))
# a = '3.45'
# a = float(a)
# print(a)



# a = 0.1 + 0.1 + 0.1
# a = round(a)
# print(a)

# a = -5
# a = abs(a)
# print(a)
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
# print((f_name + ' ') * 3)

# text = 'hello world'
# symbol = text[::-1]
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
#
# text = 'Hello %s, age %d' % (name, age)
# text2 = 'Hello {name}, age {age}'.format(name=name, age=age)
# text3 = f'Hello {name}, age {age}'
# print(text)
# print(text2)
# print(text3)

# text = 'hello world python pycharm'
# words = text.split(' ')
# text2 = '.-.-'.join(words)
# print(text2)

# text = 'hello python hello world python'
# a = text.find('python', 7, 12)
# b = text.rfind('python', 0, 20)
# a = text.index('python')
# b = text.rindex('python')
# print(a)
# print(b)
# print(text.count('Python'))

# text = 'hello python world python pycharm'
# print(text.partition('python'))
# print(text.rpartition('python'))

# text = 'hello java java, java'
# text = text.replace('java', 'python', 2)
# print(text.isalpha())

# text = 'Hello Python'
# print(text.startswith('Hell'))
# print(text.endswith('hon'))

# text = 'HELLO PYTHON'
# text = text.lower()
# print(text)
# text = text.upper()
# print(text)
# text = text.title()
# print(text)
# text = text.capitalize()
# print(text)
# text = text.swapcase()
# print(text)

# text = 'hello\tpython'
# text = text.expandtabs(15)
# print(text)

# text = ' .-=+-hello.=+-python+-=-.'
# print(text.lstrip('.=+-'))
# print(text.rstrip('.=+-'))
# print(text.strip('.=+-'))

# text = 'hello<b> python world'
# text = text.removeprefix('<b>').removesuffix('</b>')
# print(text)

text = 'hello python'
print('java' not in text)
