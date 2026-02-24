#Versió fent servir match en comptes de if/elif/else
#https://www.w3schools.com/python/python_match.asp

dia = input("Introdueix el nom del dia:")

match dia:
  case "Dilluns":
    print("Traducció: 1")
  case "Dimarts":
    print("Traducció: 2")
  case "Dimecres":
    print("Traducció: 3")
  case "Dijous":
    print("Traducció: 4")
  case "Divendres":
    print("Traducció: 5")
  case "Dissabte":
    print("Traducció: 6")
  case "Diumenge":
    print("Traducció: 7")
  case _:
    print("No sé quin dia es aquest")