## Solucions de les correccions a classe

**1.1**
```sql
INSERT INTO DEPARTAMENT (nom) VALUES ('Vendes');
```

**1.2**
```sql
INSERT INTO DEPARTAMENT (nom) VALUES ('Comptabilitat'), ('Recursos Humans');
```

**1.3**
```sql
INSERT INTO EMPLEAT (nom, cognom, departament_id)
VALUES ('Michael', 'Scott', 1);
```

**1.4**
```sql
INSERT INTO PRODUCTE (NomProducte, PreuUnitari) VALUES ('Grapadora', 12.50);
```

**2.1**
```sql
INSERT INTO EMPLEAT (nom, cognom, departament_id) VALUES
('Dwight', 'Schrute', 1),
('Jim', 'Halpert', 1),
('Phyllis', 'Vance', 1);
```

**2.2**
```sql
INSERT INTO PRODUCTE (NomProducte, PreuUnitari) VALUES
('Paper A4', 4.99),
('Bolígraf blau', 0.85),
('Cadira d''oficina', 89.00);
```
> Nota: l'apòstrof a `d'oficina` s'escapa duplicant-lo (`''`).

**2.3**
```sql
-- Primer esbrinem l'id de Dwight
SELECT id FROM EMPLEAT WHERE nom = 'Dwight' AND cognom = 'Schrute';

INSERT INTO CLIENT (nom_empresa, empleat_venedor_id) VALUES
('Dunder Mifflin Inc.', 2),
('Sabre Corp.', 2);
```

**3.1**
```sql
INSERT INTO CLIENT (nom_empresa, empleat_venedor_id)
VALUES ('Vance Refrigeration', 4)
RETURNING id;
```

**3.2**
```sql
INSERT INTO PRODUCTE (NomProducte, PreuUnitari)
VALUES ('Motxilla', 25.00)
RETURNING *;
```

**3.3**
```sql
INSERT INTO DEPARTAMENT (nom) VALUES ('Magatzem') RETURNING id;
-- Suposem que retorna 4
INSERT INTO EMPLEAT (nom, cognom, departament_id)
VALUES ('Darryl', 'Philbin', 4);
```

**4.1**
```sql
INSERT INTO COMANDA (Id_Client) VALUES (1);
SELECT * FROM COMANDA WHERE Id = 1;
```

**4.2**
```sql
INSERT INTO LINIA_COMANDA (Id_Comanda, Id_Producte) VALUES (1, 1);
SELECT * FROM LINIA_COMANDA WHERE Id_Comanda = 1 AND Id_Producte = 1;
-- Quantitat = 1 per defecte
```

**4.3**
```sql
INSERT INTO LINIA_COMANDA (Id_Comanda, Id_Producte, Quantitat)
VALUES (1, 2, 5);
```