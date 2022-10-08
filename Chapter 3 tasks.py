#--------6.1---------------------------
print('\n1 задача') 
i=10
if i > 1:
    i = i -1
print(i)

#--------6.2----------------------------
print('\n2 задача') 
i=1
if i>1:
    i=i-1
    print(i)

elif i==1:
    i = (i+1)*3+1
    print(i)

#--------6.3----------------------------
print('\n3 задача') 
i=int(-3)
if i > 1:
    i = i-1
    print(i)
elif i == 1:
    i = i+1
    print(i*2)
else:
    print(i**2)

#--------6.4----------------------------
print('\n4 задача ') 
i=40

if i <=0:
        print(i)
elif i < 0:
    i = i - 10
    if i <= 0:
        print(i)
elif i > 0:
    i= i - 10
    if i <=0:
        print(i)
else:
    print('error')
 
  
print('\n5 задача') 
i=10
if i>1 and i < 10:
    i = i -1
    print(i)
elif i == 1 or i == 10:
    i = i + 1
    print(i)
print(i+1)

#--------6.6---------------------------- 
print('\n6 задача ') 

i = 4
if i > 1 and i < 10:
    i=i*2
    print(i)
    if i>1 and i < 10:
        i = i*2
        print(i)
        if i>1 and i <10:
            print(i*2)
        else:
            print(i+2)
    else:
        print (i+2)
else:
    print(i)
