# Bateria d'exercicis per practicar `INSERT` a PostgreSQL

A continuació tens una bateria progressiva d'exercicis basats en l'esquema de `dunder_mifflin`. 
La idea és que els resolguis **en ordre**, ja que les claus foranes obliguen a inserir primer les taules "pare" i després les "filles".


>[!NOTE]
>Quan us demani fer un `SELECT`, com que encara no l'hem vist, podeu fer servir el DBeaver per veure el contingut que aneu inserint a cada taula.
>Pero quan repasseu aquests exercicis per l'examen, practiqueu amb el `SELECT`, el vostre jo del futur us ho agrairà

>[!WARNING]
>Algunes sentències que provem poden donar errors o tenir algun comportament extrany, llegiu el que diu l'error i pensem què està passant

---

## Nivell 0 — Escalfament

Abans de començar, respon:

1. Podem inserir un `EMPLEAT` amb `departament_id = 1` si encara no existeix cap departament amb `id = 1`? Per què?
2. Per què a `DEPARTAMENT`, `EMPLEAT`, `CLIENT`, `COMANDA` i `PRODUCTE` **no** cal indicar la columna `id` al `INSERT`? Què passa si ho intentes?
3. Quines taules necessiten que existeixin files prèvies en altres taules abans de poder inserir-hi dades?

---

## Nivell 1 — Inserció bàsica

### Exercici 1.1
Insereix un departament anomenat `'Vendes'`.

### Exercici 1.2
Insereix dos departaments més en una sola sentència: `'Comptabilitat'` i `'Recursos Humans'`.

### Exercici 1.3
Insereix un empleat anomenat `'Michael'` cognom `'Scott'` al departament de Vendes (suposant que és l'`id = 1`).

### Exercici 1.4
Insereix un producte anomenat `'Grapadora'` amb preu unitari `12.50`.

---

## Nivell 2 — Inserció amb diverses files

### Exercici 2.1
Insereix d'una sola vegada tres empleats al departament de Vendes:
- `'Dwight'` `'Schrute'`
- `'Jim'` `'Halpert'`
- `'Phyllis'` `'Vance'`

### Exercici 2.2
Insereix tres productes d'una sola sentència:

| NomProducte | PreuUnitari |
|---|---|
| Paper A4 | 4.99 |
| Bolígraf blau | 0.85 |
| Cadira d'oficina | 89.00 |

### Exercici 2.3
Insereix dos clients assignats al venedor `'Dwight'` (esbrina primer el seu `id` amb un `SELECT`):
- `'Dunder Mifflin Inc.'`
- `'Sabre Corp.'`

---

## Nivell 3 — Ús de `RETURNING`

### Exercici 3.1
Insereix un client nou anomenat `'Vance Refrigeration'` assignat a `'Phyllis'` i fes que la sentència **retorni l'`id`** generat.

### Exercici 3.2
Insereix un producte `'Motxilla'` amb preu `25.00` i retorna **totes les columnes** de la fila inserida.

### Exercici 3.3
Insereix un departament `'Magatzem'` i retorna només el seu `id`. Després, amb aquest `id`, insereix un empleat `'Darryl'` `'Philbin'` en aquest departament.

---

## Nivell 4 — Valors per defecte i columnes opcionals

### Exercici 4.1
Insereix una comanda **sense especificar la data**, indicant només el client. Comprova amb un `SELECT` que la data s'ha omplert automàticament amb `now()`.

### Exercici 4.2
Insereix una línia de comanda amb `Quantitat` **no especificada**. Quin valor agafa? Comprova-ho.

### Exercici 4.3
Insereix una línia de comanda amb `Quantitat = 5` per a un producte i una comanda que existeixin.

---

## Nivell 5 — Entenent els errors

Per a cada cas, **escriu la sentència que provoca l'error**, executa-la i explica el missatge que retorna PostgreSQL:

### Exercici 5.1
Intenta inserir un `EMPLEAT` amb `departament_id = 999` (inexistent).

### Exercici 5.2
Intenta inserir un `CLIENT` amb `empleat_venedor_id = 999`.

### Exercici 5.3
Intenta inserir un `DEPARTAMENT` amb `nom = NULL`.

### Exercici 5.4
Intenta inserir un `EMPLEAT` **especificant manualment** `id = 100`.

### Exercici 5.5
Intenta inserir una `LINIA_COMANDA` amb una combinació `(Id_Comanda, Id_Producte)` que **ja existeixi**.

---

## Nivell 6 — Escenari complet

Construeix un escenari coherent de principi a fi amb `INSERT`s:

1. Crea un departament nou `'Màrqueting'`.
2. Insereix-hi un empleat `'Ryan'` `'Howard'`.
3. Insereix un client `'Blue Cross'` assignat a aquest empleat.
4. Insereix una comanda per a aquest client (sense data explícita).
5. Insereix **tres línies de comanda** per a aquesta comanda amb productes diferents i quantitats diferents.
6. Fes un `SELECT` final que mostri: nom del client, data de la comanda, nom del producte i quantitat.

>[!NOTE]
> **Pista:** necessitaràs `RETURNING id` als `INSERT`s intermedis, o bé fer `SELECT` per recuperar els `id`s generats.
