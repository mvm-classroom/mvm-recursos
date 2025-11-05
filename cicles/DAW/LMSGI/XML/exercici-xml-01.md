# Exercicis XML 1: Estructura bàsica

## Exercici 1
Genera un document XML partint de les necessitats que observis al següent enunciat:

>[!NOTE]
>La nostra empresa s’ha de comunicar amb un proveïdor per tal de que ens envii la informació referent als productes que ens pot vendre i, com que nosaltres som el client, estem en posició de determinar quin serà el format del document XML que ens haurem d’intercanviar. Bàsicament, aquest document ha de permetre que rebem informació dels productes com el nom, el codi intern del producte, una breu descripció, quin preu de compra té i quin és el preu de venda recomanat. A més, en cas que el producte estigui en oferta, hem de poder identificar el nom de la oferta, el seu codi i el percentatge de descompte que cal aplicar sobre el preu. 

Quan generis el document XML, emplena’l amb informació inventada de tal manera que contingui informació de 3 productes diferents, un d’ells amb oferta aplicada.

## Exercici 2
Genera el document XML corresponent a [aquest arbre](arbre-xml-institut.svg)


## Exercici 3
Dibuixa l’arbre corresponent al següent XML i, si en trobes algun error, corregeix-lo:

```xml
<?xml version=1.0 decode=’utf-8’ ?>
<languages>
    <lang name=”HTML” version=”5” difficulty average=”easy” >           
    <lang>
       <name>CSS</name>
       <version>3</version>
      <difficulty average>medium</difficulty average>
    </lang>
<\languages>
```
Un cop hagis acabat contesta a les següents preguntes: 

1. Donat un codi XML que no té errors, obtindrem sempre el mateix arbre? Justifica la resposta posant algun exemple.
2. Donat un codi XML que té errors, obtindrem sempre el mateix arbre? Justifica la resposta posant algun exemple.
3. Argumenta per quin motiu és tan important que un llenguatge com XML tingui unes regles estrictes que no admeten errors per a funcionar.

