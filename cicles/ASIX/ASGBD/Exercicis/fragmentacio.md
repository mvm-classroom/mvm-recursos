# Distribució i fragmentació de les dades

## 0. Preparació de l'escenari

3 màquines Ubuntu Server 24.04 (poden ser VBox o Isard):

- `gateway`
- `current`
- `history`

Totes 3 amb un Ubuntu Server 24.04 on hem restaurat la base de dades `dvdrental`.

Si ho feu amb VBox, us recomano fer-ho en una màquina i després duplicar-la per estalviar temps i feina.

## 1. Enunciat

Disposem d’un servidor PostgreSQL que conté informació sobre la nostra empresa de lloguer de pel·lícules des del dia que la nostra empresa va obrir, i el fet de contenir tanta informació està fent que el sistema es torni una mica més lent del desitjat. 
Ens han proposat un projecte per tal de millorar aquesta situació, i consisteix a fragmentar algunes taules per tal d’optimitzar l’accés a aquestes dades.

>[!IMPORTANT]
>Es recomana documentar tot el procés com un tutorial, tant per per vosaltres per tenir un recurs de referència com per suport per altres exercicis lliurables.

>[!TIP] Recursos que us poden resultar d'utilitat
- [Create server](https://www.postgresql.org/docs/18/sql-createserver.html)
- [Foreign Data Wrapper](https://www.postgresql.org/docs/18/postgres-fdw.html)
- [Import Foreign Schema](https://www.postgresql.org/docs/18/sql-importforeignschema.html)
- [DDL Partitioning](https://www.postgresql.org/docs/18/ddl-partitioning.html)
- [Create Table](https://www.postgresql.org/docs/18/sql-createtable.html)

## 2. Preparació de l'entorn

Modifica la informació de les bases de dades de la següent manera:

- Servidor `current`: esborra tota la informació de la taula `payment` que tingui una data de pagament **anterior** al `2007-05-01`.
- Servidor `history`: esborra tota la informació de la taula `payment` que tingui una data de pagament **igual o superior** al `2007-05-01`.
- Servidor `gateway`: esborra taula `payment` sencera (contingut i estructura)

## 3. Importació de taules foranes

Al servidor `gateway` importar les següents taules:
- `payment_history`: aquesta taula hereta tota la informació de la taula `payment` que conté el servidor `history`
- `payment_current`: aquesta taula hereta tota la informació de la taula `payment` que conté el servidor `current`




## 4. Herència múltiple

Accedeix a servidor `gateway` i crea la taula `payment_complete`, fent que tant `payment_history` i `payment_current` n’heretin de `payment_complete`.
