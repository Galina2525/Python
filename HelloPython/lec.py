## Типы данных и переменная
## int, float, boolen, str, list, None
# value = None
# print(type(value))

# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
#value = 12334
#print(type(value))
# s = "hello 'world"
# s = 'hello "world'
# s = 'hello \'world'
#s = 'hello \nworld'
# s = 'hello world'
# print(s)
# print(a,'-',b, '-',s)
# print('{} - {} - {}'.format(a,b,s))
# print('{1} - {2} - {0}'.format(a,b,s))
# print(f'{a} - {b} - {s}')

#  #f = True
#  f = False
#  print(f)

# list = ['1','2','3', 'hello']
# print(list)

# print('Введите a');
# a = int(input())
# print('Введите b');
# b = int(input())
# print(a,' + ', b, ' = ', a +b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')
 
 # Арифметические операции
 # +, -, *,/, %, //, **
 # **,  ,  , *, /, //, %, +, -
 
 
# a = 1.321451111
# b = 3
#c = a//b   # если хотим получить целое цисло от деления
#c = a**b   # если хотим a возвести в степень b
#c = round(a*b,7)   # если хотим  округлить до 7 знаков после запятой
#print(c)

#(), Сокращенные операции
#a = 3
#a = a + 5 или 
#a += 5
#print(a)

#Логические операции
# > , < , <= , >=, ==,!=
# not, and, or   -  не путать с &, |, ^
# is, is not, in, not in
# gen
# a = 1 < 4 and 5 > 2
# print(a)

# a = 'qwe'
# b = 'qwe'
# a ==b
# print(a==b)

# a = [1,2]
# b = [1,2]
# print(a==b)

# a = 1 < 3 < 5 < 9
# print(a)

# func = 1
# T = 4
# x =123
# print(func<T>(x))

# f = 1 > 2 or 4 < 6 #истино т.к. хотя бы одно истино
# print(f)

#f =[1,2,3,4,]
#print(f)
# print( 2 in f)
# print( not 2 in f)
#is_odd = f[1] % 2 == 0 # f с индексом 1 это 2 в списке
#print(is_odd)
# по умолчанию ноль - это ложь, а единичка это истина поэтому вышесказанное можно записать
# is_odd = not f[1] % 2
# print(is_odd)

#Управляющие конструкции
# if, if -else
# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print('максимальное число это ', a)
# else:
#     print('максимальное число это '  ,b)

# username = input('Введите имя: ')
# if username =='Галина':
#     print('Ура! Это же Галина!')
# elif username == ('Маша'):
#     print('Я так долго Вас ждал, Маша!')
# elif username == ('Андрей'):
#     print('Как дела, Андрей?') 
# else:
#     print('Привет,', username,'!')  
# 
#Тернарный оператор(условие if в одну строку)
# a = 2 if(num1 ==num2) else 4
#(если num1=num2, то а=2, если нет, то а=4)
#         

# Управляющие конструкции: while
# Задача. Инвертировать число 23 в 32. По окончании написать "Пожалуй хватит"
# original = 23
# inverted = 0
# while original !=0:
#     inverted = inverted * 10 + (original % 10)
#     original //=10
# else:
#     print('Пожалуй')    
#     print('хватит')    
# print(inverted)    

# Управляющие конструкции: for
# for i in 1,2,3,4,5:
#     print(i**2) квадрат каждого числа

# list = {1,2,4,6,3}    
# for i in list:
#     print(i*2)   

# r = range(10)
# for i in r:
#     print(i)

# for i in range(1,5): # от 1 до 4
#     print(i)
  
# for i in range (1,7,2):#от 1 до 6 с приращением 2
#     print(i)

# for i in 'qwerty':
#     print(i)    

#Работа с текстом
#text ='съешь ещё этих мягких французских булок'
#print(text[0])   #с (индекс 0)
#print(text[1])   #ъ(индекс 1)
#print(text[len(text)])   # IndexError
#print(text[len(text)-1])   # к
#print(text[-5])   # б - опускается len(text)
# print(text[:])   # print(text) съешь ещё этих мягких французских булок
# print(text[0:len(text)-1])   # print(text) съешь ещё этих мягких французских було
# print(text[0:len(text)-5])   # print(text) съешь ещё этих мягких французских 
# print(text[2:5])   # ешь 
# print(text[0:5])   # съешь 
# print(text[:5])   # съешь 
# print(text[len(text)-1:])   # к
# print(text[len(text)-3:])   # лок
# print(text[2:9])   # ешь ещё
# print(text[6:-18])   #  ещё этих мягких (длина строки или отрицательный символ)
# print(text[0:len(text):6])   #  сеикакл
# print(text[::6])   #  сеикакл

# text = text[2:9] + text[-5] + text[:2]
# print(text)

# Списки: введение
## list = list
# numbers =[1,2,3,4,5,6]
# ran = range(1,6)
# print(type(ran)) #<class 'range'>
# numbers = list(ran)
# print(numbers)  #[1, 2, 3, 4, 5]

# numbers =[1,2,3,4,5,6]
# print(numbers)     #[1, 2, 3, 4, 5, 6]
# numbers[0] = 10    #[10, 2, 3, 4, 5, 6]
# print()
# print(numbers)
# for i in numbers:
#     i *= 2
#     print(i)
# print(numbers)    

# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e)  # red green blue

# for e in colors:
#     print(e*2)    #redred greengreen blueblue

# colors.append('gray') # добавить в конец листа
# print(colors ==['red', 'green', 'blue', 'gray'])   # True
# colors.remove('red') # удаление элемента red
# del colors[0] # удаление элемента red

#Функции - это фрагмент программы, используемый многократно
# def f(x):
#     if x ==1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return

# arg = 1  # Целое <class 'str'>
# arg = 2.3  # 23 <class 'int'>

# arg = 2 # None <class 'NoneTipe'>
# print(f(arg))  
# print(type(f(arg)))  


# Шпаргалки из семинара

# range(start,stop,step)
# range(5)->[0,1,2,3,4]
# range(2,5)->[2,3,4]
# range(1,7,2)->[1,3,5]

# распечатать в строчку:
#print(i,end = ' '), а по умолчанию
#print(i,end ='\n')

# Как заполнить список из 5 чисел
# a =[]
# for _ in range(5):# _ это счетчик, который не используется
#     k = int(input('Введите число: ')) 
#     a.append(k)
#     см таск2

# Удаление из списка
#a.pop(5) или a.remove(5)

# Распечатать в обратном порядке
# print(a[::-1])

# Распечатать от -N N
#print(*range(-N,N+1))

# В логических операциях сначала выполняются действия в круглых скобках, потом not
# потом and потом or
#
# Обозначения логических операций
# V - or
# ^ - and
# ¬   not
# round округляет до близкого четного числа
# т.е. 57 округлится до 58

# после логической операции not лучше все взять в скобки

# Моржовый оператор
# while x:=int(input('-->')) < 0:
#      Print('Введите число больше нуля')
# (будет запрашивать число пока не введется положительное число)