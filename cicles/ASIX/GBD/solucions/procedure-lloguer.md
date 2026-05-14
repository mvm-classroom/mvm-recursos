### 5.2 Controlar el procés de lloguer

Volem controlar el procediment del lloguer de pel.lícules per evitar que es donin situacions absurdes com que un client que no està actiu llogui una pel.lícula sense posar-se al dia en la seva suscripció.

El fet de llogar una pel.lícula, en principi implica:
- Inserir un registre a la taula `rental`
- Inserir un registre a la taula `payment`

El que farem es controlar, mitjançant l'ús de `PROCEDURES` i `TRANSACCIONS`, si es fa un insert a la taula `rental`:
- Si el client no està actiu, farem un `ROLLBACK` de la transacció i llançarem un missatge d'error
- Si el client està actiu, permetrem fer-ne el pagament i, si tot va bé, farem el `COMMIT`

#### Solució

```sql
CREATE OR REPLACE PROCEDURE processar_lloguer(
    p_inventari_id INT,
    p_client_id INT,
    p_empleat_id INT,
    p_quantitat NUMERIC
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_lloguer_id INT;
    v_client_actiu INT;
BEGIN
    --Fem l'insert del lloguer
    --Fem servir RETURNING perquè PostgreSQL ens retorni l'ID del lloguer que acaba de crear.
    INSERT INTO rental (rental_date, inventory_id, customer_id, staff_id)
    VALUES (NOW(), p_inventari_id, p_client_id, p_empleat_id)
    RETURNING rental_id INTO v_lloguer_id;

    --Comprovem si el client està actiu?
    SELECT active INTO v_client_actiu 
    FROM customer 
    WHERE customer_id = p_client_id;

    --Lògica de la Transacció
    IF v_client_actiu = 0 THEN
        --Si es 0, el client està inactiu.
        --Executem ROLLBACK per tornar enrere (carregar partida). Es com si tornèssim enrere en el temps i l'insert que hem fet abans mai hagués passat.
        ROLLBACK;
        
        --Llancem un missatge d'error per avisar l'usuari/aplicació.
        RAISE EXCEPTION 'Operació cancel·lada: El client % està inactiu. No s''ha registrat ni el lloguer ni el cobrament.', p_client_id;
    END IF;

    --Si hem arribat a aquest punt, es que el client està actiu
    --Ara inserim el pagament, vinculant-lo a l'ID del lloguer (v_lloguer_id).
    INSERT INTO payment (customer_id, staff_id, rental_id, amount, payment_date)
    VALUES (p_client_id, p_empleat_id, v_lloguer_id, p_quantitat, NOW());

    --Si tot ha anat bé, confirmem els canvis permanentment.
    COMMIT;
    
    --I mostrem notificació
    RAISE NOTICE 'Èxit: Lloguer (ID: %) i pagament processats correctament.', v_lloguer_id;
END;
$$;
```

### Com provar això a la terminal?

**Prova A: Client Inactiu (Força el ROLLBACK)**
*(Suposem que el client 16 està inactiu a la teva base de dades).*
```sql
CALL processar_lloguer_segur(10, 16, 1, 4.99);
```
*Resultat:* Donarà un error "Operació cancel·lada: El client 16 està inactiu...". Si vas a mirar la taula `rental`, veuràs que no s'ha inserit res. El `ROLLBACK` ens ha salvat.

**Prova B: Client Actiu (Força el COMMIT)**
*(Suposem que el client 1 està actiu).*
```sql
CALL processar_lloguer_segur(10, 1, 1, 4.99);
```
*Resultat:* Llançarà el missatge d'"Èxit". Si busques a la teva base de dades, veuràs una nova fila a `rental` i una altra fila a `payment` perfectament enllaçades.
