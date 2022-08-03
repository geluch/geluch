from dataclasses import replace
from itertools import count


surname="chanturidze"
#პირველი ასოს გადიდება
print(surname.capitalize())
#ყველა ასოსო გადიდება
print(surname.upper())
name="gela"
print(surname.replace("c","C"))
#strip აორებს ზედმეტ სპეისებს
print(name.strip(),surname)

my_text="i love georgia"
#გადაეცემა გახლეჩვის ადგილი split(აე რაც ჩაიზერეგა იმ ადგილებში გაიხლიჩება)
print(my_text.split())

age=22
name='gela'
my_text="my name is {} and i am {} yars old"

print(my_text.format(name,age))
#ითვლის სიმბოლოების რაოდენობას
print(surname.count("a"))


age=str(age)

count =0
for char    in age:
    if char=="0":
        count+=1
print(count)



