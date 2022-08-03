num1 = int(input("enter num1: "))
# num2 = int(input("enter num2: "))

#რიცხვის შედარება რომელია მეტი
# if num1>num2:
#     print(num1, "aris meti",num2)
# elif num2>num1:
#     print(num2," is gret",num1)
# else:
#     print(num1,"=",num2)


#ლუწი და კენტის გარჩევა 
# if (num1 % 2 )==1:
#     print("ricxvi kentia")
# else:
#     print("ricxvi lucia")

#გარკვეული პირობით რიცხვების ამორჩევა
# if num1 % 2 ==0 and 10<=num1<=30:
#     print("ricxvi  aris jigari")
# else:
#     print("ricxvi ar aris jigari")

#nested conditional
if 10<=num1 and num1<=30:
    if num1 % 2==0:
        print("ricxvi aris jigari")
    else:
        print("ricxvi")
else:
    print("ricxvi ar aris jigari")