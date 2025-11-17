# Exercicis XML 2: Namespaces

## 0. Enunciat
Som el proveïdor que dona servei a diferents clients del món de l’espectable i disposem d’una aplicació que n’enregistra els esdeveniments que volen programar perquè la gent els pugui consultar i comprar-ne les entrades.

Fa temps que treballem amb el `Client 1` i la nostra aplicació processa els seus fitxers sense cap problema. Però tot just ara que acabem de començar a treballar amb el `Client 2`, ens trobem que la nostra aplicació no és capaç de processar els seus fitxers XML.

### Exemple d'un fitxer del `Client 1`:

```xml
<esdeveniments>
	<esdeveniment>
		<grup>Ladilla Rusa</grup>
		<lloc>Sala Razzmatazz</lloc>
		<data>2025-12-10 22:30</data>
		<entrada gratuita="si"/>
	</esdeveniment>
	<esdeveniment>
		<grup>Ruïnosa y las Strippers de Rahola</grup>
		<lloc>Sala Apolo 2</lloc>
		<data>2025-11-30 21:45</data>
		<entrada gratuita="no">10</entrada>
	</esdeveniment>
	<esdeveniment>
		<grup>Los Ganglios</grup>
		<lloc>Sala Apolo 1</lloc>
		<data>2026-01-12</data>
		<entrada gratuita="no">12.5</entrada>
	</esdeveniment>
</esdeveniments>
```

### Exemple d'un fitxer del `Client 2`:

```xml
<esdeveniments>
	<esdeveniment>
		<companyia>Ultrashow</companyia>
		<lloc>Teatre Goya</lloc>
		<data>2025-11-14 23:00</data>
		<entrada>15€ + 2,5€ de gestión online</entrada>
	</esdeveniment>
	<esdeveniment>
		<companyia>Els Malvats</companyia>
		<lloc>Teatre Gaudí</lloc>
		<data>2025-11-29 20:00</data>
		<entrada>22€</entrada>
	</esdeveniment>	
</esdeveniments>
```

Examina els dos exemples atentament i, a continuació, respon a les següents preguntes:

## Preguntes

### 1. Identificar el problema
Per quin motiu creus que el fitxer Exemple 1 i Exemple 2 entren en conflicte, és a dir, per què la nostra aplicació pot processar Exemple 1 i no pas Exemple 2. 

### 2. Plantejar la solució
Explica quin mètode podem fer servir amb XML per evitar el conflicte i raona la resposta.

### 3. Detallar l'implementació de la solució
Explica en detall quins passos hem de seguir per a poder aplicar el mètode que has explicat anteriorment. 

### 4. Fitxer d'exemple integrant tots els elements amb la solució planejada
Hem fet proves sobre els canvis aplicats i tot funciona perfectament, però  volem fer un experiment: fusiona els dos fitxers XML en un de sol i aplica els espais de noms adients a totes les etiquetes perquè no hi hagi conflicte entre elles, enganxa aquí el codi font resultant.
