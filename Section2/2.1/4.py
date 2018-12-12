phrase = input("Enter a phrase: ")
words = phrase.split()
acronym = ""
for w in words:
    acronym = acronym + w[0].upper()
print("Acronym for your phrase: ",acronym)
