import_inicial = int(input("Import inicial:"))
percnt_propina = int(input("% de propina:"))
import_propina = import_inicial * (percnt_propina / 100)
total_a_pagar = round(import_inicial * (1+(percnt_propina / 100)),2)

print("Import inicial:", import_inicial, "€")
print("Propina (",percnt_propina, "%):", round(import_propina,2), "€")
print("--------------------------------------------------------")
print("Total a pagar:", total_a_pagar, "€")