# Guia bàsica GNS3

GNS3 (Graphical Network Simulator-3) és un emulador de programari lliure i de codi obert que s'utilitza per dissenyar, configurar i provar topologies de xarxa virtual i real sense necessitat de maquinari físic.
Permet als usuaris emular sistemes operatius de xarxa de proveïdors com Cisco, Juniper i Arista, per la qual cosa és ideal per a la simulació, la preparació de la certificació 
(per exemple, CCNA, CCNP) i proves.

Ens será ideal per fer laboratoris de xarxes sense disposar de tota l'infraestructura física necessària.

## Instalació
Tot i que podem instalar tant la versió amb GUI com la versió server per accedir via web, nosaltres farem servir la [OVA que ens proporcionen directament a GNS3](https://www.gns3.com/software/download-vm)

Un cop feta l'importació, configurarem la nostra VM perque tingui dues interfícies de xarxa:
- Host-Only (recorda afegir un dispositiu d'aquest tipus, com per exemple, `vboxnet0` a la configuración general de Virtual Box si no t'apareix cap)
- NAT per donar sortida a internet a la nostra VM per poder baixar imatges, actualitzar paquets, etc...

També hem d'activar l'opció `VT-x` o `AMD-V` segons el processador de la teva màquina amfitriona.

Si en el moment d'arrencar tenim un error com `VT-x is disabled in the BIOS` o `AMD-V is disabled in the BIOS` haurem d'habilitar-ho a la nostra BIOS/UEFI abans de poder continuar.

Un cop arrenquem la VM sense problemes, acabarà apareixent una pantalla amb un resum de la nostra GNS3 VM amb informació de la versió del servidor, el tipus de virtualització, etc...

Ens interesa la part on es mostra: 
- la IP (per exemple `192.168.56.101`)
- el port (per defecte `80`)
- com accedir per SSH `ssh gns3@192.168.56.101` amb el password per defecte `gns3`
- com accedir via client web `http://192.168.56.101`

Si al navegador de la nostra màquina amfitriona accedim a `http://192.168.56.101` se'ns obrirá el client web de GNS3 on ja podem començar a crear projectes, afegir plantilles, etc...

## Nodes per defecte

### Ethernet switch

Afegim un switch amb múltiples interfícies `eth` on podem connectar altres nodes del nostre projecte simulant les connexions físiques de cable ethernet a un switch real.

### NAT

Podem connectar un host o un switch a aquest tipus de node per donar-li sortida a internet. A més, proporciona servei DHCP, de manera que si a la configuració del host li habilitem, no haurem de forçar IPs estàtiques si no ho necessitem.

## Plantilles

A la pantalla inicial que trobem al accedir al client web de GNS3 podem accedir a l'opció `Go to preferences` i sel.leccionar l'opció `Docker`.

Aixó ens portarà a l'apartat `Docker container templates` on podem gestionar les plantilles.

Com no en tindrem cap, afegim una nova amb les opcions:

- Server type: Run this Docker container locally
- Docker Virtual Machine: New image -> `gns3/ubuntu:noble`
- Container name: `ubuntu-noble`
- Network adapters: `1`
- Start command: `/bin/sh`
- Console type: `telnet`
- Environment: de moment ho deixarem en blanc

Al fer `ADD TEMPLATE` ja dispondrem d'un nou tipus de node per afegir al nostre projecte.

Podem tornar al nostre projecte o crear-ne un de nou si encara no hem creat cap projecte.

Amb el botó `+` ens apareixerà a la llista de nodes per afegir, una nova opció `ubuntu-noble`


## Exemple bàsic

Farem un exemple bàsic en el que afegirem dos nodes `ubuntu-noble` conectats en una petita LAN amb un switch ethernet que a la seva vegada està connectat a un node NAT.

### Afegint nodes `ubuntu-noble`

Farem servir el nou tipus de node que hem creat per afegir dues màquines de tipus `ubuntu-noble`.

Si arrosseguem dues vegades des de la llista de nodes disponibles, ens trobarem amb un parell d'equips:
- ubuntu-noble-1
- ubuntu-noble-2

### Afegint el switch

Afegim un node de tipus `Ethernet switch`.

Penseu que aquí podem substituir aixó per un node amb un contenidor o VM que emuli un model concret i real de router o switch (Cisco, Mikrotik...)

### Afegint el node NAT

Afegim un node de tipus NAT que farem servir per donar sortida a internet als nostres equips `ubuntu-noble-1` i `ubuntu-noble-2`

### "Tirant cable"

Amb l'opció `Add a link` (normalment al costat de `+` per afegir nodes) podem "tirar cable" entre dispositius:

- Unirem `eth0` del node `ubuntu-noble-1` al `Ethernet1` del switch.
- Unirem `eth0` del node `ubuntu-noble-2` al `Ethernet2` del switch.
- Unirem `nat0` del node `NAT` al `Ethernet0` del switch.

Amb aixó estem simulant una petita LAN.

### Configuració de xarxa dels nodes `ubuntu-noble`

Abans d'arrencar els nodes `ubuntu-noble`, establirem la seva configuració de xarxa fent servir l'opció `Configure` que apareix al clicar amb el botó dret a sobre d´'un aquests nodes.

Dins de la pantalla de configuració cercarem l'opció `Edit newtwork configuration`, el que ens obrirà una pantalla amb una configuració comentada amb varies propostes.

```text
#
# This is a sample network config, please uncomment lines to configure the network
#

# Uncomment this line to load custom interface files
# source /etc/network/interfaces.d/*

# Static config for eth0
#auto eth0
#iface eth0 inet static
#	address 192.168.0.2
#	netmask 255.255.255.0
#	gateway 192.168.0.1
#	up echo nameserver 192.168.0.1 > /etc/resolv.conf

# DHCP config for eth0
#auto eth0
#iface eth0 inet dhcp
#	hostname ubuntu-noble-1
```

Com que el node NAT ja ens proporciona funcionalitat de DHCP, podem descomentar la part del DHCP si no volem tenir una configuració estàtica específica.

```ini
# DHCP config for eth0
auto eth0
iface eth0 inet dhcp
	hostname ubuntu-noble-1
```

Fem el mateix amb l'altre node

```ini
# DHCP config for eth0
auto eth0
iface eth0 inet dhcp
	hostname ubuntu-noble-2
```

### Arrencant i provant

Ara podem arrencar els nodes clicant amb el botó dret i sel.leccionat l'opció `Start`

Un cop arrencats podem, per exemple, accedir clicant amb el botó dret via `Web console`

Al terminal que s'ens obre, podem provar:

- fer una ullada a la IP que ens ha assignat el DHCP amb `ip addr show eth0 | grep "inet "`
- que tenim connectivitat amb l'altre node fent un ping a l'adreça que li hagi concedit el DHCP del node NAT.
- que tenim connectivitat amb, per exemple, `ping 1.1.1.1`
- que tenim connectivitat amb, per exemple, `ping google.com`
