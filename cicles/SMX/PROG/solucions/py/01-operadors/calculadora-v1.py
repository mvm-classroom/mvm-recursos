import_inicial = int(input("Import inicial:"))
percnt_propina = int(input("% de propina:"))
import_propina = import_inicial * (percnt_propina / 100)
total_a_pagar = import_inicial + import_propina

print("Import inicial:", import_inicial, "€")
print("Propina (",percnt_propina, "%):", import_propina, "€")
print("--------------------------------------------------------")
print("Total a pagar:", total_a_pagar, "€")