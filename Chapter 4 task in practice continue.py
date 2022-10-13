# Измените с помощью оператора break первый программный код из задания 2 таким образом,
# чтобы конструкция завершилась при s = 30.

print('Глава 4, 5 задача 5: ')

s = 0                   # присваивание s
for k in range (3,10):  # цикл с предусловием до 10 не включая, с шагом 1 с 3 начиная
    s=s+6               # суммирование каждый раз s
    if s==30:           # условия выхода из цикла с помощью break
        break           # выход из цикла
print(s,'\n')                # вывод итогового значения

print("Глaва 4, задача 6:")
k = 1
while k<=64:
    k=k*2
    if k==8 or k==64:
        continue
    print(k)


print("Глaва 4, задача 7")
s = 10
k=0

for k in range(5):
    s -=k
print(s)


print("Глaва 4, задача 8: ")
s = -30
for k in range(5):
    s+=6
print(s)

print("Глaва 4, задача 9.1: ")
for i in range(25,30,2):
    print(i)

print("Глaва 4, задача 9.2: ")
i = 7
while i>0:
    i=2*i-10
print(i)

print("Глaва 4, задача 9.3: ")
#   a = 35
#   while a <= 50:
#   if a == 43 or a == 47:
#      continue
#   if a % 2 == 1:
#      print(a)
#   a = a + 2

print("Глaва 4, задача 9.4: ")

a = 'Key'
b = 2021
for i in a:
    print(b%10)
    b=b//10