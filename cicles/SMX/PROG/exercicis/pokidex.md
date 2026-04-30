# Exercici final: POKIDEX

## Enunciat
Ens demanen crear una `pokidex` que es com una mena d'agenda per guardar dades d'unes criatures anomendades `pokis` que no tenen res a veure amb cap propietat intelectual existent. Qualsevol semblança es pura coincidència.


## Entitats
Tindrem una llista d'elements `poki` anomenada `pokidex` que inicialitzarem amb 3 elements

Cada `poki` consta de una sèrie de dades que volem emmagatzemar:
- nom
- número
- tipus
- vida
- atac
- habilitats

La dada `habilitats` serà una llista d'elements `habilitat` que consta de:
- nom
- cost
- descripció

> [!TIP]
> Per gestionar la `pokidex` i les entitats que conté podeu fer servir les estructures que cregueu adients: 
> 
> -una llista de diccionaris 
> 
> -un diccionari de diccionaris 
> 
> -una llista d'objectes 

Penseu o proveu quina combinació us pot anar millor per fer totes les accions que demano (afegir, cercar, eliminar...)

## Opcions del programa
El programa ha d'oferir les següents opcions:
- Inserir: Ens demanarà totes les dades necesàries d'un `poki` i l'afegirà a la llista
- Llistar: Ens llistarà tots els `poki` que tinguem a la `pokidex`
- Cercar: Ens demanarà el nom d'un `poki` per cercar-lo a la `pokidex`. Si el troba, el mostrarà. Si no, ens dirà que no s'ha trobat.
- Eliminar: Demanem un nom, el cerquem a la llista i, si existeix, l'eliminem
- Sortir: Finalitza el programa

Sempre que l'usuari trii una opció, s'executarà l'acció correponent i tornarem a mostrar el menú d'opcions per tornar a demanar què fer.
Si l'usuari tria l'opció `Sortir`, finalitzarem el programa.

> [!NOTE]
> Per escollir les opcions podeu fer servir números (1-5), les inicials de les opcions ([I]nserir, [L]listar, [C]ercar...) o qualsevol altre métode que tingui sentit per l'usuari


## Funcions
El vostre codi hauria d'estar estructurat en funcions, fent servir com a mínim:

### inicitalitzar(pokidex)
Inicialitza la llista afegint 3 elements (els creem fixes amb els valors que decidim)

### mostrar_menu()
Mostra el menú d'opcions

### demanar_opcio()
Demana l'opció a l'usuari i s'assegura de que es tria una opció correcta. Si l'opció triada es incorrecta, li fem saber a l'usuari i tornem a demanar.
Retorna l'opció escollida.

### demanar_dades()
Demana totes les dades necessàries per crear un `poki`
Retorna un `poki`

### inserir_poki(pokidex)
Insereix un `poki` a la `pokidex`. Li podem passar com un paràmetre extra o podem cridar a la funció `demanar_dades()` dins d'aquesta funció.
No retorna res.
Mostrar un missatge de l'estil "S'ha afegit un Barbasoul"
BONUS: Abans d'afegir, cercar per nom per si l'element ja existeix (fent servir la funció `cercar(pokidex, nom)`)

### mostrar_poki(poki)
Fem els prints necessaris per mostrar tota l'informació d'un `poki`

El disseny d'impressió no es estricte però uns exemples d'impressió d'un `poki` serien:

```text
-------------------------------------------------------------------
Nom  : Barbasoul
Nº   : 003
Tipus: Planta
Vida : 120
Atac : 100
Habilitats:
- Impactfuet: Ataca tres vegades
- Mastegot verinós: Atac que pot enverinar l'objectiu
- Fotosíntesi: Regenera 10 punts de vida per torn durant 5 torns
-------------------------------------------------------------------
```

```text
-------------------------------------------------------------------
Barbasoul                                                    Nº 003
-------------------------------------------------------------------
Tipus: Planta
Vida : 120
Atac : 100
Habilitats:
- Impactfuet: Ataca tres vegades
- Mastegot verinós: Atac que pot enverinar l'objectiu
- Fotosíntesi: Regenera 10 punts de vida per torn durant 5 torns
-------------------------------------------------------------------
```
BONUS: Si feu servir colors per millorar la llegibilitat (per exemple, en funció del tipus)

### llistar(pokidex)
Recorre la llista mostrant tots els elements
Per mostrar cada element cridarem la funció `mostrar_poki(poki)`

### cercar(pokidex, nom)
Cerquem un element pel nom i, si existeix, el mostrem fent servir la funció `mostrar_poki(poki)`

### eliminar(pokidex, nom)
Cerquem un element pel nom i, si existeix, l'eliminem

## Programa principal
Feu tota la feina que pogueu dins les funcions i feu servir el programa principal només per "vertebrar" les crides a les vostres funcions

## Comentaris
Feu servir comentaris per explicar i justificar el vostre codi

> [!CAUTION]
> No feu servir codi que no sigui vostre, que no entengueu o que no sabeu explicar. Si no sabeu defensar el que feu, **la nota serà un 0**
