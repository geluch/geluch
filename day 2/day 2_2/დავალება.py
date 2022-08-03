name = input("sheitanet saxeli: ")
surname = input("sheitanet gvari: ")
grade = int(input("sheitanet qula: "))
win = ("you win, saxeli {}, gvari {}, qula {}")
loss = ("you loss, saxeli {}, gvari {}, qula {}")

if (name.count("i"))==2 and (surname[-6:])=="shvili" and grade>50:
    print(win.format(name,surname,grade))
else:
    print(loss.format(name,surname,grade))