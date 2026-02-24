#Quantitat beguda  per hora d'exercici = 0,5 litres

import math

temps = float(input("Temps d'exercici: "))
litres_a_beure = temps * 0.5
litres_sencers = math.floor(litres_a_beure)

text_hores = "hores"
if temps == 1:
    text_hores = "hora"

text_litres = "litres"
if litres_sencers == 1:
    text_litres = "litre"

print("Com has estat", int(temps), text_hores,"fent exercici, has de beure",
      litres_sencers, text_litres, "de líquid per mantenir-te en un bon nivell d'hidratació")