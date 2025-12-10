# Exercicis XML 3: DTD

## Primera part
Per cadascun dels formats següents, defineix el DTD que validaría el format que conté

### Format `Client 1`

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
### DTD `Client 1`
Defineix aquí el DTD corresponent al format `Client 1`

### Comprovació
- Modifica el fitxer `XML` per que faci servir el `DTD` que has definit.
- Fent servir la validació `XML` del `Visual Studio Code` (amb l'extensió `XML Language Support by Red Hat`), comprova que qualsevol canvi que no concordi amb el `DTD` es mostra com error.
- Torna a deixar el document amb el contingut correcte.

### Format `Client 2`:

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

### DTD `Client 2`
Defineix aquí el DTD corresponent al format `Client 2`

### Comprovació
- Modifica el fitxer `XML` per que faci servir el `DTD` que has definit.
- Fent servir la validació `XML` del `Visual Studio Code` (amb l'extensió `XML Language Support by Red Hat`), comprova que qualsevol canvi que no concordi amb el `DTD` es mostra com error.
- Torna a deixar el document amb el contingut correcte.

## Segona part
Genera el `DTD`, en forma de fitxer extern, que defineixi l'estructura del següent `XML` tenint en compte que ara inclou _namespaces_.

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<arrel  xmlns="http://www.chus.xml.institutmvm.cat/default" 
        xmlns:c="http://www.chus.xml.institutmvm.cat/concerts" 
        xmlns:t="http://www.chus.xml.institutmvm.cat/teatre">
	<c:esdeveniments>
		<c:esdeveniment>
			<c:grup>Ladilla Rusa</c:grup>
			<c:lloc>Sala Razzmatazz</c:lloc>
			<c:data>2025-12-10 22:30</c:data>
			<c:entrada gratuita="si"/>
		</c:esdeveniment>
		<c:esdeveniment>
			<c:grup>Ruïnosa y las Strippers de Rahola</c:grup>
			<c:lloc>Sala Apolo 2</c:lloc>
			<c:data>2025-11-30 21:45</c:data>
			<c:entrada gratuita="no">10</c:entrada>
		</c:esdeveniment>
		<c:esdeveniment>
			<c:grup>Los Ganglios</c:grup>
			<c:lloc>Sala Apolo 1</c:lloc>
			<c:data>2026-01-12</c:data>
			<c:entrada gratuita="no">12.5</c:entrada>
		</c:esdeveniment>
	</c:esdeveniments>

	<t:esdeveniments>
		<t:esdeveniment>
			<t:companyia>Ultrashow</t:companyia>
			<t:lloc>Teatre Goya</t:lloc>
			<t:data>2025-11-14 23:00</t:data>
			<t:entrada>15€ + 2,5€ de gestión online</t:entrada>
		</t:esdeveniment>
		<t:esdeveniment>
			<t:companyia>Els Malvats</t:companyia>
			<t:lloc>Teatre Gaudí</t:lloc>
			<t:data>2025-11-29 20:00</t:data>
			<t:entrada>22€ </t:entrada>
		</t:esdeveniment>	
	</t:esdeveniments>
</arrel>
```

### Comprovació
- Modifica el fitxer `XML` per que faci servir el `DTD` que has definit.
- Fent servir la validació `XML` del `Visual Studio Code` (amb l'extensió `XML Language Support by Red Hat`), comprova que qualsevol canvi que no concordi amb el `DTD` es mostra com error.
- Torna a deixar el document amb el contingut correcte.
