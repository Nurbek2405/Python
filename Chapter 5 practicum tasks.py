# Практикум задачи по 5 главе

import math as mat
import random

print("Задача из 5 главы 1.1")
r = int(input("Введите радиус: "))
c = 2*mat.pi*r
print("c=2*pi*r",c)

a = random.randrange(1,4)
print('randrange= ',a)

b = mat.fabs(-5)
print("модуль x, fabs(-5)",b)

b = mat.ceil(2.404)
print("округления вверх, math.ceil(2.404)",b)

b = mat.floor(-2.404)
print("округления вниз, math.floor(-2.404)",b)

b = mat.fmod(54,3)
print("остаток от деления, math.fmod(54,3)",b)

b = mat.sqrt(4096)
print("квадратный корень из math.sqrt(4096)",b)

print("Задача из 5 главы 4.1")
a = mat.pow(mat.pow(2,3),2)
print('возведение в степень через pow(x,y), (2^3)^2',a)

print("Задача из 5 главы 4.2")
a = int(mat.pow(mat.pow(8,3),0))
print('возведение в степень через pow(x,y), ((8^3)^0)*2',a*2)

print("Задача из 5 главы 4.3")
a = int(mat.pow(mat.pow(8,3),0))
print('возведение в степень через pow(x,y), ((8^3)^0)*2',str(a*2))

print("Задача из 5 главы 4.4")
a = mat.pow(-5,2)//mat.pow(2,5)
print('mat.pow(-5,2)//mat.pow(2,5)\n','<',a,'>\n___^___')

