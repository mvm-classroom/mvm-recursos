# Instal.lació i configuració d'un NIDS/NIPS amb Suricata

En aquesta activitat prepararem una petita simulació del funcionament d'un NIDS/NIPS
Farem servir Suricata per monitoritzar el tràfic entre dos màquines que anomenarem `atacant` i `victima`
Per forçar que el tràfic entre ambdues màquines es visible per Suricata, farem servir una tercera màquina, que anomerarem `nids-nips` que farà de *gateway* entre elles.

## Preparació de l'escenari a IsardVDI

El nostre escenari haura de permetre una simulació com la mostrada a [aquest diagrama](https://editor.p5js.org/ChusVazquez/full/j2OubAKER)

Necessitarem 3 màquines amb aquestes característiques en comú:

|           |                             |
| --------- | --------------------------- |
| Plantilla | `MVM - Ubuntu 24.04 Server` |
| RAM       | `4GB`                       |
| vCPUs     | `2`                         |


### Màquina `atacant`
Interficies de xarxa:

| Interficie | Nom       | Descripció                                                                                              |
| ---------- | --------- | ------------------------------------------------------------------------------------------------------- |
| `enp1s0`   | Default   | La fem servir per donar connectivitat a internet a la màquina per si hem d'instalar alguna eina         |
| `enp2s0`   | Wireguard | La fem servir per accedir fàcilment a la màquina sense modificar la resta de la configuració de xarxa   |
| `enp3s0`   | Personal1 | Es la que ens interessa a efectes de l'exercici, ja que es la que connecta amb la màquina intermediària |

  

### Màquina `victima`
Interficies de xarxa:

| Interficie | Nom       | Descripció                                                                                              |
| ---------- | --------- | ------------------------------------------------------------------------------------------------------- |
| `enp1s0`   | Default   | La fem servir per donar connectivitat a internet a la màquina per si hem d'instalar alguna eina         |
| `enp2s0`   | Wireguard | La fem servir per accedir fàcilment a la màquina sense modificar la resta de la configuració de xarxa   |
| `enp3s0`   | Personal2 | Es la que ens interessa a efectes de l'exercici, ja que es la que connecta amb la màquina intermediària |


### Màquina `nids-nips`
Interficies de xarxa:

| Interficie | Nom       | Descripció                                                                                            |
| ---------- | --------- | ----------------------------------------------------------------------------------------------------- |
| `enp1s0`   | Default   | La fem servir per donar connectivitat a internet a la màquina per si hem d'instalar alguna eina       |
| `enp2s0`   | Wireguard | La fem servir per accedir fàcilment a la màquina sense modificar la resta de la configuració de xarxa |
| `enp3s0`   | Personal1 | Es la connexió amb la màquina `atacant`                                                               |
| `enp4s0`   | Personal2 | Es la connexió amb la màquina `victima`                                                               |


## Configuració de xarxa

### Màquina `atacant`

Configuració de netplan

```yaml
network:
  version: 2
  ethernets:
    enp1s0: {dhcp4: true}
    enp2s0: {dhcp4: true}
    enp3s0:
      dhcp4: false
      addresses: [192.168.10.2/24]
      routes:
        - to: 192.168.20.0/24
          via: 192.168.10.1
```

### Màquina `victima`

Configuració de netplan

```yaml
network:
  version: 2
  ethernets:
    enp1s0: {dhcp4: true}
    enp2s0: {dhcp4: true}
    enp3s0:
      dhcp4: false
      addresses: [192.168.20.2/24]
      routes:
        - to: 192.168.10.0/24
          via: 192.168.20.1
```

### Màquina `nids-nips`

Configuració de netplan

```yaml
network:
  version: 2
  ethernets:
    enp1s0: {dhcp4: true}
    enp2s0: {dhcp4: true}
    enp3s0:
      dhcp4: false
      addresses: [192.168.10.1/24]
    enp4s0:
      dhcp4: false
      addresses: [192.168.20.1/24]
```

## Enrutament

### Port forwarding (redirecció de ports)
Per que la nostra màquina `nids-nips` permeti (o no, si es un atac) el tràfic entre les dues subxarxes, hem d'habilitar la redirecció de ports (port forwarding)

Aixó ho podem fer, en el nostre cas, editant el fitxer `/etc/sysctl.conf` i descomentant la línia `net.ipv4.ip_forward=1` per tal de que tingui efecte.

Aplicarem els canvis amb `sudo systclt -p`

### Instal.lació i activació de `nftables`

Com que estem fent servir Ubuntu Server 24.04, es molt probable que ja tinguem instal.lat `nftables`

Si l'haguèssim d'instal.lar seria

```shell
sudo apt install nftables -y
```

Tant si el tenim instal.lat com si acabem de fer-ho, revisem l'status

```shell
systemctl status nftables
```

i l'activem si veiem que no està `enabled`

```shell
sudo systemctl enable nftables
```

