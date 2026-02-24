operacio = input("Introdueix operació:")
n1 = float(input("Introdueix n1:"))
n2 = float(input("Introdueix n2:"))
resultat = 0

match operacio:
    case "+":
        print("Ha seleccionat sumar")
        resultat = n1 + n2
    case "-":
        print("Ha seleccionat restar")
        resultat = n1 - n2
    case "*":
        print("Ha seleccionat multiplicar")
        resultat = n1 * n2
    case "/":
        print("Ha seleccionat dividir")
        resultat = n1 / n2

print("El resultat es:", resultat)