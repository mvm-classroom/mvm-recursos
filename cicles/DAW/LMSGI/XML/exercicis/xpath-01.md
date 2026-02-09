# Exercicis amb XPath

## Preparació

Per aquests exercicis farem servir l'eina `BaseX`, que ens permet treballar amb bases de dades `XML`.

Instal.la `BaseX` a qualsevol màquina virtual (ja sigui a `VirtualBox` o a `IsardVDI`)

Com soleu treballar amb Ubuntu, ho podeu instal.lar de la següent manera:
```shell
sudo apt install basex -y
```

Un cop oberta l'eina, hauràs de crear una nova base de dades i carregar el fitxer [mondial_geo_accidents.xml](../recursos/mondial_geo_accidents.xml)

## Exercicis

Fent servir XPath, obtenir la següent informació:

El nom de tots els mars:


El nom del segon mar:


El nom de l'avantpenúltim mar:


El nom del mar que té un ID igual a "sea-Asowsches_Meer":


El nom del mar que té una profunditat igual a 5267:


El nom del mar que té un ID igual a "sea-Asowsches_Meer" o bé que té una profunditat igual a 5267 sense fer servir pipes:


El nom del mar que té un ID igual a "sea-Asowsches_Meer" o bé que té una profunditat igual a 5267 fent servir pipes:

 
El nom del mar que té un ID igual a "sea-Asowsches_Meer" i també té una profunditat igual a 5267 sense fer servir pipes:


El nom del mar que té un ID igual a "sea-Asowsches_Meer" i també té una profunditat igual a 100 sense fer servir pipes:


El nom del riu situat a 1465 metres d'altura (elevació):
