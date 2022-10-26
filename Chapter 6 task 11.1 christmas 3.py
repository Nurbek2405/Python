# Вывод разноцветной гирлянды без заливки гирлянды

import turtle as t

t.color('yellow','red')
t.begin_fill()
for j in range(3):
    t.forward(100)
    t.right(120)
t.forward(120)
t.end_fill()

t.begin_fill()
t.color('green','yellow')
for j in range(3):
    t.forward(100)
    t.right(120)
t.forward(120)
t.end_fill()

t.begin_fill()
t.color('red','green')
for j in range(3):
    t.forward(100)
    t.right(120)
t.forward(120)
t.end_fill()

t.begin_fill()
t.color('yellow','black')
for j in range(3):
    t.forward(100)
    t.right(120)
t.forward(120)
t.end_fill()

t.begin_fill()
t.color('black','purple')
for j in range(3):
    t.forward(100)
    t.right(120)
t.forward(120)
t.end_fill()
