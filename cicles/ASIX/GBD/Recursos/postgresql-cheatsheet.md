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

## DDL - *Data Definition Language*

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
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,    
    posicio_ranking INTEGER DEFAULT 0,
    saldo DECIMAL DEFAULT 0,
    actiu BOOLEAN DEFAULT true
);
```

#### Crear taula amb clau forana
```sql
CREATE TABLE usuaris (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE,
    dept_id INTEGER REFERENCES usuaris(id)
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
