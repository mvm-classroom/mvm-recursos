# Manteniment d'un SGBD

## Descripció
- Objectiu: Posar en pràctica els mecanismes de gestió dels SGBDs per a millorar-ne el rendiment i mantenir-ne controlat el seu consum de disc i memòria
- Desenvolupament: Grupal
- Lliurament: Repositori en markdown que contingui tota la documentació i una presentació

## Preparació
- Màquina client: Es recomana `Ubuntu Desktop` amb `pgAdmin` instal.lat
- Màquina servidora: Pot ser una `Ubuntu Server` amb `PostgreSQL` `17` o `18` instal.lat.

## Restauració amb pgAdmin

Crear una base de dades i restaurar la copia que trobareu a [dades.backup](../Recursos/dades.backup) fent servir `pgAdmin`.

## Explain + Analyze

- Investigar i documentar-se sobre l'eina `Explain` i `Analyze` de `pgAdmin`

- Feu-la servir per analitzar una consulta com, per exemple, aquesta:

```sql
SELECT * FROM city ci INNER JOIN country co ON ci.countrycode=co.code WHERE ci.population BETWEEN 1000 AND 5000 ORDER BY ci.id;
```

- Mostreu el `query plan` i estudieu-lo per localitzar en quins punts de la consulta creieu que poden haver-hi colls d'ampolla.

- Expliqueu la diferència entre els conceptes `cost`, `time`, `rows`, `width`. 
- Quin o quins valors creieu que poden ser més rellevants per mesurar el rendiment de la consulta?

## Millores de rendiment fent servir índexs

- Expliqueu el que es un índex i com el podeu fer servir per millorar el rendiment de la consulta anterior.

- Detalleu la diferència entre índexs de tipus `cluster` i `no cluster`

### Feu servir un índex de tipus `NO cluster`

### Feu servir un índex de tipus `cluster`

## Vacuum

- Expliqueu el que fa l'eina `vacuum`

- Localitzeu on podeu veure la mida física en disc de la taula `city`
- Executeu la query 
    ```sql
    DELETE FROM city WHERE id NOT IN (SELECT capital FROM country WHERE capital IS NOT NULL);
    ```
    i comproveu si s'allibera espai

- Feu servir `vacuum` i torneu a comprovar-ho