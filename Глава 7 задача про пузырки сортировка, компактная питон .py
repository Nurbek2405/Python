# меньше код в пайтоне, чем в других языках программирования

my_list = [3,5,2,3,1]
for j in range(4):
    for i in range(4):
        if my_list[i] > my_list[i+1]:
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    print(my_list)
print(my_list)

# хорошо бы это запомнить) часть вторая