# Exercicis de classe 3: Funcions

Exercicis relacionats amb l'us de funcions

[Dcoumentació sobre funcions amb Python](https://www.w3schools.com/python/python_functions.asp)

## Constructor d'emails

Hem de crear un programa que demani a l'usuari 3 dades:
- Nom
- Cognom
- Domini

Amb aquestes 3 dades hem de construir automàticament el seu e-mail.

De moment, no ens preocuparem de si el nom o el cognom porten accents (pero ja ho farem)

Per exemple:

```shell
Nom: Chus
Cognom: Vazquez
Domini: institutmvm.cat
------------------------
e-mail: ChusVazquez@institutmvm.cat
```

**NOTA 1**: El programa demanarà les 3 dades pero la construcció del mail l'haurem de fer a una funcio construir_mail que rebi les 3 dades i ens retorni una cadena de text amb el resultat que mostrarem.

### Solució

```python
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
```

### v2

Ara haurem de garantitzar que el mail resultant sigui sempre en minúscules.
Per exemple:

```shell
Nom: Chus
Cognom: Vazquez
Domini: institutmvm.cat
------------------------
e-mail: chusvazquez@institutmvm.cat
```

**NOTA**: Et pot ser de molta utilitat fer servir la funció [lower()](https://www.w3schools.com/python/ref_string_lower.asp).


### Solució

```python
# Funció per construir el mail
def construir_mail(nom, cognom, domini):

    resultat = nom.lower() + cognom.lower() + "@" + domini.lower()
    # També valdria fer un resultat.lower()

    return resultat

# Programa principal
n = input("nom:")
c = input("cognom:")
d = input("domini:")

#Ara faig servir la meva funció
email = construir_mail(n,c,d)

print("e-mail: ", email)
```

## Exercici 2: Traductor de díes de la setmana v4

Hem començat a fer les pràctiques duals a la Federació Unida de Planetes, al departament de xenolingüistica. Ens han demanat un prototip senzill de traductor entre dues civilitzacions, els **Interians** i els **Stringerians**.

Resulta que els Interians només entenen els díes de la setmana com a **números enters**, mentre que els Stringerians només els entenen com a **cadenes de text**.

Ens han demanat millorar la versió v3 i fer una v4 que faci servir funcions.

### Solució 1

```python
# Funció per Interians
def bloc_interia():
    resultat = ""

    #Interià
    print("Vosté s'ha identificat com a Interià")
    dia = input("Introdueix el nom del dia:")

    match dia:
        case "Dilluns":
            resultat = "Traducció: 1"
        case "Dimarts":
            resultat = "Traducció: 2"
        case "Dimecres":
            resultat = "Traducció: 3"
        case "Dijous":
            resultat = "Traducció: 4"
        case "Divendres":
            resultat = "Traducció: 5"
        case "Dissabte":
            resultat = "Traducció: 6"
        case "Diumenge":
            resultat = "Traducció: 7"
        case _:
            resultat = "No sé quin dia es aquest"

    return resultat

# Funció per Stringerians
def bloc_stringeria():
    resultat = ""

    #Stringerià
    print("Vosté s'ha identificat com a Stringerià")
    num_dia = int(input("Introdueix el dia de la setmana en nº:"))

    if num_dia == 1:
        resultat = "Traducció: Dilluns"
    elif num_dia == 2:
        resultat = "Traducció: Dimarts"
    elif num_dia == 3:
        resultat = "Traducció: Dimecres"
    elif num_dia == 4:
        resultat = "Traducció: Dijous"
    elif num_dia == 5:
        resultat = "Traducció: Divendres"
    elif num_dia == 6:
        resultat = "Traducció: Dissabte"
    elif num_dia == 7:
        resultat = "Traducció: Diumenge"
    else:
        resultat = "Nº de dia de la setmana incorrecte"

    return resultat


# Programa principal
especie = input("Es vosté Interià (I) o Stringerià (S)?: ")

if especie == "I":
    r = bloc_interia()
elif especie == "S":
    r = bloc_stringeria()
else:
    r = "ERROR: Espècie no reconeguda a la federació"

print(r)
```

### Solució 2

```python
def bloc_interia():
    #Interià
    print("Vosté s'ha identificat com a Interià")
    dia = input("Introdueix el nom del dia:")
    text_a_mostrar = "..."

    match dia:
        case "Dilluns":
            text_a_mostrar = "Traducció: 1"
        case "Dimarts":
            text_a_mostrar = "Traducció: 2"
        case "Dimecres":
            text_a_mostrar = "Traducció: 3"
        case "Dijous":
            text_a_mostrar = "Traducció: 4"
        case "Divendres":
            text_a_mostrar = "Traducció: 5"
        case "Dissabte":
            text_a_mostrar = "Traducció: 6"
        case "Diumenge":
            text_a_mostrar = "Traducció: 7"
        case _:
            text_a_mostrar = "No sé quin dia es aquest"

    return text_a_mostrar

def bloc_stringeria():
    #Stringerià
    print("Vosté s'ha identificat com a Stringerià")
    num_dia = int(input("Introdueix el dia de la setmana en nº:"))

    if num_dia == 1:
        return "Traducció: Dilluns"
    elif num_dia == 2:
        return "Traducció: Dimarts"
    elif num_dia == 3:
        return "Traducció: Dimecres"
    elif num_dia == 4:
        return "Traducció: Dijous"
    elif num_dia == 5:
        return "Traducció: Divendres"
    elif num_dia == 6:
        return "Traducció: Dissabte"
    elif num_dia == 7:
        return "Traducció: Diumenge"
    else:
        return "Nº de dia de la setmana incorrecte"


# Programa principal
especie = input("Es vosté Interià (I) o Stringerià (S)?: ")
#text_a_mostrar = ""
if especie == "I":
    text_a_mostrar = bloc_interia()
elif especie == "S":
    text_a_mostrar = bloc_stringeria()
else:
    text_a_mostrar = "ERROR: Espècie no reconeguda a la federació"


print("Resultat:", text_a_mostrar)
```
