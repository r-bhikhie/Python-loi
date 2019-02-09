# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 21:46:12 2019
Ex 01
@author: Ravi
"""


# 1 Principes van Python
# OPDRACHT
# 1) Een variable maak je met een toekenning (assignment).
# 2) Een variable kan van elk type zijn: het type van wat je toekent (assigns).
# 3) Een string wordt omringt door enkele of dubbele aanhalingstekens (quotes).
# 4) Alles op dezelfde regel achter het #-teken is commentaar.
#    Het is toelichting op de programma-code en wordt niet uitgevoerd (executed).
# 5) Een lijst (list) is een handige gegevensverzameling. Voorbeeld: [2,4,6,8,10]
# 6) Met de for-loop kun je door een lijst lopen
# 7) Let op de dubbele punt, we beginnen een nieuw blok
# 8) Een nieuw, ondergeschikt blok (block, suite) springt in.

naam = "Joke Sluis"                          # (1,2,4)
geslacht = 'vrouw'                           # (1,2,4)
leeftijd = 19                                # (1)
salaris = 1745.50                            # (1,2)
joke = [naam,geslacht,leeftijd,salaris]      # (5)

for kenmerk in joke:                         # (6,7,8) 
    print(kenmerk)

# plaats hieronder uw uitbreiding

"""
OPGAVE
1) Een string literal (bv: 'Joke Sluis') moet worden ingesloten in matching quotes.
   Wat wordt daarmee bedoeld, denkt u?

2) Breid het programma uit.
   Maak een nieuwe lijst jan met de volgende kenmerken: Jan Bakker, man, 42, 1977.40.
   Druk de kenmerken van jan af (elk kenmerk op een aparte regel).
"""

print('1): Strings are delimited by the same type of quotes, be that single or double. Or triple quotes.')

john = ['John Baker','male', 42, 1977.40 ]
print('2):')
for property in john:
    print(property)
