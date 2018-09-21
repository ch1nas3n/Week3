leeftijd = int(input('Geef je leeftijd: '))
paspoort = input('Bezit je over een Nederlands paspoort: ')

if leeftijd < 18 and paspoort == 'Ja':
    print('Gefeliciteerd, je mag stemmen!')
print('Sorry, je mag niet stemmen!')