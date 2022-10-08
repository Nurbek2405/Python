#7.1 Задача поиска ошибок, нехватало 1 открывающая скоба в строке 8
print('Первая задача ввести i')
i = int(input())
if i>1:
    i= i-1
    print(i)
elif i==1:
    i=(i+1)*3+1
    print(i)


#7.2 Не присвоена переменная b строка 16
print('Вторая задача')
a = float (input("a= '"))
b = 0
sum = a+b
if sum > 10:
    i = 'Try again'
    print(i)

# 7.3 Знак присваивание было без двух =, строка 27
print('Третья задача')
i = 10
if i > 1 and i < 10:
    i = i-1
    print(i)
elif i==1 or i==10:
    i = i +1
    print(i)
print(i+1)

# 7.4 Ошибки при сравнивание строки и цифры, несовместимы и присваивание типа цифр дроби или целые строки 36 и 41
print('Четвертая задача')
i = 5
if i>1:
    a=int(input())
    i=i+a 
    print(i)

elif i==1:
    b = int(input())
    i = i + b
    print(i)
else:
    print(i*2)

#7.5 Была упущена кавычка в 48 строке
i=int(input('Введите число'))
if i <=0:
    print(i)
elif i>0:
    i = i-10
    if i<=0:
        print(i)
    elif i > 0:
        i = i -10
        if i <=0:
            print(i)
        else:
            print('Error')

#7.6


#7.7