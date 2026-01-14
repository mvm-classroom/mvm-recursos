# Exemple Markdown
Exemple amb una petita mostra de les diferents opcions de format amb markdown

## Exemple de les diverses opcions que ens dona markdown per formatar text

# Capçalera H1
## Capçalera H2
### Capçalera H3
#### Capçalera H4
##### Capçalera H5
###### Capçalera H6

---
Línia separadora
---

Es pot etiquetar text com *cursiva*, **negreta** o ***ambdues***

Es pot etiquetar `codi o paraules clau en una línia`

o etiquetar un bloc sencer com a codi

```java
// Exemple de codi Java

@DeleteMapping("/{id}")
    public ResponseEntity<?> remove(@PathVariable Long id){
        Optional<Grupo> optGrupo = service.findById(id);
        if (optGrupo.isPresent()){
            service.delete(id);
            return ResponseEntity.noContent().build();
        }
        return ResponseEntity.notFound().build();
    } 
```

```python
# Exemple de codi Python

def process_directory(input_dir, extension='jpg'):
    output_dir = os.path.join(input_dir, 'transparent_bg_rembg')
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(f'.{extension.lower()}'):
            rutaOrigen = os.path.join(input_dir, filename)
            output_filename = f"no_bg_{os.path.splitext(filename)[0]}.png"  # Siempre PNG
            rutaDestino = os.path.join(output_dir, output_filename)
            procesarImagen(rutaOrigen, rutaDestino)
```
> [!Note] 
> ### Podem definir una secció de notes
> - nota 1
> - nota 2
> - nota 3
>

> [!Note] 
> ### Les notes poden incloure blocs de codi
> ```python
> rutaDestino = os.path.join(output_dir, output_filename)
> procesarImagen(rutaOrigen, rutaDestino)
> ```

## Tipus de seccions de notes que podem fer servir

> [!NOTE]
> Informació que pot valdre la pena tenir en compte

> [!TIP]
> Consells, bones pràctiques o qualsevol informació que pot ser d'ajuda

> [!IMPORTANT]
> Informació que volem remarcar com molt necessària o crucial

> [!WARNING]
> Avisos a tenir en compte encara que no siguin errors, riscos potencials

> [!CAUTION]
> Catàstrofe imminent, perill assegurat, error garantit, apocalipsi

## Altres tipus de contingut que podem afegir

### Una checklist
- [ ] Element de la checklist desmarcat
- [x] Element de la checklist marcat

### Representar un `.stl`

```stl
solid cube_corner
  facet normal 0.0 -1.0 0.0
    outer loop
      vertex 0.0 0.0 0.0
      vertex 1.0 0.0 0.0
      vertex 0.0 0.0 1.0
    endloop
  endfacet
  facet normal 0.0 0.0 -1.0
    outer loop
      vertex 0.0 0.0 0.0
      vertex 0.0 1.0 0.0
      vertex 1.0 0.0 0.0
    endloop
  endfacet
  facet normal -1.0 0.0 0.0
    outer loop
      vertex 0.0 0.0 0.0
      vertex 0.0 0.0 1.0
      vertex 0.0 1.0 0.0
    endloop
  endfacet
  facet normal 0.577 0.577 0.577
    outer loop
      vertex 1.0 0.0 0.0
      vertex 0.0 1.0 0.0
      vertex 0.0 0.0 1.0
    endloop
  endfacet
endsolid
```

### Fer referències a coordenades en un mapa

```geojson
{
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [2.2289405, 41.4236835]
  },
  "properties": {
    "name": "Institut Manuel Vázquez Montalbán"
  }
}
```

```geojson
{
  "type": "Feature",
  "geometry": {
    "type": "LineString",
    "coordinates": [
      [2.2289405, 41.4236835],
      [2.2348467, 41.4268907]       
    ]
  },
  "properties": {
    "name": "Podem traçar una línia entre dos punts d'una mapa"
  }
}
```

Per més informació sobre com funcionen els mapes a markdown, podeu investigar sobre els formats `GeoJSON` i `TopoJSON`
