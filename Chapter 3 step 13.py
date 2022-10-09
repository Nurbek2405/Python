# Напишите программу, которая запрашивает два числа a и b и выводит результаты a + b, a - b, a * b, a / b. 
# При этом если b = 0, то выводится сообщение о несуществовании результата a / b.

numa = int(input('Введите число a: '))
numb = int(input('Введите число b: '))
print('a+b=', numa+numb)
print('a-b=', numa-numb)
if numa==0 or numb==0:
    print('a/b - не существует (делить на 0 нельзя!)')
else:
    print('a/b=', numa/numb)
if numa==0 or numb==0:
    print('a*b - не существует (умножать на 0 нельзя!)')
else:
    print('a*b=', numa*numb)