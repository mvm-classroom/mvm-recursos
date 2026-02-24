especie = input("Es vosté Interià (I) o Stringerià (S)?: ")
if especie == "I":
  #Interià
  print("Vosté s'ha identificat com a Interià")
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

elif especie == "S":
  #Stringerià
  print("Vosté s'ha identificat com a Stringerià")
  num_dia = int(input("Introdueix el dia de la setmana en nº:"))

  if num_dia == 1:
    print("Traducció: Dilluns")
  elif num_dia == 2:
    print("Traducció: Dimarts")
  elif num_dia == 3:
    print("Traducció: Dimecres")
  elif num_dia == 4:
    print("Traducció: Dijous")
  elif num_dia == 5:
    print("Traducció: Divendres")
  elif num_dia == 6:
    print("Traducció: Dissabte")
  elif num_dia == 7:
    print("Traducció: Diumenge")
  else:
    print("Nº de dia de la setmana incorrecte")
else:
  print("ERROR: Espècie no reconeguda a la federació")
  #Error