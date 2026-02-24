# Funció per construir el mail
def construir_mail(nom, cognom, domini):
    resultat = nom + cognom + "@" + domini

    return resultat

# Programa principal
n = input("nom:")
c = input("cognom:")
d = input("domini:")

#Ara faig servir la meva funció
email = construir_mail(n,c,d)

print("e-mail: ", email)