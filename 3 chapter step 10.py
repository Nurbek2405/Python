# 10 задача
print('Программа которая выводит на каком языке выводится пароль')
pas = str(input('Введите пароль qwerty: '))
if pas == 'qwerty':
    print('ENG')
elif pas == 'йцукен':
    print('РУС')
else:
    print('Неправильно введен пароль!')