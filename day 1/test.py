# # from unicodedata import name


full_name = "gela chanturidze"
# print(full_name.capitalize())#პირველი ასო მაღალ რეგისტრში იწერება
#print(full_name.upper())# ყველა სიმბოლო მაღალ რეგისტრში
# print(full_name.replace("g","G"))#ცვლის ცვლადში არსებულ სიმბოლოს მაგ. g შეიცვლება G
name="gela"; surname="chanturidze"
age=31;location='zestafoni'
# print(name+surname)#Concatenate=შეერთება სტრინს ცვლადებს, ხოლო რიცხვით ტიპებს ამატებს ერთმანეთზე
# print(name+str(age))#თუ გვინდა სტრინგს დავუმატოთ რიცხვითი ცვლადი მაშინ ეს ცვლადიც უნდა გავასტრინგოთ
# print(name.upper(),surname.split()) #split 
# print(type(full_name))

# # text="me mikvars saqartvelo"
# # print(text.upper().capitalize().split())

# my_text="me mqvia {} chami gvaria {} var {} clis da vcxovrob {}"
# print(my_text.format(location,age,surname,name))
# print(len(location))
# print("g" in name)
# #ითვლის ცვლადში სასურველი სიმბოლოების რაოდენობას
# age=str(age)
# count=0
# for char in surname:
#     if char == "e":
#         count+=1
# print(count)

# firs_num=2.0001
# second_num=5
# third_num=firs_num*second_num

# print(round(third_num))

# world="hello" "all"
# all=world*5
# print(world[2:]+world[:2])
# print(all[2:12])

# word="supercalifragilisticexpialidocious"
# print(len(word))

# a,b=0,1
# while b<50:
#     print(b)
#     a,b=b,a+b