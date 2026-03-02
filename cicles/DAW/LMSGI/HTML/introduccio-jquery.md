# Introducció a jQuery

## Què es `jQuery`?

`jQuery` es una llibreria de `Javascript` que ens proporciona una sèrie d'eines *precuinades*

Es a dir, no es un nou llenguatge de programació, continuareu fent servir `Javascript` però amb alguna petita ajuda.

## Què permet fer?

Nosaltres només el farem servir per manipular lleugerament el DOM (trobar i modificar certs elements), pero també permet:

- Detectar events
- Efectes per mostrar/ocultar elements
- Integració amb AJAX

## Còm el començo a fer servir?

Si vols anar per feina i començar a fer-lo servir ja, només has d'incloure al `<body>` del teu document `html` una línia com aquesta:

```html
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
```

Amb aixó ja tindràs a la teva disposició el conjunt d'eines de `jQuery`

Amb les presses no oblidis dir-li al teu script amb `jQuery` que s'esperi a que la pàgina hagi carregat per complet, altrament, no tindrem tots els elements disponibles.

```javascript
$(document).ready(function() {
    //El nostre codi jQuery
});
```

## Sintaxi

La sintaxi bàsica de `jQuery` es

```javascript
$(selector).accio();
```

o amb un exemple més concret

```javascript
$("p").hide();
```

- `$`: Això vol dir que estem invocant `jQuery`
- `("p")`: Sel.leccionem tots els elements del DOM que siguin de tipus `<p>`
- `.hide()`: Amaguem tots els elements recuperats pel sel.lector anterior

>[!TIP]
>L'equivalent a aixó en `Javascript` pur, sense `jQuery`, podria ser:
>
>```javascript
>let paragrafs = document.querySelectorAll("p");
>for (let i = 0; i < paragrafs.length; i++) {
>    paragrafs[i].style.display = "none";
>}
>```
>

Podem sel.leccionar elements pel seu ID

```javascript
$("#boto-mode-fosc")
```

o per la seva classe

```javascript
$(".taula-horari")
```

## Exemples

Manipular la visiblitat dels elements del DOM

```javascript
// Oculta l'element amb ID "caixa" al clicar al botó amb ID "btn-ocultar"
$("#btn-ocultar").click(function() {
    $("#caixa").hide();
});

// Mostra l'element amb ID "caixa" al clicar al botó amb ID "btn-mostrar"
$("#btn-mostrar").click(function() {
    $("#caixa").show();
});

// Alterna la la visibiltat amb un únic botó i una única acció
$("#boto-amaga-mostra").click(function() {
    $("#caixa").toggle(); 
});
```

Manipular la classe d'elements del DOM

```javascript
//Fem servir un botó per afegir una classe i treure una altra
$("#boto-fosc").hover(function() {
    $(".graella").addClass("mode-fosc");
    $(".graella").removeClass("mode-clar");
});

// Resalta una fila d'una taula al passar el ratolí per sobre
$("tr").hover(function() {
    $(this).toggleClass("fila-resaltada");
});
```

Manipular el contingut HTML directament

```javascript
// Cambiar el text d'un títol
$("#boto-canvia-contingut").click(function() {
    $("#titol-principal").text("Hem canviat el titol amb jQuery");
    
    //Afegir contingut html a un div existent 
    $("#div-missatge").html("Podem afegir html com, per exemple, <strong>text amb l'etiqueta strong</strong>");
});
```