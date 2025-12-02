# Solució - Sistemes client i servidor amb PostgreSQL

## Primera part: Servidor
### 1. Instal·lació de PostgreSQL
Instal.lar, a la màquina `server`, el SGBD. En aquest cas: `PostgreSQL 18`. Podeu aprofitar, si voleu, la màquina de l'exercici anterior.

Teniu disponible una [guia per instal.lar PostgreSQL 18 ](https://github.com/mvm-classroom/mvm-recursos/blob/main/cicles/ASIX/ASGBD/Solucions/install-postgre18.md)

### 2. Càrrega de les dades
Connectat al servidor i, fent servir el terminal, fes el necessari per carregar les dades de [`dvdrental.tar`](https://github.com/mvm-classroom/mvm-recursos/raw/main/cicles/ASIX/ASGBD/Recursos/dvdrental.tar). Potser t'interessa fer una ullada a l'eina [`pg_restore`](https://www.postgresql.org/docs/current/app-pgrestore.html)

#### 2.1 Abans de res, hauriem de crear la base de dades.
Connectem al SGBD com l'usuari `postgres`
```shell
psql -h localhost -U postgres
```
i un cop a dins, creem la base de dades
```sql
CREATE DATABASE dvdrental OWNER postgres;
```
#### 2.2 Descarregar el fitxer amb la base de dades
Podem descarregar el fitxer `dvdrental.tar` fent

```shell
wget https://github.com/mvm-classroom/mvm-recursos/raw/main/cicles/ASIX/ASGBD/Recursos/dvdrental.tar
```
#### 2.3 Revisar i importar el fitxer amb la base de dades
Per tafanejar el fitxer `dvdrental.tar` abans d'importarlo a cegues
```shell
pg_restore --list dvdrental.tar
```

Un exemple de com restaurar el fitxer `dvdrental.tar` a la base de dades `dvdrental` que hem creat prèviament

```shell
pg_restore -h localhost -U postgres -d dvdrental dvdrental.tar
```

## Segona part: Client (terminal)
### 1. Client local
Des de la mateixa màquina on tens instal·lat el servidor, converteix-te en usuari `postgres` i accedeix a la consola de PostgreSQL amb la comanda “psql”. Un cop a dins, realitzar consultes SQL de tipus SELECT cap a algunes taules de la bdd `dvdrental` al servidor, per a comprovar que tot funciona.

```shell
sudo -u postgres psql
```
Connectem a la `dvdrental` i llistem les taules

```sql
postgres=# \c dvdrental
Ahora está conectado a la base de datos «dvdrental» con el usuario «postgres».
dvdrental=# \dt
             Listado de tablas
 Esquema |    Nombre     | Tipo  |  Dueño
---------+---------------+-------+----------
 public  | actor         | tabla | postgres
 public  | address       | tabla | postgres
 public  | category      | tabla | postgres
 public  | city          | tabla | postgres
 public  | clients       | tabla | postgres
 public  | country       | tabla | postgres
 public  | customer      | tabla | postgres
 public  | film          | tabla | postgres
 public  | film_actor    | tabla | postgres
 public  | film_category | tabla | postgres
 public  | inventory     | tabla | postgres
 public  | language      | tabla | postgres
 public  | payment       | tabla | postgres
 public  | rental        | tabla | postgres
 public  | staff         | tabla | postgres
 public  | store         | tabla | postgres
(16 filas)
```
Fem una consulta, per exemple, a la taula d'actors

```sql
dvdrental=# SELECT * FROM actor LIMIT 10;
 actor_id | first_name |  last_name   |      last_update
----------+------------+--------------+------------------------
        1 | Penelope   | Guiness      | 2013-05-26 14:47:57.62
        2 | Nick       | Wahlberg     | 2013-05-26 14:47:57.62
        3 | Ed         | Chase        | 2013-05-26 14:47:57.62
        4 | Jennifer   | Davis        | 2013-05-26 14:47:57.62
        5 | Johnny     | Lollobrigida | 2013-05-26 14:47:57.62
        6 | Bette      | Nicholson    | 2013-05-26 14:47:57.62
        7 | Grace      | Mostel       | 2013-05-26 14:47:57.62
        8 | Matthew    | Johansson    | 2013-05-26 14:47:57.62
        9 | Joe        | Swank        | 2013-05-26 14:47:57.62
       10 | Christian  | Gable        | 2013-05-26 14:47:57.62
(10 filas)
```

### 2. Client remot (localhost)
La consola `psql` que has fet servir al punt anterior també serveix per a realitzar connexions remotes si fem servir el paràmetre `-h` per a establir la direcció del host i el paràmetre `-U` per a establir el nom de l’usuari. 

Des de la mateixa màquina on tens instal·lat el servidor, fent servir l’usuari predeterminat (sense sudo, ni root ni usuari `postgres`) executa la comanda `psql -h localhost -U postgres` per accedir a la instància remota de postgres i realitzar consultes `SQL` de tipus `SELECT` cap a algunes taules del servidor, per a comprovar que tot funciona.

```shell
psql -h localhost -U postgres -d dvdrental
```

```sql
dvdrental=# \dt
             Listado de tablas
 Esquema |    Nombre     | Tipo  |  Dueño
---------+---------------+-------+----------
 public  | actor         | tabla | postgres
 public  | address       | tabla | postgres
 public  | category      | tabla | postgres
 public  | city          | tabla | postgres
 public  | clients       | tabla | postgres
 public  | country       | tabla | postgres
 public  | customer      | tabla | postgres
 public  | film          | tabla | postgres
 public  | film_actor    | tabla | postgres
 public  | film_category | tabla | postgres
 public  | inventory     | tabla | postgres
 public  | language      | tabla | postgres
 public  | payment       | tabla | postgres
 public  | rental        | tabla | postgres
 public  | staff         | tabla | postgres
 public  | store         | tabla | postgres
(16 filas)

dvdrental=# SELECT film_id, title, release_year FROM film ORDER BY film_id LIMIT 10;
 film_id |      title       | release_year
---------+------------------+--------------
       1 | Academy Dinosaur |         2006
       2 | Ace Goldfinger   |         2006
       3 | Adaptation Holes |         2006
       4 | Affair Prejudice |         2006
       5 | African Egg      |         2006
       6 | Agent Truman     |         2006
       7 | Airplane Sierra  |         2006
       8 | Airport Pollock  |         2006
       9 | Alabama Devil    |         2006
      10 | Aladdin Calendar |         2006
(10 filas)
```

Si trobes qualsevol error de connexió, hauràs d’esbrinar la forma de solucionar-lo.

>[!TIP]
>No hauriem de tenir errors de connexió perquè a la pràctica anterior ho vam deixar *niquelat*

### 3. Client remot (remote host)
Fes servir `psql -h x.x.x.x -U postgres` per connectar, remotament, des de la màquina client a la màquina servidora. Realitza algunes consultes a la base de dades per comprovar que tot funciona.

>Si no estàs fent servir les màquines de l'exercici anterior, hauràs d'instalar `postgresql-client-18`

```shell
psql -h 192.168.1.100 -U postgres -d dvdrental
```

```sql
dvdrental=# SELECT * FROM category LIMIT 10;
 category_id |    name     |     last_update     
-------------+-------------+---------------------
           1 | Action      | 2006-02-15 09:46:27
           2 | Animation   | 2006-02-15 09:46:27
           3 | Children    | 2006-02-15 09:46:27
           4 | Classics    | 2006-02-15 09:46:27
           5 | Comedy      | 2006-02-15 09:46:27
           6 | Documentary | 2006-02-15 09:46:27
           7 | Drama       | 2006-02-15 09:46:27
           8 | Family      | 2006-02-15 09:46:27
           9 | Foreign     | 2006-02-15 09:46:27
          10 | Games       | 2006-02-15 09:46:27
(10 filas)
```

## Tercera part: Client (pgAdmin 4)

### 1. Instal·lació de pgAdmin 4
A la màquina servidora, instal·la la versió més nova de pgAdmin v4 fent servir el teu correu electrònic i la contrasenya "postgres" durant el procés d’instal·lació:
https://www.pgadmin.org/download/pgadmin-4-apt/

Extret de la pàgina enllaçada:

```shell
# Install the public key for the repository (if not done previously):
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg

# Create the repository configuration file:
sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'
```
```shell
# Install for web mode only: 
sudo apt install pgadmin4-web 

# Configure the webserver, if you installed pgadmin4-web:
sudo /usr/pgadmin4/bin/setup-web.sh
```

```shell
isard@ubuntu-server:~$ sudo /usr/pgadmin4/bin/setup-web.sh
Setting up pgAdmin 4 in web mode on a Debian based platform...
Creating configuration database...
/usr/pgadmin4/venv/lib/python3.12/site-packages/passlib/pwd.py:16: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
NOTE: Configuring authentication for SERVER mode.

Enter the email address and password to use for the initial pgAdmin user account:

Email address: latevaadreça@institutmvm.cat
Password:
Retype password:
pgAdmin 4 - Application Initialisation
======================================

Creating storage and log directories...
We can now configure the Apache Web server for you. This involves enabling the wsgi module and configuring the pgAdmin 4 application to mount at /pgadmin4. Do you wish to continue (y/n)? y
The Apache web server is running and must be restarted for the pgAdmin 4 installation to complete. Continue (y/n)? y
Apache successfully restarted. You can now start using pgAdmin 4 in web mode at http://127.0.0.1/pgadmin4
```

### 2. Client remot (pgAdmin 4)
Fes servir pgAdmin 4 per accedir a la instància remota de postgres i realitzar consultes SQL de tipus SELECT cap a algunes taules del servidor, per a comprovar que tot funciona.

Si trobes qualsevol error de connexió, hauràs d’esbrinar la forma de solucionar-lo.

Comencem accedint, des del navegador del client, a http://192.168.1.100/pgadmin4 i fem login amb les credencials que hem configurat al `setup-web.sh`

![Inici de sesió a pgAdmin 4 via web](img/pgAdmin4-web.png)

Un cop iniciada la sessió, com es la primera vegada, hem de configurar una nova connexió indicant:
- El host al que volem connectar (`192.168.1.199`)
- La base de dades per defecte (`postgres`)
- L'usuari (`postgres`) i password (`postgres`) amb els que connectar

>[!warning]
>**Important**: L'**usuari** i **password** no son els del pgAdmin4, son els de l'instància de PostgreSQL a la que volem connectar

![Configurar connexió a pgAdmin4](img/pgAdmin4-connexio.png)

Una vegada connetats al servidor, podem fer servir l'arbre d'objectes per navegar i comprovar que es mostren les taules de `dvdrental`.

Fem una query senzilla per acaba de verificar.

![Query de prova](img/pgAdmin4-query.png)

## Quarta part: Client (DBeaver)

### 1. Instal·lació de DBeaver
A la màquina “client” de l’exercici anterior, instal·la la versió més nova de DBeaver. El pots instal.lar de diverses formes, documenta i justifica la teva elecció.

Ho podem instal.lar, per exemple, directament amb `apt`

```shell
sudo apt install dbeaver-ce -y
```

### 2. Client remot (DBeaver)
Fes servir DBeaver per accedir a la instància remota de postgres i realitzar consultes SQL de tipus SELECT cap a algunes taules del servidor, per a comprovar que tot funciona.

Si trobes qualsevol error de connexió, hauràs d’esbrinar la forma de solucionar-lo.

Creem, a DBEaver, una nova connexió cap a un SGBD de tipus PostgreSQL
![Crear, en DBeaver, nova connexió cap a un SGBD PostgreSQL](img/DBeaver-nova-connexio.png)

Configurem la nova connexió amb els valors habituals (host, usuari, password...)
![Configurar la nova connexió cap a PostgreSQL](img/DBeaver-configurar-connexio.png)

Provem la nova configuració. Si es la primera vegada que conectem a un SGBD PostgreSQL ens demanara baixar-nos el driver.
![Provar la configuració](img/DBeaver-test-connexio.png)

Un cop baixat, la connexió es correcta. Fixeu-vos que fa servir `JDBC`.
![Resultats de la prova de connexió](img/DBeaver-resultat-test-connexio.png)

Quan intentem navegar per l'arbre per consultar l'estructura, ens trobem que només ens mostra la base de dades `postgres`. 
![Només es veu la bdd postgres a l'arbre](img/DBeaver-nomes-postgres.png)

Aixó ho podem solucionar fent una petita modificació a la configuració de la nostra connexió.
![Activar 'Show all databases'](img/DBeaver-show-all-databases.png)

Si tornem a connectar i revisitem l'arbre, veurem que ara ens mostra totes les bases de dades que gestiona el SGBD
![Ara es mostren totes les bdds](img/DBeaver-totes-bdd.png)

Ara sí, fem una consulta de prova
![Consulta de prova](img/DBeaver-query.png)

## Cinquena part: preguntes
Contesta les següents preguntes per a relacionar la pràctica amb la teoria:

### 1. Consideres PostgreSQL com un SGBD centralitzat o bé com un basat en el sistema client/servidor? Argumenta la teva resposta.

>[!NOTE]
>Clarament estem parlant d'un sistema client-servidor, ja no perquè l'enunciat de l'exercici fa força *spoiler* sobre el tema, sinó perquè si no fem servir aquesta arquitectura no podriem estar connectant des d'una màquina remota (client).
>
>La primera part de l'exercici demana una connexió local, fent servir l'usuari postgres, i aquí podria semblar que estem davant un sistema centralitzat. 	
> 	
>La segona part de l'exercici ens demana una connexió en remot, des de dins la mateixa màquina, el qual pot no semblar-ho, però està fent servir una comunicació client/servidor a través d’un protocol de xarxa.
>
>La tercera part de l'exercici ens demana una connexió en remot, des de fora cap al servidor, és a dir, connexió client-servidor. Si l'arquitectura fos centralitzada, això seria impossible, ja que les màquines centralitzades no es comuniquen amb altres màquines.


### 2. Si has categoritzat PostgreSQL com un sistema client/servidor, dins quin sistema de capes consideres que encaixa millor: 2 capes o 3 capes? Argumenta la teva resposta.

>[!NOTE]
>Estem parlant d'un **sistema de 3 capes**, ja que la comunicació no tenim per què fer-la de forma directa amb el servidor. Dins el primer 	exercici fem comunicació directa entre el client i el servidor via sockets (el client i el servidor de Postgres parlen el mateix idioma, ja que son del mateix fabricant), però d'aquest punt en endavant fem dues coses ben diferents: primer fem servir una **aplicació externa**, que es connecta al servidor a través d'un port, i li manem consultes SQL; després fem servir l'aplicació per modificar dades i veiem que això es transforma en noves consultes SQL. 
> 	
>A més, a l’exercici quatre, quan configurem DBeaver per a connectar-nos al PSQL, aquest està fent servir un **connector JDBC** i, clara indicació que estem fent servir un sistema de 3 capes. Aquesta capa intermèdia, que actua de proxy antre la 1a (el client) i la 3a (el servidor), tradueix les instruccions que li arriben a un llenguatge que pot entendre el servidor, sigui SQL o un altre. Això permet, en el cas de JDBC, que qualsevol aplicació Java parli amb el servidor i, a l’hora, que es pugui canviar de servidor sense modificar l’aplicació, o al revés: canviar l’aplicació sense canviar el servidor.
> 	
>Finalment, com a prova irrefutable, la documentació oficial sobre l'`API` i els 	diferents connectors o interfaces, que un sistema en 2 capes no tindria: https://www.postgresql.org/docs/18/client-interfaces.html
