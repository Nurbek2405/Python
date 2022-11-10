my_list = [5,4,3,2,1]

for i in range(4):
    if my_list[i] > my_list[i+1]:
        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    print(my_list)
print(my_list)