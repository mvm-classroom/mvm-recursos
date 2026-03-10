# HA amb PostgreSQL

Ens hem trobat un repositori anomenat `ha-postgresql` amb aquests fitxers

`Dockerfile`

```Dockerfile
FROM postgres:15-bullseye

USER root

RUN apt-get update && \
    apt-get install -y patroni python3-etcd curl && \
    rm -rf /var/lib/apt/lists/*

USER postgres

CMD ["patroni", "/patroni.yml"]
```

`patroni.yml`

```yml
scope: mi_cluster_ha
namespace: /db/
restapi:
  listen: 0.0.0.0:8008
etcd:
  host: etcd:2379
bootstrap:
  dcs:
    ttl: 30
    loop_wait: 10
    retry_timeout: 10
    maximum_lag_on_failover: 1048576
    postgresql:
      use_pg_rewind: true
  initdb:
    - auth-host: scram-sha-256
    - auth-local: trust
    - encoding: UTF8
  users:
    admin:
      password: adminpassword
      options:
        - createrole
        - createdb
postgresql:
  listen: 0.0.0.0:5432
  data_dir: /var/lib/postgresql/data/patroni
  pg_hba:
    - host replication replicator all scram-sha-256
    - host all all all scram-sha-256
  authentication:
    replication:
      username: replicator
      password: replicatorpassword
    superuser:
      username: postgres
      password: adminpassword
```

`haproxy.cfg`

```ini
global
    maxconn 100

defaults
    log global
    mode tcp
    retries 2
    timeout client 30m
    timeout connect 4s
    timeout server 30m
    timeout check 5s

listen stats
    mode http
    bind *:7000
    stats enable
    stats uri /

listen postgres
    bind *:5432
    option httpchk GET /primary
    http-check expect status 200

    default-server inter 3s fall 3 rise 2 on-marked-down shutdown-sessions

    server pg-1 pg-1:5432 maxconn 100 check port 8008
    server pg-2 pg-2:5432 maxconn 100 check port 8008
```

`docker-compose.yml`

```yaml
networks:
  ha-net:
    driver: bridge

services:
  # Etcd
  etcd:
    image: quay.io/coreos/etcd:v3.5.9
    container_name: etcd
    networks:
      - ha-net
    environment:
      - ETCD_LISTEN_CLIENT_URLS=http://0.0.0.0:2379
      - ETCD_ADVERTISE_CLIENT_URLS=http://etcd:2379
      - ETCD_ENABLE_V2=true

  # Node 1
  pg-1:
    build: .
    container_name: pg-1
    networks:
      - ha-net
    volumes:
      - ./patroni.yml:/patroni.yml:ro
      - pg_1_data:/var/lib/postgresql/data
    environment:
      - PATRONI_NAME=pg-1
      - PATRONI_RESTAPI_CONNECT_ADDRESS=pg-1:8008
      - PATRONI_POSTGRESQL_CONNECT_ADDRESS=pg-1:5432
    depends_on:
      - etcd

  # Node 2
  pg-2:
    build: .
    container_name: pg-2
    networks:
      - ha-net
    volumes:
      - ./patroni.yml:/patroni.yml:ro
      - pg_2_data:/var/lib/postgresql/data
    environment:
      - PATRONI_NAME=pg-2
      - PATRONI_RESTAPI_CONNECT_ADDRESS=pg-2:8008
      - PATRONI_POSTGRESQL_CONNECT_ADDRESS=pg-2:5432
    depends_on:
      - etcd

  # HAproxy
  haproxy:
    image: haproxy:alpine
    container_name: haproxy
    ports:
      - "5432:5432"
      - "7000:7000"
    networks:
      - ha-net
    volumes:
      - ./haproxy.cfg:/usr/local/etc/haproxy/haproxy.cfg:ro
    depends_on:
      - pg-1
      - pg-2

volumes:
  pg_1_data:
  pg_2_data:
```

Pero només hi han aquests fitxer y prou.

Ens toca esbrinar:

- Qué es pretén fer amb aquests fitxers?
- Quines tecnologies fa servir i perqué serveix cadascuna?
- Com podem verificar si tot aixó funciona?

Ja que hem invertit temps en investigar tot aixó, farem el següent:

- Personalitzar els fitxers perque no facin servir passwords genérics
- Crear un repositori amb els nostres fitxers
- Crear un readme.md explicant tot el procés i les proves
 

>[!TIP]
>Per treballar amb `docker` i `docker compose` podeu instal.lar
>```shell
>sudo apt install docker.io docker-compose-v2 -y
>```

>[!TIP]
>Per arrencar tots els contenidors orquestrats per `docker compose` ho podeu fer amb
>```shell
>docker compose up -d
>```
>o amb
>```shell
>docker compose up -d --build
>```
>si heu de repetir algun pas i voleu forçar a que es torni a generar la imatge a partir del `Dockerfile`

>[!TIP]
>Proveu aixó i investigueu què vol dir
>```shell
>docker exec -it pg-1 patronictl -c /patroni.yml list
>```
>
>També podeu provar d'accedir a `http://ip-de-la-maquina-amfitriona:7000`

