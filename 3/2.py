#Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3

number1 = float(input('Enter number 1: '))                #ВОПРОС!! Почему мы тут всё должны приводить к инту либо флоту?
number2 = float(input('Enter number 2: '))                #без инта либо флота не делится я проверял
number3 = float(input('Enter number 3: '))
common = ((number1 + number2 + number3) / 3)

print(round(common, 3))
