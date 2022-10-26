# Вывод разноцветной гирлянды без заливки гирлянды

import turtle as t
for j in range(5):
    t.color('black','purple')
    t.begin_fill()
    for j in range(4):
        t.forward(100)
        t.right(90)
    t.forward(120)
    t.end_fill()