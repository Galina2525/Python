# Напишите программу, в которой пользователь будет задавать две строки,
# а программа определять количество вхождений одной строки в другой
#" Я люблю Python"
#"лю"
# --> 2

# text = 'Я люблю Python '
# print(text)
# char = input('Введите значение поиска: ')
# len_char = len(char)
# i = 0
# count = 0
# while i < len(text)-1:
#     if char.lower() == text[i:len_char+i].lower():
#         count +=1
#     i+=1    
# print(count)

# text = 'Я люблю Python '
# print(text)
# searchText = input('Введите значение поиска: ')
# list = text.split(searchText)
# print(len(list)-1)

text = 'Я люблю Python '
print(text) 
searchText = input('Введите значение поиска: ')
count = 0
for i in range(len(text)-len(searchText)+1):
    if text[i:i+len(searchText)]==searchText:
        count+=1
print(count)        

