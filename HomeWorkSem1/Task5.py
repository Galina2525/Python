#Напишите программу, которая принимает на вход координаты двух точек
# и находит рассояние между ними в 2D пространстве
#A(3,6) B(2,1) - 5.0
#(7,-5) B(1,-1) - 7,21
 # AB = √ (x(B) - x(A))² + (y(B) - y(A))²
xA = int(input('Введите xA '))
xB = int(input('Введите xB '))
yA = int(input('Введите yA '))
yB = int(input('Введите yB '))
import math
AB = math.sqrt((xB - xA)**2 + (yB - yA)**2)
print(round(AB,2))