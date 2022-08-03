
def my_fun(my_list):
    for i in range(len(my_list)):
        my_list[i]=my_list[i]**2
    return my_list

print(my_fun([10,20,30,40]))
