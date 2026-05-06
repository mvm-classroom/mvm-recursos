# Odoo 18 dockeritzat

## Instal.lació de docker
Instal.larem docker seguint la [documentació oficial](https://docs.docker.com/engine/install/ubuntu/)

## Directori de treball
```shell
mkdir odoo18
```

```shell
cd odoo18
```

```shell
mkdir ./config ./addons ./data/postgres
```

```shell
nano docker-compose.yml
```

```yaml
services:
  db:
    image: postgres:16
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_PASSWORD=odoo_password
      - POSTGRES_USER=odoo
      - PGDATA=/var/lib/postgresql/data/pgdata
    volumes:
      - odoo-db-data:/var/lib/postgresql/data/pgdata
    restart: always

  odoo:
    image: odoo:18.0
    depends_on:
      - db
    ports:
      - "8069:8069"
      - "8072:8072"
    environment:
      - HOST=db
      - USER=odoo
      - PASSWORD=odoo_password
    volumes:
      - ./addons:/mnt/extra-addons
      - ./config:/etc/odoo
      - odoo-web-data:/var/lib/odoo
    restart: always

volumes:
  odoo-db-data:
  odoo-web-data:
```

```shell
docker compose up -d
```
ens donarà una sortida semblant a

```shell
[+] up 34/34
 ✔ Image odoo:18.0             Pulled                                      34.6s
 ✔ Image postgres:16           Pulled                                      14.6s
 ✔ Network odoo18_default      Created                                     0.0s
 ✔ Volume odoo18_odoo-web-data Created                                     0.0s
 ✔ Volume odoo18_odoo-db-data  Created                                     0.0s
 ✔ Container odoo18-db-1       Started                                     4.6s
 ✔ Container odoo18-odoo-1     Started                                     0.5s
```

Si tot s'aixecat correctament, podem provar d'accedir a `http://localhost:8069`

Si vols crear una nova base de dades, elminar l'actual o escollir entre les que tinguis, pots fer servir l'enllaç `http://10.2.85.135:8069/web/database/selector`
