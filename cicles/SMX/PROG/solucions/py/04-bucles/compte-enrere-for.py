import time

numero = int(input("Quants segons vols que duri el compte enrere?: "))

for i in range(numero, 0, -1):
    print(i)
    time.sleep(1)  # Espera 1 segon

print("¡JA!")