# Exercicis SQL: Introducció a la clàusula `JOIN`

## La clàusula `JOIN`
Fins ara hem treballat amb una sola taula. Però la potència de les bases de dades relacionals resideix en relacionar dades de diferents taules. Per fer això utilitzem la clàusula **`JOIN`**.

L'estructura bàsica és:
```sql
SELECT t1.columna, t2.columna
FROM taula1 t1
JOIN taula2 t2 ON t1.id = t2.foreign_id;
```

o, amb un exemple més concret, seguint amb la base de dades `pagila` que ja coneixem:

```sql
SELECT f.title, l.name
FROM film f
JOIN language l ON f.language_id = l.language_id;
```
Aqui estem unint (`JOIN`) les taules film i language, fent servir com a nexe d'unió el camp `language_id`.
Fixeu-vos que el camp `language_id` es:
- La PRIMARY_KEY (`PK`) de la taula `language`
- Una FOREIGN_KEY (`FK`) que existeix a la taula `film` per fer referencia al seu registre relacionat a la taula `language`

Fixeu-vos també que al SELECT, a l'hora d'especificar els camps que volem mostrar, ho fem indicant el prefixe de la taula per saber de quina taula volem cada dada (pensem que ara podem fer joins amb moltes taules i alguns noms de columnes poden estar repetits):
- `f.title` vol dir que de la taula `f` (l'àlies que hem assignat per `film`) volem el camp `title`
- `l.name` vol dir que de la taula `l` (l'àlies que hem assignat per `language`) volem el camp `name`

Ens donaria un resultat semblant a aquest (però amb més registres)

```text
title            | name
-----------------+----------
ACADEMY DINOSAUR | English
ACE GOLDFINGER   | English    
```

## Tipus de `JOIN`

Un **JOIN** serveix per combinar columnes de dues (o més) taules basant-se en una columna relacionada entre elles. La diferència principal entre els tipus de JOIN és com tracten les files que **no tenen coincidència** a l'altra taula.


### `INNER JOIN` (La intersecció)
Mostra **només** les files quan hi ha una coincidència a **totes dues** taules. Si una fila de la taula A no té relació amb la taula B, no surt.

#### Exemple:

>Volem veure els clients i els seus pagaments. Si un client no ha fet cap pagament (hipotèticament), no sortiria a la llista.

```sql
SELECT customer.first_name, payment.amount
FROM customer
INNER JOIN payment ON customer.customer_id = payment.customer_id;
```
Només surten clients que han pagat i pagaments associats a clients

```text
first_name | amount
-----------+--------
MARY       |   2.99
MARY       |   0.99
PETER      |   5.99
```

### `LEFT JOIN` (Tot el de l'esquerra)
Mostra **totes** les files de la taula de l'esquerra (la primera que es menciona al construir la query). Si hi ha coincidència amb la dreta, mostra les dades; si no n'hi ha, mostra `NULL`.

#### Exemple:

>Volem un llistat de **totes les pel·lícules** (`film`, taula esquerra) i veure si tenim còpies a l'inventari (`inventory`, taula dreta).

> Hi ha pel·lícules registrades que potser no tenim físicament a la botiga. Amb un `INNER JOIN` desapareixerien. Amb `LEFT JOIN` surten amb NULL.

```sql
SELECT film.title, inventory.inventory_id
FROM film
LEFT JOIN inventory ON film.film_id = inventory.film_id
WHERE inventory.inventory_id IS NULL; -- Filtre opcional per veure només els casos sense estoc
```

```text
 title             | inventory_id
-------------------+--------------
    ALICE FANTASIA |         NULL  <-- Existeix la pel·li, però no hi ha inventari
    APOLLO TEEN    |         NULL
    ARGONAUTS TOWN |         NULL
```
*Com veus, la pel·lícula es mostra, però la columna d'inventari està buida.*

> [!TIP]
> Prova també el resultat sense afegir el `WHERE`

---

### `RIGHT JOIN` (Tot el de la dreta)
És just el contrari del `LEFT JOIN`. Mostra **totes** les files de la taula de la dreta (la segona que es menciona al construir la query). Si no tenen coincidència amb l'esquerra, mostra `NULL` a les columnes de l'esquerra.

#### Exemple:

> Volem veure **tots els idiomes** (`language`, taula dreta) i quines pel·lícules tenim en aquest idioma (`film`, taula esquerra).
> A Pagila hi ha idiomes com "Italian" o "Japanese" definits, però totes les pel·lícules estan en "English".

```sql
SELECT film.title, language.name
FROM film
RIGHT JOIN language ON film.language_id = language.language_id;
```


```text
title             | name
------------------+----------
ACADEMY DINOSAUR  | English
ACE GOLDFINGER    | English
NULL              | Italian   <-- Tenim l'idioma, però cap pel·lícula associada
NULL              | Japanese
NULL              | Mandarin
```
*Aquí, encara que no hi ha pel·lícules en Mandarí, l'idioma apareix al llistat perquè hem fet un RIGHT JOIN sobre `language`.*

---

## Exercicis proposats

### Nivell 1: Unions directes (2 taules)
> [!NOTE]
> L'objectiu és unir dues taules que tenen una relació directa (Clau Primària - Clau Forana).

#### 1. **Pel·lícules i Idiomes:** 
Selecciona el títol de la pel·lícula (`film.title`) i el nom de l'idioma (`language.name`).

#### 2.  **Ciutats i Països:** 
Selecciona el nom de la ciutat (`city.city`) i el nom del país al qual pertany (`country.country`).

#### 3.  **Adreces i Ciutats:** 
Selecciona l'adreça (`address.address`) i el nom de la ciutat (`city.city`) de la taula `address`.

#### 4.  **Clients i Adreces:** 
Selecciona el nom i cognom del client (`customer`) i la seva adreça (`address`).

#### 5.  **Empleats i Adreces:** 
Selecciona el nom de l'empleat (`staff`) i la seva adreça.

#### 6.  **Pel·lícules en anglès:** 
Mostra els títols de les pel·lícules, però només aquelles on l'idioma sigui 'English'.

#### 7.  **Pagaments i Clients:** 
Mostra la data del pagament (`payment_date`) i l'import (`amount`), juntament amb el nom complet del client que l'ha fet.

#### 8.  **Inventari i Pel·lícules:** 
Mostra l'ID de l'inventari (`inventory_id`) i el títol de la pel·lícula que correspon a aquest ítem.

#### 9.  **Lloguers i Empleats:** 
Mostra l'ID del lloguer (`rental_id`) i el nom de l'empleat (`staff`) que va processar el lloguer.

#### 10. **Clients i Botigues:** 
Mostra el nom del client i l'ID de la botiga (`store_id`) a la qual està assignat, però assegura't de mostrar l'adreça de la botiga (necessitaràs unir `customer` i `store`, i després `store` i `address`).

##### *Versió 1*: Mostra només la relació del client amb la botiga

##### *Versió 2*: Mostra client, botiga i adreça

##### *Versió 3*: Mostra client, botiga, adreça del client i adreça de la botiga

### Nivell 2: Camins de 3 taules o taules intermèdies
> [!NOTE]
> Aquí sovint necessitem una taula "pont" (com film_actor) o saltar de A a B i de B a C.

#### 11. **Pel·lícules i Categories:** 
Mostra el títol de la pel·lícula i el nom de la seva categoria (`category.name`). *Pista: `film` -> `film_category` -> `category`.*

#### 12. **Pel·lícules i Actors:** 
Mostra el títol de la pel·lícula i el nom i cognom dels actors que hi surten. *Pista: `film` -> `film_actor` -> `actor`.*

#### 13. **Clients i Ciutats:** 
Volem saber de quina ciutat és cada client. Mostra el nom del client i la ciutat. *Pista: `customer` -> `address` -> `city`.*

#### 14. **Inventari, Pel·lícula i Botiga:** 
Mostra l'ID de l'inventari, el títol de la pel·lícula i l'ID de la botiga on es troba.

#### 15. **Lloguers detallats (Client):** 
Mostra la data de lloguer, el títol de la pel·lícula llogada i el nom del client. *Pista: `rental` -> `inventory` -> `film` (per al títol) i `rental` -> `customer` (per al client).*

### Nivell 3: Múltiples Joins i Lògica de Negoci

> [!NOTE]
> Combinem 4+ taules o afegim filtres específics (`WHERE`) sobre les taules unides.

#### 16. **Clients i Països:** 
Volem un llistat dels clients indicant el seu país de residència. Mostra: Nom Client, País.

#### 17. **Actors de "ACADEMY DINOSAUR":** 
Mostra només els noms dels actors que han actuat a la pel·lícula titulada "ACADEMY DINOSAUR".

#### 18. **Qui ha llogat què? (Filtre per nom):** 
Mostra els títols de les pel·lícules que ha llogat la clienta 'MARY SMITH'.

#### 19. **Pagaments detallats:** 
Mostra la data del pagament, l'import, el nom del client i el nom de l'empleat que ha cobrat.

#### 20. **Informació completa de la Botiga:** 
Mostra l'ID de la botiga, la ciutat on està i el país.

### Nivell 4: `LEFT JOIN` i `RIGHT JOIN`

#### 21. **Totes les películes i si son a l'inventari (LEFT JOIN)**
Volem una llista de **totes** les pel·lícules i, si en tenim còpies, el seu ID d'inventari. Si no en tenim, volem que surti la pel·lícula igualment amb un NULL.

#### 22. **Tots els idiomes i les seves pel·lícules (RIGHT JOIN).**
Volem llistar **tots** els idiomes disponibles a la base de dades i el títol de les pel·lícules associades. Fes servir `RIGHT JOIN` amb la taula d'idiomes a la dreta. Si per un idioma no hi han pel.lícules, s'ha de mostrar l'idioma i un NULL

#### 23. **Actors i les seves pel·lícules (LEFT JOIN).**
Llista tots els actors i l'ID de les pel·lícules que han fet. Encara que a Pagila tots els actors han treballat, aquesta consulta és la manera correcta de verificar si tenim algun actor "a l'atur".

#### 24. **Inventari i Lloguers (LEFT JOIN).**
Mostra tot l'inventari (cintes físiques) i l'ID del lloguer si està llogada. Volem veure totes les cintes, fins i tot les que mai s'han llogat (o l'historial de lloguer).

#### 25. **Comparativa: Pel·lícules sense inventari (RIGHT JOIN).**
Repeteix l'exercici 1 (pel·lícules i inventari) però utilitzant `RIGHT JOIN`. Posa `inventory` a l'esquerra i `film` a la dreta.

#### 26. **Troba les pel·lícules que NO tenim a l'inventari.**
Utilitza un `LEFT JOIN` i filtra amb `WHERE` per mostrar només els títols que tenen l'ID d'inventari a NULL.

#### 27. **Compta quantes pel·lícules ens falten a l'inventari.**
En lloc de llistar els títols, volem saber la xifra total de pel·lícules que consten a la base de dades però no tenim físicament.

#### 28. **Troba idiomes sense pel·lícules (RIGHT JOIN + WHERE).**
Mostra els noms dels idiomes que no tenen cap pel·lícula associada a la base de dades.

#### 29. **Suma del cost de reemplaçament de les pel·lícules "perdudes".**
Volem saber quants diners representaria (segons `replacement_cost`) si haguéssim de comprar una còpia de totes les pel·lícules que actualment no tenim a l'inventari.

#### 30. **Llistar pel·lícules 'G' que NO estan a l'inventari (Filtre compost).**
Volem títols de pel·lícules que siguin aptes per a tots els públics (`rating` = 'G') **I** que, a més a més, no tinguem a l'inventari.

### Nivell 5: Expressions

#### 31. **Expressió de cadena: Llistar el nom complet dels actors en una unica columna**

Volem el nom complet dels actors (`first_name` i `last_name`) en una unica columna que es digui "Nom actor"

#### 32. **Expressió aritmética: Llistar la duració de les películes en hores**

Volem mostrar la duració de les películes en hores en comptes de en minuts. El resultat ha de mostrar-se amb una precissió de 2 decimals i la columna s'ha de dir "Hores duració"

#### 33. **Expressió condicional: Etiquetes de preu**

Volem mostrar una nova columna, anomenada "Etiqueta preu", que ens mostri:
- Si el lloguer es inferior a 1.00$: `Ofertón`
- Si el lloguer està entre 1.00$ i 3.00$: `Preu amic`
- Si el lloguer es superior a 3.00$: `Premium`
