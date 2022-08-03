from dataclasses import replace
from itertools import count


#surname="          chanturidze              geluka                   "
#name="gela"
#პირველი ასოს გადიდება
# print(surname.capitalize())
#ყველა ასოს გადიდება
#print(surname.upper(),name)
#name="gela"
# print(surname.replace("c","C"))#ცვლის ცვლადში ჩვენთვის სასურველი ასოს
#print(name.strip(),surname.strip(),name) #strip() შლის ცვლადში ზედმეტ სპეისებს თავსა და ბოლოში

my_text="i love georgia"
#გადაეცემა გახლეჩვის ადგილი split(აქ რაც ჩაიწერება იმ ადგილებში გაიხლიჩება)
print(my_text.split())


# age=22
# name='gela'
# my_text="my name is {} and i am {} yars old"

# print(my_text.format(name,age))
#ითვლის სიმბოლოების რაოდენობას
# print(surname.count("a"))


# age=str(age)

# count =0
# for char    in age:
#     if char=="":
#         count+=1
# print(count)



