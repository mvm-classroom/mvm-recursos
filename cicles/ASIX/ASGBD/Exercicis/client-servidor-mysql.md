# Sistemes client i servidor amb MySQL

## Descripció

>[!NOTE]
>- **Objectiu**: Posar en pràctica els coneixements adquirits sobre les arquitectures dels sistemes gestors de bases de dades i la comunicació entre clients i servidors.
>
>- **Desenvolupament**: Individual
>
>- **Duració**: 3h aproximadament.
>
>- **Lliurament**: No cal lliurar-ho, pero recomano recopilar tota la documentació necessaria a `Github`, amb un fitxer ben formatat amb markdown. El vostre jo del futur us ho agrairà.

## Preparació de l'escenari
>[!NOTE]
> Necessitem crear el següent escenari a IsardVDI:
> - **Servidor:** Plantilla `MVM - Ubuntu 24.04 Server` amb les opcions de hardware que ja venen de serie.
>  
> - **Client:** Plantilla `Ubuntu Desktop 22.04`, 2 vCPU, 4GB de RAM. Xarxes: `Default` i `Personal1`
>

## Primera part: Servidor
### 1. Instal·lació de MySQL
Instal.lar, a la màquina `server`, el SGBD. En aquest cas: `MySQL`.

Comprovar que podem accedir amb l'eina client de terminal al SGBD que acabem d'instal.lar.

### 2. Càrrega de les dades
Cerca qualsevol base de dades de proves MySQL i documenta't sobre com carregar-la o restaurar-la.
Per exemple [aquesta](https://dev.mysql.com/doc/employee/en/)

## Segona part: Client (terminal)
### 1. Client local
Intentar accedir localment amb l'eina client de terminal i comprovar que podem accedir i treballar amb la base de dades de prova.


## Tercera part: Client remot (MySQL Workbench)

### 1. Instal·lació de MySQL Workbench
A la màquina client, instal·la la versió més nova de MySQL Workbench o una eina client amb GUI similar.

### 2. Client remot (MySQL Workbench)
Fes servir MySQL Workbench per accedir a la instància remota de MySQL al servidor i fer consultes a qualsevol de les taules de la base de dades de prova.

Si trobes qualsevol error de connexió, hauràs d’esbrinar la forma de solucionar-lo.

## Quarta part: Client (DBeaver)

### 1. Instal·lació de DBeaver
A la màquina “client” de l’exercici anterior, instal·la la versió més nova de DBeaver. El pots instal.lar de diverses formes, documenta i justifica la teva elecció.

### 2. Client remot (DBeaver)
Fes servir DBeaver per accedir a la instància remota de MySQL i realitzar consultes SQL de tipus SELECT cap a algunes taules del servidor, per a comprovar que tot funciona.

Si trobes qualsevol error de connexió, hauràs d’esbrinar la forma de solucionar-lo.


## Cinquena part: preguntes
Contesta les següents preguntes per a relacionar la pràctica amb la teoria:

### 1. Consideres MySQL com un SGBD centralitzat o bé com un basat en el sistema client/servidor? Argumenta la teva resposta.

### 2. Si has categoritzat MySQL com un sistema client/servidor, dins quin sistema de capes consideres que encaixa millor: 2 capes o 3 capes? Argumenta la teva resposta.

### 3. Pots fer una comparativa entre aquesta pràctica i la versió de PostgreSQL? Quines similituds has trobat? Quines diferències? 
