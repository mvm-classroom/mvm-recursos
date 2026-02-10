# Monitoratge de servidors i serveis

## Descripció
- Objectiu: Posar en pràctica els mecanismes de control i supervisió de màquines remotes que actuen com a servidors de diferents tipus de serveis
- Desenvolupament: Grupal
- Lliurament: Repositori en markdown que contingui tota la documentació i una presentació

## Preparació
- Màquina client: Es recomana `Ubuntu Desktop` per accedir a l'eina de monitorització `nagios`
- Màquina servidora: Pot ser una `Ubuntu Server` amb `PostgreSQL` `17` o `18` instal.lat.

## Instal.lació de `nagios`

- Investigueu i documenteu-vos sobre l'eina [`nagios`](https://www.nagios.org/projects/nagios-core/) i procediu a la seva instalació

- Documenteu el procés d'instal.lació

- Mostreu i expliqueu captures del llistat de serveis monitorats per defecte


## Configuració i proves amb `check_pgsql`

- Investigueu i documenteu-vos sobre el plug-in `check_pgsql`
  Us pot ser d'utilitat [aquest](https://assets.nagios.com/downloads/nagioscore/docs/nagioscore/4/en/freshness.html?_ga=2.48630502.1182335243.1552209727-1735064696.1552209727) i [aquest](https://support.nagios.com/forum/viewtopic.php?f=7&t=33955) link.

- Configureu-lo i demostreu com i perqué l'esteu fent servir

## Configuració i proves amb `check_postgres`

- Investigueu i documenteu-vos sobre el conjunt de plug-ins `check_postgres` 
  Us pot ser d'utilitat [aquest](https://exchange.nagios.org/directory/plugins/databases/postgresql/check_postgres/details/) i [aquest](https://github.com/bucardo/check_postgres) link.

- Expliqueu en que es diferencia de l'anterior

- Instal.leu el conjunt de plug-ins i escolliu un dels que porta, justificant l'elecció

- Configureu-lo i feu una demostració del seu funcionament

