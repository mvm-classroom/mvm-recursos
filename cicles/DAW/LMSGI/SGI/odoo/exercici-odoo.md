# Exercici pràctic: Gestió del manteniment del parc informàtic del centre amb Odoo 18

## 1. Context de l'Escenari
Sou els responsables del departament d'IT d'un centre educatiu. El centre disposa de 3 aules tècniques (DAW, SMX i ASIX), cadascuna amb 20 equips. La vostra missió és configurar Odoo per gestionar les incidències de maquinari (hardware) i programari (software), portar el control d'estoc de les peces de repost i generar informes d'activitat.

---

## 2. Configuració Inicial del Sistema

Un cop accediu a la vostra instància d'Odoo, heu de realitzar els següents ajustos corporatius:

### A. Informació de l'Empresa
* **Nom:** Institut MVM - elvostrenom (per exemple: `Institut MVM - JVazquez`)
* **Configuració:** Pugeu un logotip corporatiu (podeu fer servir el del centre o un altre), configureu la moneda en EUR i les dades de l'empresa com adreça, tlf, correu electrònic... (podeu consultar les del centre)

### B. Configuració d'Usuaris i Accessos
A Odoo 18, els permisos de reparacions estan integrats en la gestió d'Inventari. Creeu els següents perfils:
1.  **Tècnic:**
    * Permís: **Inventory / Administrator**.
    * Responsabilitat: Validar peces, confirmar reparacions i tancar tiquets.
2.  **Usuari:**
    * Permís: **Inventory / User**.
    * Responsabilitat: Reportar incidències i consultar l'estat dels seus equips.

### C. Impostos i Comptabilitat
* Assegureu-vos que l'**IVA (VAT) del 21%** estigui configurat per defecte per a la venda de serveis i components.

---

## 3. Preparació de l'Inventari (Actius del Centre)

Per poder reparar un equip, aquest ha d'estar identificat de forma única al sistema.

1.  **Creació del Producte Mestre:**
    * Nom: `PC d'Aula`.
    * Tipus: **Goods** (Producte Emmagatzemable).
    * Traçabilitat (Pestanya Inventory): **By Unique Serial Number**.
2.  **Càrrega dels 60 Equips:**
    * Elaboreu i carregueu un fitxer amb els 60 números de sèrie (`DAW-01` a `DAW-20`, `SMX-01` a `SMX-20` i `ASIX-01` a `ASIX-20`). Aixó ho podeu fer creant un únic producte i exportant-lo a fitxer. Editar el fitxer afegint elements i tornant-lo a importar.
3.  **Estoc de Recanvis:**
    * Doneu d'alta 5 unitats dels següents productes (Tipus Goods): `Memòria RAM 8GB`, `Disc SSD 500GB`, `Teclat USB`, `Font d'Alimentació 500W`.

---

## 4. Gestió del Negoci: El Flux de Reparacions

Heu de registrar i resoldre les següents incidències simulades:

### Cas 1: Avaria de Maquinari (Aula SMX)
* **Equip:** `SMX-05`.
* **Problema:** La font d'alimentació s'ha cremat.
* **Procediment:**
    1.  Crear una **Repair Order** (Ordre de Reparació).
    2.  Assignar l'etiqueta `AULA-SMX`.
    3.  A la pestanya **Parts**, afegir una "Font d'Alimentació 500W".
    4.  Confirmar la reparació i marcar com a finalitzada perquè l'estoc es desconte automàticament.

### Cas 2: Incidència de Programari (Aula DAW)
* **Equip:** `DAW-12`.
* **Problema:** Error crític en l'entorn Docker després d'una actualització.
* **Procediment:**
    1.  Crear una **Repair Order**.
    2.  Assignar l'etiqueta `AULA-DAW`.
    3.  Com que és programari, no hi ha peces. Documenteu la solució (reinstal·lació d'imatge) a la pestanya de **Notes**.

---

## 5. Facturació i Reporting

Encara que és un centre educatiu, simularem el cobrament de serveis externs per aprendre el flux administratiu.

1.  **Generació de Factura:**
    * Des de la reparació de l'`SMX-05`, genereu la factura corresponent a la peça utilitzada i 1 hora de mà d'obra (creeu el producte "Mà d'obra" si és necessari).
2.  **Reporting d'Inventari:**
    * Accediu a **Inventory > Reporting > Stock**.
    * Verifiqueu que l'estoc de "Fonts d'Alimentació" ha disminuït correctament.
3.  **Anàlisi de Reparacions:**
    * Aneu al mòdul **Repairs** i activeu la **Vista Pivot** o **Vista Gràfica**.
    * Agrupeu per "Etiqueta" (Tag) per identificar quina aula està generant més incidències aquest mes.

---

## 6. Lliurament
S'haurà d'exportar en PDF la **Llista de Reparacions** del mes, on es vegi clarament l'estat de cada equip, l'aula a la qual pertany (via Etiquetes) i si ha requerit peces de recanvi.

Heu de deixar al repositori habilitat, el següent:
- Llista de reparacions
- Exemple de factura
- Informe d'inventari
- Captures de les diferents vistes (pivot, gràfica) de les reparacions
- Document de tot el procés d'instalació, configuració i proves en .md
- Video explicatiu (4-6 minuts) on defenseu tota la pràctica (podeu fer servir qualsevol eïna de captura com `OBS`). Al video s'ha de mostrar una presentació amb el més important de tota la feina que heu fet. No cal que surtiu vosaltre, però heu de fer servir la vostra veu.
