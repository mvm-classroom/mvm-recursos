stock_inicial = int(input("Stock inicial: "))
stock_restant = stock_inicial

# Compra client 1
quant_cli1 = int(input("Quantitat de pocions a comprar: "))

if (quant_cli1 > stock_restant):
    print("Només li puc vendre", stock_restant, "unitats")
    stock_restant = 0;
else:
    stock_restant = stock_restant - quant_cli1
    print("S'han comprat", quant_cli1, "unitats")

# Compra client 2
if (stock_restant > 0):
    quant_cli2 = int(input("Quantitat de pocions a comprar: "))

    if (quant_cli2 > stock_restant):
        print("Només li puc vendre", stock_restant, "unitats")
        stock_restant = 0;
    else:
        stock_restant = stock_restant - quant_cli2
        print("S'han comprat", quant_cli2, "unitats")
else:
    print("Pocions exhaurides, torni demà")

# Compra client 3
if (stock_restant > 0):
    quant_cli2 = int(input("Quantitat de pocions a comprar: "))

    if (quant_cli2 > stock_restant):
        print("Només li puc vendre", stock_restant, "unitats")
        stock_restant = 0;
    else:
        stock_restant = stock_restant - quant_cli2
        print("S'han comprat", quant_cli2, "unitats")
else:
    print("Pocions exhaurides, torni demà")