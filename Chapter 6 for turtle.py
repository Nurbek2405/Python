# Напишем программу, позволяющую пользователю самому решать, какой правильный многоугольник нарисовать с помощью Черепашки:

import turtle as t
n = int(input('Количество вершин многоугольника: '))
g = ((n-2)*180)/n
if n%2 ==0:
    t.bgcolor('yellow')
    t.color('red')
else:
    t.bgcolor('red')
    t.color('yellow')
for i in range(n):

    t.forward(100)
    t.left(180-g)