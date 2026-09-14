#!/usr/bin/env python3
"""Prüft ev_charge_planner/config.yaml gegen die Regeln, an denen der Supervisor das Speichern ablehnt.

Übernommen aus thermoctl-addon, wo beide Fehler im echten Betrieb auftraten: ein leerer
Vorgabewert für ein URL-/Port-Feld und eine verschachtelte Gruppe ("Missing option ... in
root"). Zusätzlich: ingress_port darf nicht 0 sein und muss zu einem freigegebenen Port passen.

Aufruf: python3 pruefe-konfiguration.py  -- Rückgabe 0, wenn nichts zu beanstanden ist.
"""

import sys
from pathlib import Path

import yaml

KONFIGURATION = Path(__file__).parent / "ev_charge_planner" / "config.yaml"
PFLICHTSCHLUESSEL = ("name", "version", "slug", "description", "arch", "image")


def pruefe_schema(schema: dict, optionen: dict) -> list[str]:
    probleme: list[str] = []
    for schluessel, typ in schema.items():
        if isinstance(typ, dict):
            probleme.append(f"'{schluessel}' ist eine verschachtelte Gruppe -- flach auflösen")
            continue
        if not str(typ).rstrip(")").endswith("?") and schluessel not in optionen:
            probleme.append(f"Pflichtfeld '{schluessel}' ({typ}) fehlt in den Vorgaben")
        if optionen.get(schluessel) == "" and str(typ).startswith(("url", "port", "int", "float")):
            probleme.append(f"'{schluessel}' hat den leeren Vorgabewert \"\", Typ {typ} lässt das nicht zu")
    for schluessel in optionen:
        if schluessel not in schema:
            probleme.append(f"Vorgabe '{schluessel}' hat keinen Eintrag im Schema")
    return probleme


def pruefe_ingress(geladen: dict) -> list[str]:
    if not geladen.get("ingress"):
        return []
    port = geladen.get("ingress_port")
    if port in (0, None):
        return ["ingress_port ist 0 oder fehlt -- Ingress zeigt dann ins Leere (gunicorn lauscht auf 5000)"]
    if f"{port}/tcp" not in (geladen.get("ports") or {}):
        return [f"ingress_port {port} ist nicht unter ports freigegeben -- Port und Ingress laufen auseinander"]
    return []


def main() -> int:
    geladen = yaml.safe_load(KONFIGURATION.read_text(encoding="utf-8"))
    probleme = [f"Pflichtschlüssel '{s}' fehlt" for s in PFLICHTSCHLUESSEL if s not in geladen]
    probleme += pruefe_schema(geladen["schema"], geladen["options"]) + pruefe_ingress(geladen)
    for zeile in probleme:
        print(zeile)
    if not probleme:
        print("Keine Verstöße gegen die Supervisor-Regeln gefunden.")
    return 1 if probleme else 0


if __name__ == "__main__":
    sys.exit(main())
