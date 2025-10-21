# Instal.lació de PostgreSQL 18 a Ubuntu Server 24.04

## 1. Actualització de repositoris

Actualitzem els repositoris fent servir l'script que ens proporcionen al web oficial de `PostgreSQL`
```shell
sudo apt install -y postgresql-common
```
Podeu fer una ullada a l'script, segur que trobeu alguna cosa interessant
```shell
cat /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh
```
Executem l'script
>[!IMPORTANT]
>```shell
>isard@ubuntu-server:~$ sudo /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh
>This script will enable the PostgreSQL APT repository on apt.postgresql.org on
>your system. The distribution codename used will be noble-pgdg.
>
>Press Enter to continue, or Ctrl-C to abort.
>
>Using keyring /usr/share/postgresql-common/pgdg/apt.postgresql.org.gpg
>Writing /etc/apt/sources.list.d/pgdg.sources ...
>
>Running apt-get update ...
>.
>.
>.
>Descargados 12,4 MB en 2s (7.655 kB/s)
>Leyendo lista de paquetes... Hecho
>
>You can now start installing packages from apt.postgresql.org.
>
>Have a look at https://wiki.postgresql.org/wiki/Apt for more information;
>most notably the FAQ at https://wiki.postgresql.org/wiki/Apt/FAQ
>
>```

Arribats a aquest punt, ja tenim els repositoris actualitzats i podem instal.lar `postgresql-18`

## 2. Instal.lació i comprovacions inicials
### 2.1 Instal.lació
```shell
sudo apt install -y postgresql-18
```

### 2.2 Comprovacions inicials
Un cop instal.lat, revisem que almenys el servei funciona
```shell
isard@ubuntu-server:~$ systemctl status postgresql
● postgresql.service - PostgreSQL RDBMS
     Loaded: loaded (/usr/lib/systemd/system/postgresql.service; enabled; preset: ena>
     Active: active (exited) since Tue 2025-10-06 06:54:40 UTC; 10min ago
   Main PID: 1809 (code=exited, status=0/SUCCESS)
        CPU: 1ms

```
Connectem directament amb l'usuari `postgres`
```shell
sudo -u postgres psql
```

El resultat hauría de ser semblant a aquest
>[!IMPORTANT]
>```shell
>isard@ubuntu-server:~$ sudo -u postgres psql
>psql (18.0 (Ubuntu 18.0-1.pgdg24.04+3))
>Digite «help» para obtener ayuda.
>
>postgres=#
>```

>[!IMPORTANT]
>```shell
>postgres=# \password postgres
>Ingrese nueva contraseña para usuario «postgres»:
>Ingrésela nuevamente:
>postgres=#
>
>```

En aquest cas, he fet servir `pirineus` per fer la prova.

Uns segons després penso que, tot i ser un entorn de proves, hauria de seguir el meu instint de fer servir una contrasenya més robusta, així que la canviarem.

>[!IMPORTANT]
>```shell
>postgres=# ALTER USER postgres WITH PASSWORD 'postgre-pirineus';
>ALTER ROLE
>postgres=#
>```

Ara podem provar funcionament bàsic del SGBD, com llistar `\l` les bases de dades existents:

```shell
                                                               Listado de base de datos
  Nombre   |  Dueño   | Codificación | Proveedor de locale |   Collate   |    Ctype    | Configuración regional | Reglas ICU: |      Privilegios
-----------+----------+--------------+---------------------+-------------+-------------+------------------------+-------------+-----------------------
 postgres  | postgres | UTF8         | libc                | es_ES.UTF-8 | es_ES.UTF-8 |                        |             |
 template0 | postgres | UTF8         | libc                | es_ES.UTF-8 | es_ES.UTF-8 |                        |             | =c/postgres          +
           |          |              |                     |             |             |                        |             | postgres=CTc/postgres
 template1 | postgres | UTF8         | libc                | es_ES.UTF-8 | es_ES.UTF-8 |                        |             | =c/postgres          +
           |          |              |                     |             |             |                        |             | postgres=CTc/postgres
(3 filas)

```

o connectar a una de les existents amb `\c`

```shell
postgres=# \c postgres
Ahora está conectado a la base de datos «postgres» con el usuario «postgres».
postgres=#
```

### 2.3 Connexió a postgres des d'un client

A postgres podem connectar de diverses maneres

Connexió per defecte, sense indicar host, ni usuari ni password ni bdd
```shell
psql
```

Amb `-U` indiquem només l'usuari
```shell
psql -U usuari
```

Forcem l'usuari d'execució

```shell
sudo -u postgres psql
```

Amb `-d` indiquem la bdd
```shell
psql -d basededades
```

Amb `-h` indiquem al host que volem connectar
```shell
psql -h localhost -p 5432 -U usuari -d basededades
```

```shell
psql -h 192.168.1.1 -p 5432 -U usuari -d basededades
```

```shell
psql -h 192.168.1.1 -p 5432 -U usuari -d basededades
```

>[!CAUTION]
>Si has intentat connectar des del client, segurament t'has trobat amb errors de connexió

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


Després de canviar l'opció, reiniciar el servei de postgres, comprovar l'status i tornar a provar des del client

>[!CAUTION]
>Encara falla?

Aixó es que encara ens falta algún canvi més a la configuració

>[!TIP]
>Encara que el servei **escolta** adreces remotes, falta afinar una mica més la seguretat.
>Podem indicar quin tipus d'autenticació fem servir segons el métode de connexió, l'usuari, la base de dades, l'adreça remota...
>Tot aixó ho podem definir al fitxer `/etc/postgresql/18/main/pg_hba.conf`
>
>Llegiu tota l'introducció que hi ha als comentaris del fitxer per entendre millor el que estem apunt de modificar
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

Reiniciem i comprovem l'status
```shell
sudo systemctl restart postgresql

systemctl status postgresql
```

I tornem a provar des del client i el server

```shell
psql -h 192.168.1.100 -U postgres
```
Un cop solucionats els problemes de connexió, podem continuar amb les proves bàsiques

### 2.4 Proves amb la base de dades

#### 2.4.1 Crear usuari `ncognom` amb els privilegis de postgres.

```sql
CREATE USER ncognom WITH PASSWORD '@lumn3$$';
```

Tenim el problema que, si hem creat l'usuari d'aquesta manera, no podrem fer login ni serem superusuaris.

```sql
CREATE ROLE ncognom WITH LOGIN PASSWORD '@alumn3$$' SUPERUSER;
```

#### 2.4.2 Fem login amb el nou usuari per fer totes les proves restants

```shell
psql -h 192.168.1.100 -U ncognom -d postgres
```

#### 2.4.3 Creem la base de dades `mvm_asgbd`

```sql
CREATE DATABASE mvm_asgbd OWNER ncognom;
```

#### 2.4.4 Creem la taula `mascotes`

```sql
CREATE TABLE mascotes (
    id serial PRIMARY KEY,
    num_chip VARCHAR(50) NOT NULL,
    nom VARCHAR(50) NOT NULL,
    especie VARCHAR(50) NOT NULL,
    descripcio VARCHAR(100)
);
```

#### 2.4.5 Afegim uns quants elements per comprovar que tenim permís `insert`

```sql
INSERT INTO mascotes (id, num_chip, nom, especie, descripcio)
VALUES
('1', '0001', 'Currupipi', 'Tigre', ''),
('2', '1P-1002', 'Firulais', 'Gos', ''),
('3', '300010', 'Capitán Escorbuto', 'Lloro', ''),
('4', '500-U3300', 'Marcel', 'Mico', ''),
('5', '47221301-S', 'Ronald McPerkins', 'Humà', '');
```

```sql
SELECT * FROM mascotes;
```

#### 2.4.6 Comprovem que podem fer també `update` i `delete`

```sql
DELETE FROM mascotes WHERE especie='Humà';
```

```sql
UPDATE mascotes SET especie='Mico caputxí' where nom='Marcel';
```

```sql
SELECT * FROM mascotes;
```
