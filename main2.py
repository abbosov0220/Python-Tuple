students = [
    ("Ali", ["Fizika", "Matematika"]),
    ("Laylo", ["Ingliz tili"]),
    ("Jasur", ["Matematika", "Informatika"])
]

Mat = input("Matn kiriting: ")
count = 0
for i in students:
        if Mat in i[1]:
           count += 1

print(f"{count} talaba Matematika fanini tanlagan.")
