# Symbol und Logo

`icon.png` (128 × 128) und `logo.png` (250 × 100) werden im Anwendungsprojekt aus dessen
freigegebenem Logo-System (`assets/logos/`) erzeugt:

    python tools/build_addon_images.py <Pfad zu diesem Ordner>

Quelle sind `assets/logos/logo-app.svg` und `assets/logos/logo-horizontal-dark.svg` dort.
Nicht von Hand bearbeiten.

- **`icon.png`** ist die vollflächige blaue Kachel mit verkleinertem Motiv: Home Assistant
  schneidet das Symbol in der Seitenleiste kreisförmig zu, das Motiv bleibt dabei vollständig.
- **`logo.png`** bringt seine eigene dunkle Fläche mit: Im Add-on-Store erscheint es auf hellem
  wie dunklem Hintergrund.
