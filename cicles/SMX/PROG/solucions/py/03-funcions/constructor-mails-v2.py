# Funció per construir el mail
def construir_mail(nom, cognom, domini):

    resultat = nom.lower() + cognom.lower() + "@" + domini.lower()
    # També valdria fer un resultat.lower()

    return resultat

# Programa principal
n = input("nom:")
c = input("cognom:")
d = input("domini:")

#Ara faig servir la meva funció
email = construir_mail(n,c,d)

print("e-mail: ", email)