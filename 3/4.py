#Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных

number1 = float(input('Enter number 1: '))
number2 = float(input('Enter number 2: '))
number3 = float(input('Enter number 3: '))
print('Positive: ', (number1 > 0) + (number2 > 0) + (number3 > 0))
print('Negative: ', (number1 < 0) + (number2 < 0) + (number3 < 0))




