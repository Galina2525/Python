# Напишите программу, которая принимает на вход координаты
# точки (X и Y), причем X ≠ 0 Y ≠ 0 и выдает номер четверти плоскости
# в которой находится эта точка( или на какой оси она находится).
# x =34, y = -30  -> 4 
# x =2, y = 4  -> 1 
# x = -34, y = -30  -> 3 

x = int(input('Введите X '))
y = int(input('Введите Y '))
if x > 0 and y > 0:
    print('Плоскость 1')
elif  x < 0 and y > 0: 
     print('Плоскость 2')
elif  x < 0 and y < 0: 
    print('Плоскость 3')  
else:
    print('Плоскость 4')       