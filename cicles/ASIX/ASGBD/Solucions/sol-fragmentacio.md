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

> [!IMPORTANT]
>Es recomana documentar tot el procés com un tutorial, tant per per vosaltres per tenir un recurs de referència com per suport per altres exercicis lliurables.

> [!TIP] 
> Recursos que us poden resultar d'utilitat
>- [Create server](https://www.postgresql.org/docs/18/sql-createserver.html)
>- [Foreign Data Wrapper](https://www.postgresql.org/docs/18/postgres-fdw.html)
>- [Import Foreign Schema](https://www.postgresql.org/docs/18/sql-importforeignschema.html)
>- [DDL Partitioning](https://www.postgresql.org/docs/18/ddl-partitioning.html)
>- [Create Table](https://www.postgresql.org/docs/18/sql-createtable.html)

## 2. Preparació de l'entorn

Modifica la informació de les bases de dades de la següent manera:

- Servidor `current`: esborra tota la informació de la taula `payment` que tingui una data de pagament **anterior** al `2007-05-01`.
  
    ```sql
    DELETE FROM payment WHERE payment_date < '2007-05-01';
    ```
- Servidor `history`: esborra tota la informació de la taula `payment` que tingui una data de pagament **igual o superior** al `2007-05-01`.

    ```sql
    DELETE FROM payment WHERE payment_date >= '2007-05-01';
    ```

- Servidor `gateway`: esborra taula `payment` sencera (contingut i estructura)
  
    ```sql
    DROP TABLE payment CASCADE;
    ```

## 3. Importació de taules foranes

Al servidor `gateway` importar les següents taules:
- `payment_history`: aquesta taula hereta tota la informació de la taula `payment` que conté el servidor `history`
- `payment_current`: aquesta taula hereta tota la informació de la taula `payment` que conté el servidor `current`

Primer de tot ens cal definir una connexió des del servidor postgres local cap al servidor postgres remot, per tant procedim a seguir la documentació oficial (https://www.postgresql.org/docs/18/sql-createserver.html) executem la següent comanda:

```sql
CREATE SERVER postgres_fdw 
FOREIGN DATA WRAPPER srvHistory_fdw 
OPTIONS (host 'ip-history', dbname 'dvdrental', port '5432');
```

Això ens hauria de crear una connexió cap a un servidor remot, de tal manera que el servidor local es pugui comunicar de forma nativa amb el remot, però ens dona un error:

>[!CAUTION]
>
>```sql
>ERROR:  foreign-data wrapper "srvhistory_fdw" does not exist
>```

Accedim a la documentació sobre els foreign data wrappers (https://www.postgresql.org/docs/18/postgres-fdw.html) i trobem el que necessitem per poder donar d’alta aquests serveis.

Primer de tot ens cal l’extensió que habilita els foreign data wrappers:

```sql
CREATE EXTENSION postgres_fdw;
```

Amb la extensió activada, podem donar d’alta un servidor remot:

```sql
CREATE SERVER srvHistory 
FOREIGN DATA WRAPPER postgres_fdw
OPTIONS (host 'ip-history', port '5432', dbname 'dvdrental');
```

Ara cal definir els permisos que farem servir en remot:

```sql
CREATE USER MAPPING FOR postgres
SERVER srvHistory 
OPTIONS (user 'postgres', password 'postgres');
```

Finalment, ja podem importar la taula i canviar-ne el nom: (https://www.postgresql.org/docs/18/sql-importforeignschema.html):

```sql
IMPORT FOREIGN SCHEMA public LIMIT TO (payment) 
FROM SERVER srvHistory INTO public;

ALTER TABLE payment RENAME TO payment_history;
```

Hauriem de fer el mateix procediment pero amb `current`

## 4. Herència múltiple

Accedeix a servidor `gateway` i crea la taula `payment_complete`, fent que tant `payment_history` i `payment_current` n’heretin de `payment_complete`.

Ara que tenim les taules remotes accessibles de forma local (només lectura des de “gateway”, però els canvis que es fan als servidors remots es veuen des del local), procedirem a crear-ne una de nova que contindrà tota la informació d'ambdues taules. Aquesta part és força senzilla si ens fixem en el que diu la documentació sobre particions (https://www.postgresql.org/docs/18/ddl-partitioning.html) on trobem exemples i ampliem amb la documentació sobre creació de taules (https://www.postgresql.org/docs/18/sql-createtable.html) que conté informació sobre herències:

El més important és tenir clar que una taula heretada mostrarà tota la informació d’aquelles que n’hereten; és a dir, payment_current i payment_history hereten de payment_complete i, per tant, una consulta a payment_complete mostrarà la informació de les altres dues taules; justament al revés del que es podria pensar en un principi, sobretot si es pensa en com funcionen les herències en un llenguatge de programació (com `Java` o `C#`).


Procedim a crear la nova taula i a modificar-ne les dues anteriors per activar-ne l’herència:


```sql
CREATE TABLE public.payment_complete (
	payment_id serial4 NOT NULL,
	customer_id int2 NOT NULL,
	staff_id int2 NOT NULL,
	rental_id int4 NOT NULL,
	amount numeric(5, 2) NOT NULL,
	payment_date timestamp NOT NULL,
	CONSTRAINT payment_pkey PRIMARY KEY (payment_id)
);

ALTER TABLE public.payment_current INHERIT public.payment_complete;
ALTER TABLE public.payment_history INHERIT public.payment_complete;
```

Ara, si fem una consulta a `payment_complete`, veurem tots els registres que tenen `payment_current` i `payment_history`
