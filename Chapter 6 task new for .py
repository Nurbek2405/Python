# Гирлянда из треугольников, направленных вниз

import turtle as t

t.bgcolor('green')
t.color('red')
n=3
m=6
for b in range(m):
    for i in range(n):
        t.forward(100)
        t.right(120)
    t.forward(120)