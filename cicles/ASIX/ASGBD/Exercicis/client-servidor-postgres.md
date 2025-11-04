# Sistemes client i servidor amb PostgreSQL

## Descripció

>[!NOTE]
>- **Objectiu**: Posar en pràctica els coneixements adquirits sobre les arquitectures dels sistemes gestors de bases de dades i la comunicació entre clients i servidors.
>
>- **Desenvolupament**: Individual
>
>- **Duració**: 3h aproximadament.
>
>- **Lliurament**: Allotjant tota la documentació necessaria a `Github`, amb un fitxer ben formatat amb markdown i pujant la URL del repositori a la tramesa en Moodle

>[!IMPORTANT]
>Heu d'explicar, **AMB LES VOSTRES PARAULES**, tot el procés d'instal·lació, configuració i proves.
>
>Explicar:
>
>- Perquè feu cada pas i perquè modifiqueu cada opció o fitxer.
>- De quin recurs heu tret l'informació (lloc oficial, varis tutorials, etc...)
>- Quines proves heu fet i el resultat obtingut
>
>Si les explicacions son copiades de ChatGPT o similar la puntuació de l'exercici serà 0
>

## Preparació de l'escenari
>[!NOTE]
> Necessitem crear el següent escenari a IsardVDI:
> - **Servidor:** Plantilla `MVM - Ubuntu 24.04 Server` amb les opcions de hardware que ja venen de serie.
>  
> - **Client:** Plantilla `Ubuntu Desktop 22.04`, 2 vCPU, 4GB de RAM. Xarxes: `Default` i `Personal1`
>
> Podeu fer servir les màquines de l'exercici anterior si voleu estalviar temps

> [!warning]
> Has de canviar el hostname de cada màquina creada. Per exemple, si soc Joseph Joestar i he de posar nom a les màquines servidora i i clients, les anomenaria `jjoestar-server`, `jjoestar-cli1` i `jjoestar-cli2`
> 
> Per aconseguir aixó pots fer el següent:
> 
> ```
> sudo hostnamectl set-hostname jjoestar-server
> ``` 
> 
> Durant l'exercici, qualsevol referencia que veieu a `jjoestar` es un exemple i ha de ser canviada per la nomenclatura equivalent al vostre nom.
> 
> Si no es segueix aquesta nomenclatura **la puntuació de l’exercici serà un 0**.


## Primera part: Servidor
### 1. Instal·lació de PostgreSQL
Instal.lar, a la màquina `server`, el SGBD. En aquest cas: `PostgreSQL 18`. Podeu aprofitar, si voleu, la màquina de l'exercici anterior.

### 2. Càrrega de les dades
Connectat al servidor i, fent servir el terminal, fes el necessari per carregar les dades de [`dvdrental.tar`](https://github.com/mvm-classroom/mvm-recursos/raw/main/cicles/ASIX/ASGBD/Recursos/dvdrental.tar). Potser t'interessa fer una ullada a l'eina [`pg_restore`](https://www.postgresql.org/docs/current/app-pgrestore.html)

## Segona part: Client (terminal)
### 1. Client local
Des de la mateixa màquina on tens instal·lat el servidor, converteix-te en usuari `postgres` i accedeix a la consola de PostgreSQL amb la comanda “psql”. Un cop a dins, realitzar consultes SQL de tipus SELECT cap a algunes taules de la bdd `dvdrental` al servidor, per a comprovar que tot funciona.

### 2. Client remot (localhost)
La consola `psql` que has fet servir al punt anterior també serveix per a realitzar connexions remotes si fem servir el paràmetre `-h` per a establir la direcció del host i el paràmetre `-U` per a establir el nom de l’usuari. 

Des de la mateixa màquina on tens instal·lat el servidor, fent servir l’usuari predeterminat (sense sudo, ni root ni usuari `postgres`) executa la comanda `psql -h localhost -U postgres` per accedir a la instància remota de postgres i realitzar consultes `SQL` de tipus `SELECT` cap a algunes taules del servidor, per a comprovar que tot funciona.

Si trobes qualsevol error de connexió, hauràs d’esbrinar la forma de solucionar-lo.

### 3. Client remot (remote host)
Fes servir `psql -h x.x.x.x -U postgres` per connectar, remotament, des de la màquina client a la màquina servidora. Realitza algunes consultes a la base de dades per comprovar que tot funciona.

>Si no estàs fent servir les màquines de l'exercici anterior, hauràs d'instalar `postgresql-client-18`

## Tercera part: Client (pgAdmin 4)

### 1. Instal·lació de pgAdmin 4
A la màquina servidora, instal·la la versió més nova de pgAdmin v4 fent servir el teu correu electrònic i la contrasenya "postgres" durant el procés d’instal·lació:
https://www.pgadmin.org/download/pgadmin-4-apt/

### 2. Client remot (pgAdmin 4)
Fes servir pgAdmin 4 per accedir a la instància remota de postgres i realitzar consultes SQL de tipus SELECT cap a algunes taules del servidor, per a comprovar que tot funciona.

Si trobes qualsevol error de connexió, hauràs d’esbrinar la forma de solucionar-lo.

## Quarta part: Client (DBeaver)

### 1. Instal·lació de DBeaver
A la màquina “client” de l’exercici anterior, instal·la la versió més nova de DBeaver. El pots instal.lar de diverses formes, documenta i justifica la teva elecció.

### 2. Client remot (DBeaver)
Fes servir DBeaver per accedir a la instància remota de postgres i realitzar consultes SQL de tipus SELECT cap a algunes taules del servidor, per a comprovar que tot funciona.

Si trobes qualsevol error de connexió, hauràs d’esbrinar la forma de solucionar-lo.


## Cinquena part: preguntes
Contesta les següents preguntes per a relacionar la pràctica amb la teoria:

### 1. Consideres PostgreSQL com un SGBD centralitzat o bé com un basat en el sistema client/servidor? Argumenta la teva resposta.

### 2. Si has categoritzat PostgreSQL com un sistema client/servidor, dins quin sistema de capes consideres que encaixa millor: 2 capes o 3 capes? Argumenta la teva resposta. 
