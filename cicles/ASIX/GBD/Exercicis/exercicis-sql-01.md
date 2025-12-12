# Exercicis SQL: Consultes a la base de dades Pagila
**Objectiu:** Practicar sentències SELECT bàsiques, filtratge, ordenació i funcions d'agregació;

---

### 1. Consultes Bàsiques (SELECT)
1.  Selecciona totes les dades de la taula d'actors (`actor`).
2.  Selecciona només el nom (`first_name`), cognom (`last_name`) i el correu electrònic (`email`) de tots els clients (`customer`).
3.  Selecciona el títol (`title`) i la descripció (`description`) de totes les pel·lícules (`film`).

---

### 2. Filtratge de Dades (WHERE)
4.  Selecciona totes les pel·lícules que tinguin una classificació (`rating`) de 'G'.
5.  Selecciona totes les pel·lícules que durin (`length`) més de 120 minuts.
6.  Troba els pagaments (`payment`) on l'import (`amount`) sigui exactament 0.99.
7.  Selecciona les pel·lícules que tinguin una durada de lloguer (`rental_duration`) de 3 dies o de 5 dies.

---

### 3. Funcions d'Agregació (COUNT, SUM, AVG, MIN/MAX)
8.  Quantes pel·lícules hi ha registrades en total a la taula `film`?
9.  Calcula el total de diners recaptats registrats a la taula de pagaments (`payment`).
10. Quina és la durada mitjana (`length`) de totes les pel·lícules de la base de dades?
11. Quin és el cost de reemplaçament (`replacement_cost`) més alt i el més baix de les pel·lícules?

---

### 4. Ordenació de Resultats (ORDER BY)
12. Llista els títols de les pel·lícules ordenats alfabèticament (A-Z).
13. Llista els clients ordenats pel seu cognom (`last_name`) de forma descendent (Z-A).
14. Mostra les pel·lícules ordenades per durada (`length`), de la més llarga a la més curta.

---

### 5. Limitació de Resultats (LIMIT)
15. Mostra només les 5 primeres files de la taula d'actors (`actor`).
16. Mostra els 10 pagaments (`payment`) amb l'import (`amount`) més alt (requereix ordenar primer).

---

### 6. Exercicis Combinats
17. Troba les 5 pel·lícules més llargues que tinguin una classificació (`rating`) de 'PG-13'.
18. Calcula la mitjana de l'import dels pagaments, però tenint en compte només aquells pagaments superiors a 5.99.
19. Troba el títol i el cost de reemplaçament de les 3 pel·lícules més barates de reemplaçar (`replacement_cost`), però que la seva durada sigui superior a 100 minuts.
20. Compta quants clients estan "actius" (camp `active` = 1) i tenen una adreça de correu electrònic que comença per la lletra 'M' (Pista: utilitza `LIKE 'M%'`).