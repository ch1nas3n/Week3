zin = 'Guido van Rossum heeft programmeertaal Python bedacht.'
list = ['a', 'e', 'o', 'u', 'i']
naam = ""
for letter in zin:
    if letter in list:
        naam = naam + letter
        print(naam)
