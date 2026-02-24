operacio = input("Introdueix operació: ")
#if operacio != "+" and operacio != "-" and operacio != "*" and operacio != "/":
if operacio not in "+-*/":
    #Error
    print("Error: Operació incorrecta")
else:
    #Operació be, demanem els numeros
    print("Operació correcta")
    n1 = input("Introdueix n1: ")
    n2 = input("Introdueix n2: ")

    if not(n1.isnumeric()) or not(n2.isnumeric()):
        #Error
        print("Error: només podem operar amb números")
    else:
        #Números correctes podem continuar
        n1 = float(n1)
        n2 = float(n2)
        print("Numeros correctes")

        resultat = 0
        #En aquest punt bifurquem el nostre codi en les 4 possibilitats
        match operacio:
            case "+":
                resultat = n1 + n2
            case "-":
                resultat = n1 - n2
            case "*":
                resultat = n1 * n2
            case "/":
                resultat = n1 / n2

        #Hora de mostrar el resultat
        print(n1, operacio, n2, "=", resultat)