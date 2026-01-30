# TUIs SQL

Per no haver de dependre d'una SO amb entorn gràfic per fer servir una eina amb `GUI` (Graphical User Interface), podem instal.lar, directament al nostre servidor, una `TUI` (Terminal User Interface) per treballar una mica mès àgils que amb el terminal que ens dona, per exemple `psql`.

## harlequin
`harlequin` es un TUI dissenyat per treballar amb bases de dades SQL

### Instal.lació

Si no tenim instal.lat el gestor de paquets `uv` el podem instalar fent

```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Quan ja tenim `uv` podem executar, per exemple:

```shell
uv tool install "harlequin[postgres]"
```

Aixó instal.larà `harlequin` amb l'adaptador necessari per treballar amb `PostgreSQL`

## Execució
```shell
harlequin -a postgres "postgres://postgres:postgres@localhost:5432/pagila"
```



