# Рисунки

import turtle as t
t.speed(11)

# двигаемся в лево
t.up()
t.left(135)
t.forward(300)
t.down()

# рисуем круги, 3 раза
for i in range(3):
    t.circle(50)
    t.left(120)
# перемещаем для след фигуры
t.up()
t.right(135)
t.forward(300)
t.down()

#рисуем равнобедренные треугольники
for j in range(3):
    t.begin_fill()
    t.color('black','yellow')
    for i in range(3):
        t.forward(100)
        t.left(120)
    t.end_fill()
    t.left(120)

# перемещаем для след фигуры
t.up()
t.left(5)
t.forward(300)
t.down()

# рисуем квадраты
for j in range (3):
    t.begin_fill()
    t.color('green','red')
    for g in range(4):
        t.forward(100)
        t.left(90)
    t.left(120)
    t.end_fill()

# передвигаемся на след фигуру
t.up()
t.left(200)
t.forward(600)
t.down()

# рисуем пятиугольники
for l in range(3):
    t.begin_fill()
    t.color('black','green')
    for k in range(5):
        t.forward(80)
        t.left(72)
    t.left(120)
    t.end_fill()

# передвигаемся на след фигуру
t.up()
t.left(155)
t.forward(400)
t.down()


# рисуем последнюю фигуру
for p in range(3):
    t.begin_fill()
    t.color('black','purple')
    for o in range(6):
        t.forward(70)
        t.left(60)
    t.left(120)
    t.end_fill()