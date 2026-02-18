# Exercicis amb XPath

## Preparació

Per aquests exercicis farem servir l'eina `BaseX`, que ens permet treballar amb bases de dades `XML`.

Instala `BaseX` a qualsevol màquina virtual (ja sigui a `VirtualBox` o a `IsardVDI`)

Com soleu treballar amb Ubuntu, ho podeu instal.lar de la següent manera:
```shell
sudo apt install basex -y
```

Un cop oberta l'eina, hauràs de crear una nova base de dades i carregar el fitxer [mondial_geo_accidents.xml](../recursos/mondial_geo_accidents.xml)

## Exercicis

Fent servir XPath, obtenir la següent informació:

El nom de tots els mars:

```xpath
//sea/name/text()
```

El nom del segon mar:

```xpath
//sea[2]/name/text()
```

El nom de l'avantpenúltim mar:

```xpath
//sea[last()-2]/name/text()
```

El nom del mar que té un ID igual a "sea-Asowsches_Meer":

```xpath
//sea[@id="sea-Asowsches_Meer"]/name/text()
```

El nom del mar que té una profunditat igual a 5267:

```xpath
//sea[depth=5267]/name/text()
```

El nom del mar que té un ID igual a "sea-Asowsches_Meer" o bé que té una profunditat igual a 5267 sense fer servir pipes:

```xpath
//sea[@id="sea-Asowsches_Meer" or depth=5267]/name/text()
```

El nom del mar que té un ID igual a "sea-Asowsches_Meer" o bé que té una profunditat igual a 5267 fent servir pipes:

```xpath
//sea[@id="sea-Asowsches_Meer"]/name/text() | //sea[depth=5267]/name/text()
```
 
El nom del mar que té un ID igual a "sea-Asowsches_Meer" i també té una profunditat igual a 5267 sense fer servir pipes:

```xpath
//sea[@id="sea-Asowsches_Meer" and depth=5267]/name/text()
```

El nom del mar que té un ID igual a "sea-Asowsches_Meer" i també té una profunditat igual a 100 sense fer servir pipes:

```xpath
//sea[@id="sea-Asowsches_Meer" and depth=100]/name/text()
```

El nom del riu situat a 1465 metres d'altura (elevació):

```xpath
//river/source[elevation=1465]/../name/text()
```
