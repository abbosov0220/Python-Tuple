emails = (
    ("Ali", "ali@gmail.com"),
    ("Vali", "vali@yandex.ru"),
    ("Sami", "sami@mail.ru")
)

domains = [] 

for person in emails:
    email = person[1]
    parts = email.split("@") 
    domain = parts[1]  
    domains.append(domain) 

print(domains)
