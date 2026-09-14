# Änderungen (Add-on)

Änderungen an der Add-on-Verpackung selbst. Für die Anwendung siehe das Anwendungsprojekt.

## 0.2.1

- Abbild `ev-charge-planner:0.2.1`.
- Neues Symbol und Logo (finale Bildmarke: neues Blau und Grün, überarbeitete Balken und Blitz).
- Seitenleiste: Symbol `mdi:ev-plug-type2`, Titel „Ladeplanung“, `panel_admin: false`.

## 0.2.0

- Zugriff auf den Ordner `ssl` (nur lesend) für MQTT-Zertifikate.
- Erste Fassung des Add-ons: Abbild `ev-charge-planner:0.2.0`, Architekturen
  `amd64`/`aarch64`, Ingress über die Seitenleiste, zusätzlicher Port 5000 ohne Anmeldung.
- Optionen für Trockenlauf, Datenbank (SQLite unter `/data` oder MariaDB), MQTT inklusive
  TLS und Discovery-Präfix sowie das Auffangfeld `env`.
- Neues Logo.
