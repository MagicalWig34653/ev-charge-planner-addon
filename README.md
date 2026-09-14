# EV Charge Planner — Home-Assistant-Add-on

Dieses Repository ist ein **Add-on-Repository für Home Assistant**. Es enthält keinen
Anwendungscode; das Add-on nutzt das Abbild `ghcr.io/magicalwig34653/ev-charge-planner`.

## Installieren

1. In Home Assistant: **Einstellungen → Add-ons → Add-on-Store**
2. Oben rechts **⋮ → Repositories**
3. Diese Adresse eintragen:
   ```
   https://github.com/MagicalWig34653/ev-charge-planner-addon
   ```
4. Nach dem Neuladen erscheint **EV Charge Planner** im Store.

Was das Add-on tut und was vor dem Start zu beachten ist, steht in
[`ev_charge_planner/DOCS.md`](ev_charge_planner/DOCS.md).

## Prüfen vor einem Commit

    python3 pruefe-konfiguration.py

## Voraussetzung

Home Assistant **OS** oder **Supervised**.
