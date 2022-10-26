# Вывод красной гирлянды

import turtle as t

for i in range(5):
    t.begin_fill()
    t.color('yellow','red')
    for j in range(3):
        t.forward(100)
        t.right(120)
    t.forward(120)
    t.end_fill()