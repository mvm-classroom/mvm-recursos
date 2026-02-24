preu_unitat = float(input("Preu per unitat: "))
descompte_unitat = float(input("Descompte per cada unitat: "))
despeses_vancances = float(input("Despeses de les nostres vacances: "))

benefici_unitat = preu_unitat * (descompte_unitat / 100)

num_a_comprar = despeses_vancances / benefici_unitat

print("")
print("---------------------------------------------------------------------------------------------")
print("Preu per unitat:", preu_unitat, "€")
print("Descompte per cada unitat:", descompte_unitat, "%")
print("Benefici per unitat:", benefici_unitat, "€")
print("Depeses de les nostres vacances: ", despeses_vancances, "€")
print("---------------------------------------------------------------------------------------------")
print("Nº de Toblerones que hem de comprar i revendre per amortitzar les vancances:", num_a_comprar)
print("---------------------------------------------------------------------------------------------")