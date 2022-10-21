a = 52344
s = 0
while a != 0:
    s+=a%10
    print('s=',s)
    a=(a-a%10)//10
    print('a=',a)
if s/3 == int(s/3):
    print('s=',s)
    print(True)
else:
    print(False)