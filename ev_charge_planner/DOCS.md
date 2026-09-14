# EV Charge Planner

Plant das Laden eines Elektroautos anhand dynamischer Strompreise (Tibber), eigener
Verfügbarkeitsfenster und eines Ziel-Ladestands — und schaltet die Wallbox entsprechend
ein und aus. Status und Ladesitzung erscheinen per MQTT-Discovery als Entitäten in Home
Assistant.

## Wichtig, bevor Sie anfangen

**EV Charge Planner schaltet eine echte Wallbox.** Eine falsche Konfiguration kann dazu
führen, dass das Auto nicht oder zur falschen Zeit lädt.

**Keine eigene Anmeldung.** Über die Seitenleiste schützt Sie die Anmeldung von Home
Assistant. Der zusätzlich freigegebene **Port 5000 hat keinen Schutz**: Wer ihn im Netz
erreicht, kann alle Einstellungen ändern und die Wallbox schalten. Brauchen Sie ihn nicht,
leeren Sie ihn unter *Konfiguration → Netzwerk*.

## Installation

1. *Einstellungen → Add-ons → Add-on-Store → ⋮ → Repositories* und
   `https://github.com/MagicalWig34653/ev-charge-planner-addon` hinzufügen.
2. **EV Charge Planner** installieren.
3. Unter *Konfiguration* den MQTT-Broker eintragen (siehe unten).
4. Add-on starten und über die Seitenleiste („Laden“) öffnen.
5. In der Weboberfläche unter *Einstellungen* Tibber-Zugang, Wallbox und
   Ladestand-Quelle einrichten. Diese Werte liegen in der Datenbank des Add-ons, nicht in
   der Add-on-Konfiguration.

## Konfiguration

### Trockenlauf (`dry_run`)

Vorgabe: aus. Eingeschaltet schaltet das Add-on die Wallbox nicht, veröffentlicht nichts
per MQTT, verschickt keine Benachrichtigungen **und speichert nichts** — auch Änderungen in
der Weboberfläche werden verworfen. Gedacht für den Parallelbetrieb neben einer bereits
laufenden Instanz, nicht für die Ersteinrichtung.

### Datenbank

Vorgabe ist SQLite unter `/data/evcp.db` — dem Datenverzeichnis des Add-ons, das Updates
übersteht und im Home-Assistant-Backup enthalten ist.

Mit `database_type: mariadb` nutzt das Add-on stattdessen einen MariaDB-Server (z. B. das
MariaDB-Add-on, Host `core-mariadb`). Host, Port, Benutzer, Passwort und Datenbankname sind
dann Pflicht; die Datenbank muss vorher existieren. Fehlt ein Feld, startet das Add-on nicht
und nennt im Protokoll das fehlende Feld.

### MQTT

Tragen Sie Host, Port, Benutzer und Passwort Ihres Brokers selbst ein — auch wenn das
Mosquitto-Add-on läuft (Host dann `core-mosquitto`); die Zugangsdaten werden nicht
automatisch übernommen. `mqtt_base_topic` (Vorgabe `evplanner`) bestimmt die Topics
`<topic>/status` und `<topic>/cmd/#`; `ha_discovery_prefix` (Vorgabe `homeassistant`) muss
zur MQTT-Integration von Home Assistant passen. Für TLS `mqtt_tls` einschalten und bei einer
eigenen Zertifizierungsstelle `mqtt_ca_cert` auf eine Datei zeigen lassen, die im Container
erreichbar ist.

### Wenn ein Feld fehlt: `env`

Für alles ohne eigenes Feld nimmt `env` den Inhalt einer `.env` auf, eine Zuweisung je
Zeile; Zeilen mit `#` werden übersprungen:

```
MQTT_TLS_INSECURE=1
MQTT_TLS_CERT=/ssl/client.pem
```

Diese Zuweisungen gelten **nach** den Feldern oben und überschreiben sie. Die bekannten
Namen stehen in der `.env.example` des Anwendungsprojekts. Was hier steht, ist im Klartext
gespeichert — Passwörter gehören in die dafür vorgesehenen Felder.

## Home-Assistant-Widget

Die Seite `/ha/widget` lässt sich als Webseiten-Karte einbinden. Die Einstellungsseite der
Weboberfläche zeigt die passende Adresse zum Kopieren.

## Voraussetzung

Home Assistant **OS** oder **Supervised**.
