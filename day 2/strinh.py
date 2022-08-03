name = "gela"
surname = "   chanturidze"
age = 32
location = "zestafoni"
#გამოიტანს რიგით მეორე სიმბოლოს
print(name[2])
#გამოიტანს ცვლადის სიმბოლოს სიგრძეს
print(len(name))
#ამოწმებს ცვლადში სიმბოლოს არსეობას
print("l" in name)
#SLICING ჩამოჭრა სიმბოლოს
print(surname[2:5])
print(surname[:5])
print(surname[2:])
#negativ index
print(surname[-10])

#capitalize რიგით პირველი სიმბოლოს გაზრდის მაღალ რეგისტრში
print(surname.capitalize())
#ყველა სიმბოლო გადაყავს მაღალ რეგისტრში
print(surname.upper())
#replace შეცვლის სიმბოლოს
print(surname.replace("t","T"))
#strip ჩამოაჭრის ზედმეტ სპეისებს
print(surname.strip(),name)

my_text = "me mikvars saqartvelo"
#დაშლის წინადადებას სიტყვებად რა სიმბოლოსაც გადავცემთ იმის მიხედვით
print(my_text.split("a"))

my_text1 = "me mqvia {} var {} clis da vcxovrob {}"
print(my_text1.format(name, age,location))
print(my_text1.count('a'))