import time

numero = int(input("Quants segons vols que duri el compte enrere?: "))

while numero > 0 :
    print(numero)    
    time.sleep(1)  # Espera 1 segon
    numero -= 1

print("¡JA!")