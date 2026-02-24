stock_inicial = int(input("Stock inicial: "))

unitats_cli1 = int(input("Unitats comprades pel client 1:"))
unitats_cli2 = int(input("Unitats comprades pel client 2:"))
unitats_cli3 = int(input("Unitats comprades pel client 3:"))

stock_final = stock_inicial - unitats_cli1 - unitats_cli2 - unitats_cli3

print("")
print("----------------------------------")
print("Stock inicial:", stock_inicial)
print("----------------------------------")
print("Compra client 1: -", unitats_cli1)
print("Compra client 2: -", unitats_cli2)
print("Compra client 3: -", unitats_cli3)
print("--------------------------------------")
print("Stock al final del dia:", stock_final, " pocions")