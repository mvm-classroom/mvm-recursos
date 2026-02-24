import random

num_secret = random.randint(1, 100)
intents = 0
endevinat = False

print("Endevina el nº entre 1 i 100")

while not endevinat:
    num_usuari = int(input("Nº: "))
    intents += 1
    
    if num_usuari < num_secret:
        print("El teu nº es més petit que el secret")
    elif num_usuari > num_secret:
        print("El teu nº es més gran que el secret")
    else:
        endevinat = True
        print(f"Correcte! L'has endevinat en {intents} intents")