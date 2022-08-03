#dictionaries არის სიის ტიპი სადაც შეგვიძლია ჩანაწერების შეცვლა
#შეგვიძლია გამოვიძახოთ მნიშვნელობები ცალცაკე ordered
#და არ არის დუბლიკატების გაკეთება შესაძლებელი

#სიის ჩანაწერი არის შემდეგი key:value key აუცილებლად სტრინგი უნდა იყოს
my_dict={
    "name":"gela",
    "surname":"chanturidze",
    "age":22,
    "location":"zestafoni",
    "children":["gio","sandro","luka"]
}
print(len(my_dict))#სიგრძის გამოტანა
print(my_dict["surname"])#კონკრეტული ცვლადის გამოტანა
my_dict["children"][1]="gaga"
print(my_dict)
