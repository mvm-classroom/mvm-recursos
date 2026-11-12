# Cheatsheet PostgreSQL

## Connexió a bases de dades amb `psql`

### Conectar a base de dades local en mode `Peer`
```shell
sudo -u postgres psql
```
### Conectar a base de dades local en mode `Host`
```shell
psql -h localhost -U postgres
```
### Conectar a base de remota
```shell
psql -h ip.de.equip.servidor -U postgres
```

>[!NOTE]
>En aquest cas estem fent servir sempre l'usuari `postgres` per defecte, pero tingueu en compte que `-u` i `-U` precedeixen el nom d'usuari

>[!CAUTION]
>Si has intentat connectar des del client i et trobes erros de connexió o connexió refusada, aquí tens un parell de correccións:

>[!TIP]
>Per que el nostre servei escolti peticions remotes, ho heu d'habilitar amb l'opció `listen_addresses` al fitxer `/etc/postgresql/18/main/postgresql.conf`
>
>L'opció la trobarem comentada amb el valor per defecte
>``` ini
>#listen_addresses = 'localhost'
>```
>
>Aixó vol dir que només està escoltant 'localhost' i que no podrem rebre cap petició remota
>
>Podem canviar-ho descomentant la línia i indicant les adreces que volem escoltar, si volem escoltar totes farem servir un `*`
>```ini
>listen_addresses = '*'
>```


>[!WARNING]
>Pero amb aixó no serà suficient, hem de tocar un altre fitxer

>[!TIP]
>Encara que el servei **escolta** adreces remotes, falta afinar una mica més la seguretat.
>Podem indicar quin tipus d'autenticació fem servir segons el métode de connexió, l'usuari, la base de dades, l'adreça remota...
>Tot aixó ho podem definir al fitxer `/etc/postgresql/18/main/pg_hba.conf`
>
>
>Per exemple, una manera molt insegura pero que ens podem permetre en aquest entorn de proves seria afegir:
>
>```c
># Permetre connexions des de qualsevol IPv4 remota (no recomanable a producció)
>host    all             all             0.0.0.0/0               scram-sha-256
>
># Permetre connexions des de qualsevol IPv6 remota (no recomanable a producció)
>host    all             all             ::/0                    scram-sha-256
>```
>

>[!TIP]
>Reiniciem i comprovem l'status
>```shell
>sudo systemctl restart postgresql
>
>systemctl status postgresql
>```
>
>Ara ja hauriem de poder connectar sense cap problema.

## Algunes comandes d'utilitat a `psql`

|Comanda|Descripció|
|---|---|
|`\l`|Llistar totes les bases de dades|
|`\c nom_bdd`|Connectar a una base de dades|
|`\dt`|Llistar les taules de la base de dades|
|`\dt+`|Llistar les taules de la base de dades amb més detall|
|`\d nom_taula`|Mostrar descripció de la taula|
|`\du`|Llistar usuaris/rols|
|`\dn`|Llistar esquemes|
|`\i fitxer.sql`|Executar un fitxer|
|`\o fitxer.txt`|Redirigir la sortida a un fitxer|
|`\h`|Ajuda de comandes `SQL`|
|`\?`|Ajuda de comandes `psql`|
|`\q` o `exit`|Sortir de `psql`|

## Exemple de càrrega de les dades
Connectat al servidor i, fent servir el terminal, fes el necessari per carregar les dades de [`dvdrental.tar`](https://github.com/mvm-classroom/mvm-recursos/raw/main/cicles/ASIX/ASGBD/Recursos/dvdrental.tar). Potser t'interessa fer una ullada a l'eina [`pg_restore`](https://www.postgresql.org/docs/current/app-pgrestore.html)

### Abans de res, hauriem de crear la base de dades.
Connectem al SGBD com l'usuari `postgres`
```shell
psql -h localhost -U postgres
```
i un cop a dins, creem la base de dades
```sql
CREATE DATABASE dvdrental OWNER postgres;
```
### Descarregar el fitxer amb la base de dades
Podem descarregar el fitxer `dvdrental.tar` fent

```shell
wget https://github.com/mvm-classroom/mvm-recursos/raw/main/cicles/ASIX/ASGBD/Recursos/dvdrental.tar
```
### Revisar i importar el fitxer amb la base de dades
Per tafanejar el fitxer `dvdrental.tar` abans d'importarlo a cegues
```shell
pg_restore --list dvdrental.tar
```

Un exemple de com restaurar el fitxer `dvdrental.tar` a la base de dades `dvdrental` que hem creat prèviament

```shell
pg_restore -h localhost -U postgres -d dvdrental dvdrental.tar
```

## Restaurar base de dades de prova `pagila`
En aquest cas farem servir la base de dades de prova anomenada `pagila` que podem trobar [aquí](https://github.com/devrimgunduz/pagila)

Podem descarregar tot el repositori fent servir
```shell
git clone https://github.com/devrimgunduz/pagila.git
```
i accedim al directori que ens ha creat
```shell
cd pagila
```
Abans de restaurar el contingut, hem de crear la base de dades al nostre SGBD
```shell
isard@ubuntu-server:~$ psql -h localhost -U postgres
Contraseña para usuario postgres:
psql (18.0 (Ubuntu 18.0-1.pgdg24.04+3))
Conexión SSL (protocolo: TLSv1.3, cifrado: TLS_AES_256_GCM_SHA384, compresión: desactivado, ALPN: postgresql)
Digite «help» para obtener ayuda.

postgres=# CREATE DATABASE pagila;
CREATE DATABASE
postgres=# exit
```
Farem servir l'opció `-f` de `psql` per restaurar un parell de fitxers del repositori descarregat:

```shell
psql -h localhost -U postgres -d pagila -f pagila-schema.sql
```
```shell
psql -h localhost -U postgres -d pagila -f pagila-insert-data.sql
```
Un cop finalitzat el procés podem connectar via `psql` i comprovar que la base de dades `pagila` conté certa estructura i dades.


## Tipus de dades
Podeu consultar, de manera molt més extensa i detallada, tota la documentació sobre tipus de dades [a aquest capítol de la documentació de PostreSQL 18.](https://www.postgresql.org/docs/current/datatype.html)

### Tipus numérics

|Nom|Tamany|Descripció|Rang de valors|
|---|---|---|---|
smallint|2 bytes|enter petit|-32768 a +32767
integer|4 bytes|enter|-2147483648 a +2147483647
bigint|8 bytes|enter gran|-9223372036854775808 a +9223372036854775807
numeric|variable|precisió especificada per l'usuari, exacte|fins a 131072 digits abans del punt decimal; fins a 16383 digits després del punt decimal
decimal|variable|sinónim de numeric, exacte|fins a 131072 digits abans del punt decimal; fins a 16383 digits després del punt decimal
real|4 bytes|precisió variable, inexacte|Precisió de 6 digits decimals
double precision|8 bytes|precisió variable, inexacte|Precisió de 15 digits decimals
smallserial|2 bytes|petit enter autoincremental|1 a 32767
serial|4 bytes|enter autoincremental|1 a 2147483647
bigserial|8 bytes|enter autoincremental gran|1 a 9223372036854775807

>[!NOTE]
>En realitat `smallserial`,`serial` i`bigserial` no son tipus. Son _àlies_ que ens simplifiquen la gestió dels camps autoincrementals i la seqüència que han de portar associada per controlar la numeració.
>
>Es a dir, quan, per exemple, fem:
>```sql
>CREATE TABLE clients (
>    id SERIAL
>);
>```
>en realitat estem definint una estructura com aquesta:
>```sql
>CREATE SEQUENCE clients_id_seq AS integer;
>CREATE TABLE clients (
>    id integer NOT NULL DEFAULT nextval('clients_id_seq')
>);
>ALTER SEQUENCE clients_id_seq OWNED BY clients.id;
>```

Aixó, a l'hora de definir permisos, ens pot donar algun mal de cap. També s'allunya del SQL més estandaritzat.

Per aixó, tenim la alternativa `GENERATED BY DEFAULT AS IDENTITY`

### `GENERATED BY DEFAULT AS IDENTITY`

No l'hem de pensar com una única opció, ja que es composa de 3 parts: `GENERATED` + `BY DEFAULT` + `AS IDENTITY` 

#### `GENERATED`: 
Indica a PostgreSQL que el sistema s'encarregarà de crear el valor d'aquesta columna. No és un camp estàtic, sinó un camp **calculat** o **produït** pel motor.

#### `BY DEFAULT`: 
Defineix quan actua el sistema. Aquí és on tens dues opcions: `BY DEFAULT` o `ALWAYS`.

 - `BY DEFAULT`: El podem entendre com: *Si no ens informen el valor, agafo el següent número de la seqüencia. Si ens informen el valor, ens quedarem amb aquest valor.*
 
 - `ALWAYS`: El podem entendre com: *Els valors sempre s'agafaràn de la seqüencia, no m'interessa que ningú insereixi cap valor manual perque em poden desincronitzar la seqüencia.* Si algú intenta informar el valor manualment, donarà error.
 

#### `AS IDENTITY`:
El podem entendre com: ***Fes servir una seqüència interna complint l'estàndard SQL***. Això substitueix l'antic comportament del SERIAL. Vincula la columna a una seqüència numèrica (1, 2, 3...) però la lliga a l'estructura de la taula de manera segura (si esborres la taula, s'esborra la seqüència automàticament).

### `SERIAL` vs `GENERATED BY DEFAULT AS IDENTITY`

| Característica | SERIAL (Mètode Antic) | GENERATED ... AS IDENTITY (Mètode Modern) |
| :--- | :--- | :--- |
| **Estandardització** | **No Estàndard.** És una invenció específica de PostgreSQL. Altres bases de dades no ho entenen. | **Estàndard SQL.** Compleix la normativa ISO SQL:2003. Facilita la portabilitat. |
| **Naturalesa** | És un **"pseudo-tipus"** (una drecera o macro) que crea una seqüència per darrere. | És una **propietat de la columna**. La base de dades gestiona la identitat nativament. |
| **Gestió de Permisos** | **Manual.** Si dones permís d'escriptura a la taula, sovint has de donar permís explícit a la seqüència també. | **Automàtica.** Els permisos sobre la seqüència estan lligats als de la taula. |
| **Control d'Inserció Manual** | **Permissiu.** Sempre permet inserir un ID manualment, cosa que pot desincronitzar la seqüència. | **Configurable.** Pots triar `BY DEFAULT` (permissiu) o `ALWAYS` (estricte: bloqueja insercions manuals). |
| **Dependència** | La columna depèn de la seqüència. Si esborres la columna malament, la seqüència pot quedar "òrfena". | La seqüència és un atribut intern de la columna. Si esborres la columna, tot desapareix netament. |
| **Rendiment** | Molt ràpid (fa servir seqüències). | Igual de ràpid (també fa servir seqüències internament). |
| **Recomanació (PostgreSQL 10+)** | **Obsolet.** Es manté per compatibilitat amb codi antic. | **Recomanat.** És la manera correcta de treballar avui dia. |

## DDL - *Data Definition Language*
Es un llenguatge que, fent servir certes sentències SQL, ens permet **definir** l'estructura de les dades. Dit d'una altra manera, son les instruccions que farem servir per construir l'estructura de la nostra base de dades.

Consta de 4 ordres:
- `CREATE`: Ens permet crear parts de l'estructura tals com la propia **base de dades**, **taules**, **vistes**...
- `ALTER`: Ens permet alterar o modificar l'estructura, com per exemple, **afegir columnes** a una taula o **canviar el tipus de dada d'una columna**
- `DROP`: Ens permet eliminar una part de l'estructura. Podem eliminar una **columna**, una **taula** o **tota la base de dades** si cal
- `TRUNCATE`: Ens permet eliminar tot el contingut de la taula pero mantenint l'estructura
  
>[!NOTE]
>El que fa realment `TRUNCATE` es eliminar la taula (`DROP`) i tornar-la a crear (`CREATE`) tot en una i sense que ho haguem de fer nosaltres explícitament. Es per aixó que aquesta operació la classifiquem com `DDL` i no com `DML`. Sempre que volguem esborrar **TOTS** els registres de la taula, es una opció més recomanable a efectes de rendiment que fer un `DELETE FROM nom_taula`.
    
A continuació teniu alguns exemples de sentències DDL que podem fer servir:

### Definició de la propia base de dades
#### Crear la base de dades
```sql
CREATE DATABASE nom_base_de_dades;
```

#### Crear la base de dades indicant el seu **propietari**
```sql
CREATE DATABASE nom_base_de_dades OWNER usuari;
```

#### Eliminar la base de dades
```sql
DROP DATABASE nom_base_de_dades;
```

#### Renombrar la base de dades
```sql
ALTER DATABASE nom_antic RENAME TO nom_nou;
```

### Definició de taules

#### Crear taula

Crear una taula definint alguns camps
```sql
CREATE TABLE clients (
    id GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,    
    posicio_ranking INTEGER DEFAULT 0,
    saldo DECIMAL DEFAULT 0,
    actiu BOOLEAN DEFAULT true
);
```

#### Crear taula amb clau forana
```sql
CREATE TABLE usuaris (
    id GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE,
    dept_id INTEGER REFERENCES usuaris(id) --dept_id es una clau forana que apunta a la clau primaria d'usuaris (id)
);
```

#### Eliminar taula
```sql
DROP TABLE nom_taula;
```

#### Buidar la taula (eliminem els registres que conté pero no la taula)
```sql
TRUNCATE TABLE nom_taula;
```

#### Canviar el nom de la taula
```sql
ALTER TABLE nom_taula_actual RENAME TO nom_taula_nou;
```

#### Afegir columnes
```sql
ALTER TABLE nom_taula ADD COLUMN nom_columna tipus_de_dada;
```

#### Eliminar columna
```sql
ALTER TABLE nom_taula DROP COLUMN nom_columna;
```

#### Modificar columna
```sql
ALTER TABLE nom_taula ALTER COLUMN nom_columna TYPE nou_tipus_de_dada;
```

#### Canviar els camps tipus SERIAL per camps GENERATED ALWAYS AS IDENTITY
```sql
-- 1. Elimina el vincle amb la seqüència antiga (el mecanisme del SERIAL)
ALTER TABLE "CLIENT" ALTER COLUMN "Id" DROP DEFAULT;

-- 2. (Opcional però recomanat) Esborra la seqüència vella que ha quedat òrfena
-- Normalment es diu NomTaula_Camp_seq
DROP SEQUENCE IF EXISTS "CLIENT_Id_seq";

-- 3. Afegeix la nova propietat d'Identitat estricta (ALWAYS)
ALTER TABLE "CLIENT" ALTER COLUMN "Id" 
ADD GENERATED ALWAYS AS IDENTITY;
```
Com encara no tenim valors, potser eliminareu la taula i la tornareu a crear. Pero tingueu en compte que a un model amb dades existents no podriem esborrar la taula i també hauriem de gestionar que el comptador de la seqüència no perdi el valor actual.


## DML - Data Manipulation Language
Es un llenguatge que, fent servir certes sentències SQL, ens permet manipular les dades. Dit d'una altra manera, son les instruccions que farem servir per afegir i modificar contingut a la base de dades que hem definit prèviament. Ens permet realitzar les operacions **CRUD** (Create, Read, Update, Delete) fent servir les següents sentències:

### `INSERT`
Les sentències `INSERT` son les que ens permeten **inserir** o afegir informació a la nostra base de dades en forma de **registres** a les taules. Podem entendre cada registre com una fila de la taula.

Per exemple, si volem inserir un registre a la taula usuaris que hem creat als exemples previs:

```sql
INSERT INTO usuaris (nom, email, detp_id)
VALUES ('Gregorio Esteban Sánchez Fernández', 'dongregorio@gmail.com', 2);
```

>[!NOTE]
>No hem d'informar tots els camps de la taula a l'insert, només els que volguem (o els que no ens quedi més remei perque no admeten NULLS).
>
>En aquest cas no he informat el camp `id` ja que es un `IDENTITY` que, a més, es `GENERATED ALWAYS`, de manera que si l'intento informar jo manualment ens tirarà un error.

### `SELECT`
Les sentències `SELECT` son les que ens permeten consultar o seleccionar l'informació existent a la nostra base de dades.

Un exemple molt senzill seria consultar tot el contingut de la taula d'usuaris:
```sql
SELECT * FROM usuaris;
```
Si analitzem l'estructura de la sentència, li estem dient al nostre SGBD:
 - `SELECT`: Vull seleccionar o llistar registres
 - `*`: Voldré veure totes les columnes del registre
 - `FROM usuaris`: De la taula anomenada `usuaris`

Si només vull mostrar algunes columnes de la taula faria servir:
```sql
SELECT nom, email FROM usuaris;
```
Si analitzem l'estructura de la sentència, li estem dient al nostre SGBD:
 - `SELECT`: Vull seleccionar o llistar registres
 - `nom, email`: Voldré veure les columnes anomenades `nom` i `email`
 - `FROM usuaris`: De la taula anomenada `usuaris`

#### `WHERE`
No sempre (de fet gairebé mai) voldrem veure **TOTS** els registres d'una taula, per aixó fem servir els filtres.
Si volem aplicar filtres sobre els registres que consultem amb una sentència `SELECT` farem servir el modificador `WHERE`.

Per exemple:
```sql
SELECT * FROM usuaris WHERE nom='Mario';
```
Si analitzem l'estructura de la sentència, li estem dient al nostre SGBD:
 - `SELECT`: Vull seleccionar o llistar registres
 - `*`: Voldré totes les columnes del registre
 - `FROM usuaris`: De la taula anomenada `usuaris`
 - `WHERE`: Quan es donin les següents condicions
 - `nom='Mario'`: La condició es que el nom de l'usuari sigui, exactament, `Mario`

Podem filtrar per més d'una columna
```sql
SELECT * FROM usuaris WHERE nom='Mario' AND dept_id=4;
```

Podem filtrar per més d'un valor a la mateixa columna
```sql
SELECT * FROM usuaris WHERE dept_id in (4,5,6);
```
```sql
SELECT * FROM usuaris WHERE nom='Mario' or nom='Luigi';
```

#### `COUNT`, `SUM`, `AVG`

Podem contar els registres d'una taula

```sql
SELECT COUNT(*) FROM usuaris;
```

Sumar el valor de tots els registres trobats
```sql
SELECT SUM(import) FROM comandes WHERE any_fiscal=2025;
```

Treure la mitga dels valors trobats
```sql
SELECT AVG(durada) FROM pelicules WHERE idioma=3;
```

#### `ORDER BY`
Podem indicar l'ordre en el que volem que es mostrin els registres

```sql
SELECT * FROM usuaris ORDER BY nom;
```

#### `LIMIT`
També podem limitar els resultats de la cerca
```sql
SELECT * FROM usuaris LIMIT 5;
```

### `UPDATE`
Permet **modificar** dades **existents** a la base de dades

```sql
UPDATE nom_taula SET columna = valor_nou WHERE condicio;
```


> [!CAUTION]
>
> Revisa que tinguis sempre el `WHERE` a la teva sentència `UPDATE`, si no, estaràs **MODIFICANT TOTS ELS REGISTRES DE LA TAULA**
>
> Recorda sempre [aquesta cançó](https://www.youtube.com/watch?v=i_cVJgIz_Cs&list=RDi_cVJgIz_Cs&start_radio=1)


### `DELETE`
Permet **eliminar** dades **existents** a la base de dades

```sql
DELETE FROM nom_taula WHERE condicio;
```
 Aquí no hem d'indicar la columna ja que estem eliminant **tot el registre**

> [!CAUTION]
>
> Al igual que amb els `UPDATE`, revisa que tinguis sempre el `WHERE`, altrament, estaràs **ELIMINANT TOTS ELS REGISTRES DE LA TAULA**
>
> Recorda sempre [aquesta cançó](https://www.youtube.com/watch?v=i_cVJgIz_Cs&list=RDi_cVJgIz_Cs&start_radio=1)


## Stored Procedures

### Què són els PROCEDURES en una Base de Dades?

Un **Procediment Emmagatzemat** (Stored Procedure) és un conjunt d'instruccions SQL i estructures de control (com variables, bucles o condicionals) que es compila i es desa directament al servidor de la base de dades. En lloc d'enviar múltiples consultes des de la teva aplicació (backend) a la base de dades una per una, simplement invoques o "crides" el procediment pel seu nom.

#### En quins casos s'utilitzen?

1. **Reutilització i manteniment de codi:** Si tens una lògica de negoci molt específica i complexa (per exemple, un tancament comptable a final de mes o la liquidació de carretons de compra) que s'utilitza des de diverses aplicacions o serveis, centralitzar-la a la base de dades evita haver de reprogramar-la en diferents llenguatges.
2. **Millora del rendiment:** En executar múltiples operacions directament dins del servidor, redueixes dràsticament la latència i el trànsit de xarxa entre la teva aplicació i la base de dades. A més, el motor de la base de dades sol desar a la memòria cau el pla d'execució del procediment, fent-lo més ràpid en usos posteriors.
3. **Seguretat robusta:** Pots concedir als usuaris i aplicacions permisos exclusivament per executar el *procedure*, sense donar-los permisos de lectura o escriptura (`SELECT`, `UPDATE`, `DELETE`) sobre les taules reals. Això és una barrera excel·lent contra atacs i errors de manipulació.
4. **Control de transaccions complexes:** Són ideals quan necessites fer operacions múltiples que s'han de tractar com una única unitat (el clàssic "tot o res").

---

### PROCEDURES a PostgreSQL

A PostgreSQL, històricament els desenvolupadors utilitzaven només **Funcions** (`FUNCTIONS`) per agrupar lògica. No obstant això, a partir de la versió 14 de PostgreSQL, es van introduir els veritables **Procediments** (`PROCEDURES`). 

**Quina és la diferència clau a PostgreSQL?**
Les funcions sempre s'executen dins de la transacció que les crida i *sempre retornen un valor*. Per contra, els *procedures* **poden controlar transaccions de forma interna**. Això significa que dins del codi d'un *procedure* de PostgreSQL pots executar explícitament `COMMIT` (per desar els canvis fins a aquest punt) o `ROLLBACK` (per desfer-los). A més, no retornen cap valor directament.

#### Exemple Pràctic: Transferència Bancària

Imagina que tenim una taula de comptes bancaris i volem transferir diners d'un a un altre. Aquest és el cas d'ús perfecte per a un Procedure, ja que requereix fer diversos `UPDATE` i necessitem controlar la transacció perquè els diners no "desapareguin" si ocorre un error a la meitat del procés.

**1. Creem la taula de prova:**

```sql
CREATE TABLE comptes (
    id SERIAL PRIMARY KEY,
    titular VARCHAR(50) NOT NULL,
    saldo NUMERIC(10, 2) NOT NULL DEFAULT 0.00
);

INSERT INTO comptes (titular, saldo) VALUES 
('Ana', 1000.00),
('Carlos', 500.00);
```

**2. Creem el PROCEDURE en PL/pgSQL:**

Escriurem un procediment que resti saldo d'un compte i el sumi a l'altre. Si el compte d'origen no té fons suficients, llançarem una excepció.

```sql
CREATE OR REPLACE PROCEDURE transferir_diners(
    compte_origen INT, 
    compte_desti INT, 
    import NUMERIC
)
LANGUAGE plpgsql
AS $$
DECLARE
    saldo_actual NUMERIC;
BEGIN
    -- 1. Verifiquem el saldo del compte origen
    SELECT saldo INTO saldo_actual FROM comptes WHERE id = compte_origen;
    
    IF saldo_actual < import THEN
        RAISE EXCEPTION 'Saldo insuficient al compte dorigen.';
    END IF;

    -- 2. Restem els diners del compte origen
    UPDATE comptes SET saldo = saldo - import WHERE id = compte_origen;
    
    -- 3. Sumem els diners al compte destí
    UPDATE comptes SET saldo = saldo + import WHERE id = compte_desti;

    -- 4. Confirmem la transacció permanentment
    COMMIT;
    
    RAISE NOTICE 'Transferència de % completada amb èxit.', import;
END;
$$;
```

**3. Executem (Cridem) al PROCEDURE:**

A diferència de les funcions que es criden amb un `SELECT`, els procediments s'invoquen amb la instrucció `CALL`.

```sql
-- Transferim 200 de l'Ana (id=1) a en Carlos (id=2)
CALL transferir_diners(1, 2, 200.00);
```

En executar aquesta línia, PostgreSQL processa tota la lògica al servidor. L'Ana passarà a tenir 800.00 i en Carlos 700.00. Si intentéssim executar `CALL transferir_diners(1, 2, 5000.00);`, el procediment llançaria l'excepció i cancel·laria la transacció abans de tocar els diners de ningú.
