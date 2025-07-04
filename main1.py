people = [("Ali", 24), ("Laylo", 30), ("Jasur", 19)]

eng_katta_ism = ""
eng_katta_yosh = 0

for person in people:
    ism = person[0]
    yosh = person[1]
    
    if yosh > eng_katta_yosh:
        eng_katta_yosh = yosh
        eng_katta_ism = ism

print(f"{eng_katta_ism} — {eng_katta_yosh} yosh")
