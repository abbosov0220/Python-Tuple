words = ("apple", "banana", "strawberry", "kiwi")

eng_uzun_soz = ""
uzunlik = 0

for word in words:
    if len(word) > uzunlik:
        uzunlik = len(word)
        eng_uzun_soz = word

print(eng_uzun_soz)
