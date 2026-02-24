#Quantitat beguda  per hora d'exercici = 0,5 litres

import math

temps = float(input("Temps d'exercici: "))
litres_a_beure = temps * 0.5
litres_sencers = math.floor(litres_a_beure)

print("Com has estat", temps, "hores fent exercici, has de beure",
      litres_sencers, "litre de líquid per mantenir-te en un bon nivell d'hidratació")