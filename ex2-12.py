# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 01:57:38 2019

@author: Ravi

Zoek uit (start met Google search) wat mutable betekent in de Python-context.
Het doel van uw zoektocht is een verklaring te geven voor de respons van de shell.
Schrijf uw verklaring op. Doe dat helder en beknopt.

Maak het codefragment werkend.
Verplicht: gebruik alleen slicing (géén loops, functies, methods of andere constructies).
"""

print("De list slice voor 'Ams' probeert strings aan te passen terwijl dat geen optie is.")
ams = 'Amsterdam'
rot = 'Rot'
ans = rot+ams[3:]
print(ans)
