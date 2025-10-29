# Xifrant amb XOR

## Exercici 1: Vernam

L'algoritme Vernam consisteix en aplicar l'operació XOR a cada bit que forma la representació binària numèrica de cada lletra d'un missatge en clar (és a dir, als valors `A = 0 = 00000`, `B = 1 = 00001`, `C = 2 = 00010`, ...fins `Z = 26 = 11010`) contra una clau formada per la representació binària de lletres (del mateix alfabet que el missatge en clar) i amb una longitud arbitrària (tot i que quan més llarga millor per evitar patrons, ja que si no arriba a la longitud del missatge en clar caldrà anar repetint-la). 

>[!NOTE]
>Cal tenir en compte que si la representació numèrica del resultat d'haver transformat una lletra concreta superés el  límit de 26 lletres de l'alfabet i es vol escriure igualment el missatge xifrat en format alfabètic, caldrà aplicar-li llavors  l'operació mòdul 26 (mod 26) per tal de fixar el resultat per sota d'aquest límit i així poder-li assignar una lletra de l'alfabet.  A https://es.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic i també a l'apartat 1 de http://www.criptored.upm.es/crypt4you/temas/criptografiaclasica/leccion5.html podreu trobar explicada l'operació "mòdul" 

Per exemple, suposem que el missatge en clar és `OAK` i la clau és `SON`. Per tant, el missatge xifrat serà el resultat de `OAK` **XOR** `SON`.

Partint d'aquesta premisa, us demano:
- El resultat `???` del missatge `OAK` xifrat amb la clau `SON`.
- Desxifrar el missatge `???` fent servir la clau `SON` per obtenir el missatge original `OAK`
- Fer el **XOR** entre el missatge original `OAK` i el xifrat `???` per obtenir la clau `SON`
- Fes el mateix amb un missatge i clau inventats per tú.
- Passa el missatge xifrat i la clau a un company per veure si sap obtenir el missatge original


## Exercici 2: Baudot

Busca a internet informació sobre la `taula de Baudot` i fes-la servir com a taula d'equivalencia per convertir lletres en combinacions de 0 i 1.

- Amb aquesta taula, fes el xifrat del missatge `PEPINO` amb la clau `BABA`.
- Despres, fes el desxifrat del resultat amb la clau per obtenir el missatge original.
- Repeteix el procés amb una paraula i una clau inventada per tu.
- Passa el missatge xifrat i la clau a un company per veure si sap obtenir el missatge original


## Exercici 3: Encriptar un text llarg

Ara fes un procés similar per encriptar un text llarg com, per exemple, el següent:

>*En moltes coses precioses ara ens podrem transformar,
travessar l'espai amb un núvol i, així, poder viatjar.
L'aventura comença ara:
anem-la a buscar, anem, anem, anem, anem!
Anirem per mars i muntanyes, i per tot l'univers,
intentant aconseguir la bola d'un drac meravellós,
i, així, la bola del drac,
per fi serà nostra.*

Has de mostrar el resultat després de l'encriptació i tornar a aplicar la clau per obtenir-ne el missatge original.

Pista 1: ni se us acudeixi fer-ho a mà

<details>
<summary><b>Pista 2: exemple de codi en Python, només obrir si us rendiu</b></summary>

```python
#!/usr/bin/env python 
from os import urandom 

def genkey(length): 
    return bytearray(urandom(length))


def vernam(text, key): 
    return bytearray( 
        [ text[i] ^ key[i] 
            for i in range(len(text)) 
        ]) 

plaintext = bytearray('Missatge original', "UTF-8") 
key = genkey(len(plaintext)) 
print('Text pla: ' + str(plaintext)) 

ciphertext = vernam(plaintext, key) 
print('Text xifrat: ' + str(ciphertext)) 

plaintext2 = vernam(ciphertext, key) 
print('Text desxifrat: ' + str(plaintext2))
```

</details>

## Exercici 4: Xifrar una imatge

Descarrega't la imatge `secret.png` disponible a la web del curs. D'aquesta imatge (que si intentes obrir veuràs que no pots perquè no és reconeguda com una imatge vàlida ja que està xifrada) un "ocellet" ens ha dit vàries coses: 

- Que és de tipus `PNG` 
- Que està xifrada mitjançant `XOR` 

Gràcies a la primera informació podem saber quina hauria de ser la seqüència de bytes per la què hauria de començar la imatge desxifrada, que no és una altra que el ["magic number" assignat oficialment al format PNG](http://www.libpng.org/pub/png/spec/iso) . Aquest `magic number` és, concretament `89 50 4e 47 0d 0a 1a 0a` 

>[!NOTE]
>Els "magic numbers" són seqüències de bits estandaritzades que estan integrades dins de tot fitxer (concretament, al seu inici) per identificar el tipus de fitxer del qual es tracta. Aquesta informació és molt més fiable que les extensions dels  fitxers, completament manipulables per l'usuari. Hi ha una llista dels "magic numbers" més habituals [aquí](https://en.wikipedia.org/wiki/List_of_file_signatures) o també [aquí](https://www.garykessler.net/library/file_sigs.html)

Comproba, fent simplement `hexdump -C secret.png`, que el començament del fitxer és `76 af b1 b8 f2 f5 e5 f5` 

>[!NOTE]
>La comanda hexdump mostra el contingut binari "tal qual", sense interpretar, del fitxer que se li indiqui. Per defecte els bytes es mostren horitzontalment, en hexadecimal i agrupats per parelles; a l'esquerra de tot apareix també un nombre  hexadecimal que indica la posició del primer byte (el de més a l'esquerra) de cadascuna de les línies de bytes  mostrades (a mode de comptador de línies). El paràmetre -C serveix per mostrar, a més, una nova columna a la dreta de tot  mostrant l'equivalència en ASCII de cada byte del fitxer, per ordre (i si no, un punt), per si aquesta fos de rellevància. Una  altra comanda similar a `hexdump` que també es troba per defecte en els sistemes Linux és `od` 

Com que sabem que es compleix que ki = xi XOR yi , dels valors anteriors podem deduir que: 

k1 = 89 **XOR** 76

k2 = 50 **XOR** af

k3 = 4e **XOR** b1

k4 = 47 **XOR** b8

k5 = 0d **XOR** f2

... 

Si tenim la sort de què la clau sigui més curta que la longitud del "magic number", podrem esbrinar-la per complet i llavors podrem aplicar l'operació xi = yi XOR ki per desxifrar tota la imatge. El primer que has de fer, per tant, és trobar la clau amb les operacions anteriors. Per fer-ho, torna a usar la calculadora del Gnome (en "mode programació" i, en aquest cas, fent que la representació dels números sigui hexadecimal) i ves fent l'operació XOR per cada byte, un rera l'altre, per anar "descobrint" la clau byte a byte. 

>[!NOTE]
>Com que en aquest cas les operacions **XOR** només afecten a un byte cada cop, també podries fer-les sense utilitzar  la calculadora de Gnome sinó simplement executant la comanda següent per cada parella de bytes xi i yi fins trobar la clau  utilitzada: `echo $(( 0x76 ^ 0x89 ))` És fàcil veure com a la comanda anterior s'indica que estem fent una operació **XOR** -amb l'operand `^`- de dos números escrits en hexadecimal; no obstant, el resultat obtingut vindria donat en decimal. Si volguéssim obtenir-lo en hexadecimal, hauríem de fer servir la comanda printf, la qual ens permet especificar el format  desitjat (mitjançant el modificador `%format`, en aquest cas seria `%X`, així): `printf "%X\n" $(( 0x76 ^ 0x89 ))` 


A partir d'aquí, hauriess d'aplicar l'operació xi = yi XOR ki byte a byte al conjunt de tots els bytes del fitxer xifrat per obtenir la imatge desxifrada. No obstant, en aquest cas la calculadora de Gnome (o la web Cryptii o similars) no la podrem fer servir perquè el problema d'aquestes sol.lucions és que acabem tenint com a resultat una tira de números hexadecimals que representa el contingut de la foto desxifrada, sí, però no el podem guardar en forma de fitxer perquè el copiar-pegar es fa amb la seva representació ASCII i no pas amb el contingut binari subjacent. Per tant, el que haurem de fer és emprar una comanda específicament dissenyada per aplicar l'operació XOR directament sobre el contingut d'un fitxer (obtenint-ne un altre com a resultat), la comanda xor. No obstant, aquesta comanda no està disponible als repositoris oficials de les distribucions importants sinó que hauràs de descarregar el seu codi font i compilar-lo per obtenir l'executable pertinent. En concret, has de descarregar-te el fitxer `xor.c` (disponible a https://github.com/dirtbags/fluffy) des de https://raw.githubusercontent.com/dirtbags/fluffy/master/xor.c i executar la comanda següent per realitzar la compilació: `gcc -o xor.exe xor.c`

>[!NOTE]
>Una comanda similar, però dissenyada per aplicar l'operació XOR a fluxes d'entrada de bits (rebuts per canonada)  en lloc de fitxers és https://github.com/mstrand/xcat 


Utiliza la comanda `xor.exe` obtinguda al pas anterior (consulta a la nota següent, extret de la seva documentació oficial, per veure uns quants exemples d'ús) per obtenir un nou arxiu anomenat `foto.png` que es correspongui a la foto desxifrada i visualitza-la finalment amb un visor de fotos qualsevol. Comprova, a més (fent ara `hexdump -C foto.png` ), que, efectivament i com no podia ser d'una altra manera, el "magic number" d'aquest fitxer es correspon al d'un fitxer de tipus PNG (`89 50 4e 47 0d 0a 1a 0a`)  

>[!NOTE]
>Consider the following example command, where "22" is the key (the value to manipulate the bits with) and the text is either the plaintext or ciphertext that will be manipulated: `echo "hello" | ./xor 22` This should display something like "~szzy" Now try the reverse: `echo "~szzy" | ./xor 22` 
>
>To use the `xor` command over all the content of a file, you should do something like this: `./xor 0x22 < filename.txt` *Take note on the xor program that there is a big difference between `./xor 22 < file.txt` and `./xor 0x22 < file.txt`. The 2nd one is a hex number while the 1st is decimal. You can indicate your value is hex by using the `-x` argument like this: `./xor -x 22 < file.txt`
>
>*You can also have a multi value key which would look like this: `./xor -x 01 a0 22 f5 < file.txt`


Una alternativa a xifrar completament tot un fitxer (com per exemple una imatge) des del seu primer byte a l'últim (tal com vam veure a l'exercici anterior) és xifrar només el que seria el seu contingut efectiu: és a dir, deixar sense xifrar el que seria la capçalera on apareix el "magic number" del fitxer (juntament amb altres possibles metadades addicionals que hi puguin haver) per xifrar només els píxels pròpiament dits (en el cas de les imatges). D'aquesta manera, se seguiria tenint una imatge formalment vàlida (visible per qualsevol visor de fotografies) però mostrant un conjunt de píxels aleatoris sense cap mena de patró ni sentit, semblants a simple soroll. És el que veurem en el proper exercici. 


## Exercici 5: XOR entre imatges

Descarrega't les imatges `lemur.png` i `key.png` disponibles a la web del curs i visualitza-les: veuràs que ambdues semblen soroll, ja que la primera imatge ha sigut xifrada mitjançant l'operació **XOR** (però respectant l'estructura interna del format `PNG` per mantenir-la vàlida) amb una clau que resulta ser la segona imatge, la qual està formada, aquesta sí, per una tira de píxels aleatoris de la mateixa mida que la primera. 

>[!NOTE]
>Aquestes imatges tenen una "profunditat de color" de 24 bits. Això significa que el color de cada píxel d'aquestes  imatges ve definit per 3 bytes, el valor del qual indica respectivament la quantitat del color primari vermell (Red) que tindrà el color final, la quantitat de color primari verd (Green) i la quantitat de color primari blau (Blue). Existeixen altres  profunditats de colors (per exemple, la d'1 bit només permet dos colors -blanc i negre-, la de 2 bits en permet quatre -blanc,  negre, gris clar i gris fosc-, etc). No obstant, cal tenir en compte, però, que aquesta estructura és més aviat lògica: no està  directament implementada així dins del contingut d'un fitxer d'imatge ja que, segons el format que tingui (PNG, JPG, etc),  aquest contingut es trobarà comprimit de determinada manera i no seguirà aquest esquema de 24 bits per pixel. Aquesta és  una raó més, a banda de la que s'explica al següent paràgraf, de per què no es pot fer un **XOR** directament als bytes del  fitxer i ja està per desxifrar-lo. Per saber més detalls, per exemple, de l'estructura interna d'una imatge `PNG`, es pot llegir  l'article https://evanhahn.com/worlds-smallest-png 

¿Com podem executar l'operació **XOR** entre `lemur.png` i `key.png`? Més enllà del fet que ara la clau és tot un fitxer i no una simple tira d'un pocs valors hexadecimals (i per tant, la comanda `xor` emprada a l'exercici anterior no serà adient) hem de tenir en compte que, tal com s'ha comentat, el procediment que utilitzem ha de ser prou "intel·ligent" per distingir les parts de les imatges que no estan xifrades (la capçalera amb els "magic numbers", per exemple) de les que sí; hem de pensar que, per exemple, l'operació XOR entre dos valors iguals dóna 0, així que si l'apliquéssim entre dos fitxers que fossin imatges des del seu començament, afectaríem a les seves dues capçaleres amb el resultat d'obtenir una capçalera plena de zeros (és a dir, un fitxer amb un format irreconeixible). Afortunadament, manipular imatges en general i, en concret, manipular les juntament amb altres imatges (no només aplicant entre elles algoritmes criptogràfics com l'operació **XOR** sinó d'altres com les operacions **AND**, **OR** i moltíssimes més) és senzill si fem servir eines especialitzades en el processament digital de fotografies, com ara [GMIC](https://gmic.eu), [GraphicsMagick](http://www.graphicsmagick.org) o [ImageMagick](https://imagemagick.org), entre altres. 

Instal·la el paquet `gmic` en el teu ordinador i a continuació executa la comanda `gmic lemur.png key.png -blend xor -o fotofinal.png`. ¿Què n'obtens?  

>[!NOTE]
>Tens la referència del paràmetre `-blend` [aquí](https://gmic.eu/reference/blend.html)

¿Què passa si, en canvi, com a valor del paràmetre `-blend` escrius `and`?  

¿I si, tot i fer servir l'operació `xor`, utilitzes una altra imatge com a clau? 

Dedueix, veient el resultat, què fa la comanda següent i en quin sentit es diferencia de la comanda utilitzada a l'apartat anterior: `gmic fotofinal.png xor 123` 

>[!NOTE]
>Tens la referència de l'operador `xor` [aquí](https://gmic.eu/reference/xor.html)

¿Quin resultat obtens de fer, en canvi, `gmic fotofinal.png and 123` ? ¿I `gmic fotofinal.png or 123` ? 

>[!NOTE]
>GraphicsMagick té el paràmetre `-operator` i ImageMagick els paràmetres `-evaluate` i `-fx` que son similars en  funcionalitat als exemples vistos en aquest exercici amb Gmic. D'altra banda, si es vol tenir un control més programàtic de  l'edició d'imatges, es poden fer servir llibreries especialitzades per fer totes aquestes tasques (i més), com ara [OpenCV](https://opencv.org) o [Pillow](https://python-pillow.org), entre moltes altres