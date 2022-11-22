# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя
# способами

#1 Способ

# text = input('Enter your sentence: ')               #Не понял почему получилось
# text = '-'.join(text.split(' '))
# print(text)

#2 Способ

text = input('Enter your sentence: ')
print(text.replace(' ', '-'))


