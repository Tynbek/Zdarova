#   Без использования collections, написать программу, которая будет
#    создавать словарь для подсчитывания количества вхождений каждой
#    буквы в текст введенный с клавиатуры

text = input('Vvedite text: ')
data = {text[i]: text.count(text[i]) for i in range(0, len(text))}
print(data)

#2 Сп
# from collections import Counter
# text = input('Vvedite text: ')
# data = Counter(text)
# print(data)

#3 Сп

# text = input('Vvedite text: ')
# data = {i: text.count(i) for i in text}
# print(data)
