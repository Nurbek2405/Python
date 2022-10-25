import turtle as t
a1= (input('Выберите цвет из blue,green,orange,pink: '))
if a1=='blue' or a1== 'pink' or a1=='green' or a1== 'orange':
    t.color(a1)
    n=4
    for i in range (n):
        t.forward(50) 
        t.left(90) 
    t.left(30) 
    t.backward(20) 
    t.forward(20) 
    t.left(60) 
    t.forward(50) 
    t.right(60) 
    t.backward(20) 
    t.left(60) 
    t.backward(50) 
    t.right(90) 
    t.forward(50) 
    t.left(30) 
    t.forward(20)
else:
    print('Вы выбрали неправильный цвет!')

 