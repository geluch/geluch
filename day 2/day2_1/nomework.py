# იუზერს ვეკითხებით სახელს გვარს შეფასებას
#ვამოწმებთ სახელში 2ზე მეტი ასო აქვს ი
# გვარი მთავრდება შვილზე
# ქულა მეტია 50 ზე
# დაპრინტოს დაფორმატებული ტექსტი თქვენ მოიგეთ სახელი გვარი ქულა

#else
# თქვენ წააგეთ სახელი გავარი ქულა

name = input("sheitanet tkveni saxeli: ")
surname = input("sheitanet tkveni gvari: ")
grade = int(input("sheitanet qula: "))

win =("you win , saxeli {}, gvari {}, qula {}")
loss =("you loss, saxeli {}, gvari {}, qula {}")

if name.count("i")==2 and (surname[-6:])=="shvili" and grade >50:
    print(win.format(name,surname,grade))
else:
    print(loss.format(name,surname,grade))
