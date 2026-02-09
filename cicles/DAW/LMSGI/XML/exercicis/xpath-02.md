# Més exercicis XPath (ara amb muntanyes, deserts i aeroports)

Fent servir `BaseX` amb el fitxer [mondial_geo_accidents.xml](../recursos/mondial_geo_accidents.xml), executeu les consultes XPath necessàries per trobar:

## Nivell 1
1. Obtenir el nom de tots els deserts llistats al fitxer.
2. Obtenir l'atribut `type` (tipus) del desert "Aralkum".
3. Obtenir l'elevació de la muntanya anomenada "Musala".
4. Obtenir tots els codis IATA dels aeroports.
5. Obtenir el nom de les muntanyes que pertanyen a la serralada anomenada "Balkan".
6. Obtenir la latitud del desert "Gobi".
7. Obtenir el nom de l'aeroport que té l'atribut `city` igual a "cty-Yemen-Aden".
8. Obtenir el valor de l'àrea del desert "Sahara" (o "Great Sandy Desert" si el Sahara no hi és). *Nota: Fes servir "Great Sandy Desert" per assegurar resultat.*
9. Obtenir l'identificador (`id`) de totes les muntanyes.
10. Seleccionar l'element `<name>` de tots els accidents geogràfics de tipus `<desert>`.

## Nivell 2

11. El nom de les muntanyes que superen els 2500 metres d'elevació.
12. El nom dels deserts que tenen una àrea superior a 100.000.
13. El nom dels aeroports que tenen un desplaçament horari (`gmtOffset`) negatiu (menor que 0).
14. El nom dels deserts que són de tipus "sand" (sorra).
15. El nom de les muntanyes situades al país amb codi "GR" (Grècia).
16. Els identificadors dels deserts que contenen la paraula "Erg" al seu nom.
17. El nom de les muntanyes que NO tenen assignada una serralada (no tenen l'element `<mountains>`).
18. Els aeroports que es troben a una elevació entre 100 i 500 metres.
19. El nom dels mars que limiten amb el "sea-Nordsee" (Mar del Nord).
20. El nom de les muntanyes que tenen una latitud major de 45.

### Nivell 3

21. Comptar quantes muntanyes hi ha registrades al fitxer.
22. Calcular la suma total de l'àrea de tots els deserts.
23. Obtenir el nom de l'últim desert que apareix al document XML.
24. Obtenir el nom del desert que apareix immediatament abans del desert "Gobi".
25. Obtenir l'identificador de l'element pare del nom "Kyllini".
26. El nom de tots els elements (siguin mars, muntanyes, etc.) que tenen un atribut `country` amb valor "F" (França).
27. Seleccionar el segon element `<located>` dins del mar "Atlantic Ocean".
28. El nom dels deserts que tenen definit un tipus (`@type`) I TAMBÉ tenen una àrea superior a 50000.
29. El nom de l'aeroport que està llistat just després de l'aeroport "Aden Intl".
30. Els noms de les muntanyes on la longitud és menor que 20 o l'elevació és superior a 2800.
