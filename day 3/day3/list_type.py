#ordered
from operator import truediv


my_list = ["gela","gaga","sofo","ანანო"]
print(my_list)

#რომელიმე ჩანაწერის შეცვლა ნუმერაციის ათვლა იწყება 0_დან 
#მაგ. ამ სიაჩი არის ჩანაწერები ნომრით 0,1,2,3
# my_list[2]="lobiani"
# print(my_list)

#sort სიის დალაგება
#my_list.sort()# დალაგება A_Z
#my_list.sort(reverse=True)#დალაგება Z_A

#ამოშლა ჩანაწერის სიიდან
#my_list.remove("gela")
#del my_list #სიის წაშლა
#my_list.clear() #სიის გასუფთავება
#print(my_list[3:4]) #სიიდან სასურველის ჩანაწერის/ჩანაწერების დაბეჭდვა
#print(my_list[-2])#სიიდან სასურველის ჩანაწერის/ჩანაწერების დაბეჭდვა უკუთვლის შემთხვევაში
new_list=my_list[2:4]#მონაცემების ერთი სიიდან მეორეში გადატანა
#new_list.append("nino")#სიასი ახალი მონაცემის შეტანა
print(new_list)

print("gela" in my_list)#ამოწმებს სიაში კონკრეტული ჩანაწერის არსებობას