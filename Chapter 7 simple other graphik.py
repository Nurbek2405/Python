import turtle as t

t.bgcolor('black')
t.tracer(30)

for i in range(300):
    t.color('cyan')
    t.up
    t.goto(0,0)
    t.fd(i)
    t.down()
    t.begin_fill()
    t.circle(20,100)
    t.end_fill()
t.done()