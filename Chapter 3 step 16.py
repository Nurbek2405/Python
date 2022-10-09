# 16 задача, Напишите программу, которая запрашивает левую А и правую В границы числового промежутка и спрашивает,
# какой тип числового промежутка вывести на экран. При этом:




numa=float(input('Введите левую границу промежутка:\n'))
numb=float(input('Введите правую границу промежутка:\n'))
numequals=str(input('Вывести интервал, полуинтервалы или отрезок с заданными границами?\n'))
if numequals == 'интервал' or numequals == 'Интервал' or numequals == 'интервалы' or numequals == 'Интервалы':
    print('(', numa ,';', numb ,')')
elif numequals == 'полуинтервалы' or numequals == 'полуинтервал' or numequals == 'Полуинтервал' or numequals == 'Полуинтервалы':
    print('(', numa ,';', numb ,'] и [',numa,';',numb,')')
elif numequals == 'отрезок' or numequals == 'Отрезок' or numequals == 'отрезки' or numequals == 'Отрезки':
    print('[', numa ,';', numb ,']')
else:
    print('Ошибка ввода, введеные неправильные данные')