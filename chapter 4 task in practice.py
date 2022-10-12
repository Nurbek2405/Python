# Заполните пустые ячейки таблицы, используя знания о функции range();



for n in range (0,4,4):
    print(n)

print("Задача 2.1  глaва 4 циклы\n")
s = 0
for k in range (3,10):
    s = s+6
print(s)


print("Задача 2.2  глaва 4 циклы\n")
k = 0
for m in range(1,10,2):
    k +=6
    print(k)

print("Задача 2.3  глaва 4 циклы\n")
s = 0
for k in range(5):
    k -=k
print(s)

print("Задача 3.1  глaва 4 циклы\n")
s = -30
while s<0:
    s+=6
print(s)

print("Задача 3.2  глaва 4 циклы\n")
s = 1
n = 15
while n>0:
    n=n-s
    s=s*2
print(n)

print("Задача 3.3 глaва 4 циклы\n")
k = 1
while k<=64:
    k=k*2
    print(k)


print("Задача 4 глaва 4 циклы\n Таблицы итерации:\n")
print('№ задачи количество итерации \n  2.1            7 раз\n  2.2            5 раз \n  2.3            5 раз \n  3.1            5 раз \n  3.2            4 раз \n  3.3            7 раз ')
