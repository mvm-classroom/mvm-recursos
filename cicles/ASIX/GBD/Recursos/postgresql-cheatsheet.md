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

## DDL - *Data Definition Language*

### Definició la propia base de dades

Crear la base de dades
```sql
CREATE DATABASE nom_base_de_dades;
```

Crear la base de dades indicant el seu propietari
```sql
CREATE DATABASE nom_base_de_dades OWNER usuari;
```

Eliminar la base de dades
```sql
DROP DATABASE nom_base_de_dades;
```

### Definició de taules

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

Renombrar la base de dades
```sql
ALTER DATABASE nom_antic RENAME TO nom_nou;
```
