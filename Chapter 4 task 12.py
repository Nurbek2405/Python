
a = float(input('Введите любое число, проверим делится ли она на 3: '))
aold=a
s = 0
while a != 0:
    s+=a%10
    #print('s=',s)
    a=(a-a%10)//10
    #print('a=',a)
if s/3 == int(s/3):
    #print('s=',s)
    print('Число ',aold,' является делимым на 3')
else:
    print('Число ',aold,' не является делимым на 3')