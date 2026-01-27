# Replicació de sistemes heterogenis

## 0. Preparació de l'escenari

2 màquines Ubuntu Server 24.04:

- `servidor-mysql` amb la versió més recent de MySQL
- `servidor-psql` amb un PostgreSQL 17 o 18


## 1. Enunciat

>[!IMPORTANT]
>Es necessari documentar tot el procés com un tutorial, tant per per vosaltres per tenir un recurs de referència com per suport per altres exercicis lliurables.

### Primera Part: Preparació

Es farà servir la màquina `servidor-mysql` per a migrar les dades de la base de dades `employees` cap a la màquina `servidor-psql`.

Dins la màquina `servidor-mysql` cal que instal·leu l’aplicació `pgloader`, però tingueu en compte el següent:

- La versió dels repositoris (3.6.3) no és compatible amb la codificació de caràcters que estim fent servir a MySQL v8,necessitem la versió 3.6.7 o superior.

- Cal descarregar l’última versió estable del repositori GitHub i compilar-la: https://github.com/dimitri/pgloader
- Un cop compilada, s’ha de fer servir aquesta versió (i no pas la dels repositoris) per continuar amb l’exercici. Comprova que estàs fent servir la versió correcta.

A continuació feu el següent:

- Comprova que tens la base de dades `employees` dins `servidor-mysql`, si no fos el cas, l’hauràs de carregar com vas fer a l’exercici anterior.

- S'ha de crear una base de dades `employees` al `servidor-psql`.

- Feu servir pgloader per a migrar les dades de la base de dades `employees` del `servidor-mysql` cap al `servidor-psql`. Us haureu de documentar al respecte i explicar el procés que heu seguit.
  
- Si el pas anterior és correcte, dins el `servidor-psql` s'haurà creat un nou esquema `employees` dins la base de dades `employees`.


## Segona part: replicació principal-secundari

`SymmetricDS` (https://www.symmetricds.org/) és una aplicació open-source que permet mantenir dues bases de dades sincronitzades perquè comparteixin la mateixa informació (replicació). 

Realitza la instal·lació i configuració de l'aplicació dins la màquina virtual `servidor-psql` complint els següents requisits:

S'ha de configurar `SymmetricDS` perquè llegeixi la informació de la base de dades `employees` dins `servidor-mysql` i porti tots els canvis a la base de dades `employees` dins `servidor-psql`.

Qui mana (node principal) és `servidor-mysql`, per tant mai s'han de portar canvis de `servidor-psql` (node secundari) cap a `servidor-mysql`.

Si tens errors durant els processos (batch) revisa les taules `sym_incomming_batch`, `sym_incomming_error` i `sym_outgoing_batch` tant al `servidor-mysql` com al `servidor-psql`. 

Quan es modifica la configuració de `SymmetricsDS`, com per exemple un router (taula `sym_router`), no es modifica la configuració original amb la qual es va activar l’enviament de canvis, però segurament podràs solucionar-ho modificant la informació d’aquestes taules.




## Tercera part: replicació principal-principal

Modifica el procediment anterior perquè tots dos nodes funcionin com a principals, és a dir, els canvis a `servidor-mysql` s’apliquen a `servidor-psql` com passava abans, però ara els canvis a `servidor-psql` també s’apliquen a `servidor-mysql`. 
No cal modificar els nodes, és a dir, pots continuar tenint un `principal` i un `secondary`, però cal que la comunicació dels canvis funcioni de forma bidireccional.


