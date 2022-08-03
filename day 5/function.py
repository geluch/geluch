def my_mean(arr):
    my_sum = 0
    for element in arr:
        my_sum +=element
    return my_sum/len(arr)

arr = []
amount_of_numbers=int(input("ჩაწერეთ რამდენი რიცხვის სეტან გსურთ: "))

for i in range(amount_of_numbers):
    x=int(input("შეიყვანეთ რიცხვი:  "+str(i+1)+"სიისთვის: "))
    arr.append(x)

print(my_mean(arr))