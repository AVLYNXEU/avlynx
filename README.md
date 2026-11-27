# AVLYNX

AVLYNX is a browser-based editor for AV system diagrams. Devices are placed from a library and connected by signal type; the drawing, the equipment list and the cable list are exported from the same data and always match.

![AVLYNX with an example drawing](docs/screenshot.png)

## Getting started

- **Online:** https://avlynxeu.github.io/avlynx/
- **Offline:** download `avlynx.html` from the [latest release](https://github.com/avlynxeu/avlynx/releases/latest) and open it in a browser.
- **News:** follow [AVLYNX on LinkedIn](https://www.linkedin.com/company/145449744/)

AVLYNX is a single HTML file. It requires no installation, no server and no account, and it does not transmit drawings. Projects and the device library are stored in the browser.

## Features

**Drawing**
- Device blocks with any number of inputs and outputs
- 19 signal types with their own colours, including HDMI, DisplayPort, USB-C, SDI, HDBaseT, analog audio, Dante, NDI, USB, network, fiber (SFP), power, RS-232 and IR
- Connection check: only matching signal types connect, outputs to inputs. Different video connectors require an adapter device
- Up to two cables per analog audio connector; any number per speaker connector, with loudspeaker-to-loudspeaker chains for 70/100 V systems
- Right-angled or curved lines; every part of a right-angled line can be moved, and corners can be added
- Automatic cable IDs per signal type, for example H001 and A001
- Rooms as labelled frames; the room becomes the location of the devices inside it
- Room quantity for identical rooms ("× 6"), counted in all lists
- Devices marked "supplied by others"
- Custom devices for a single drawing, without changing the library
- Text boxes in three highly legible fonts, alignment guides, align and distribute
- Several sheets per project, with cables that continue from one sheet to another; sheets can be duplicated
- Select an area with Shift and drag; copy, cut and paste several devices, rooms and cables, also into another sheet or project
- Cable bundles: many cables of one signal type share one run and split again just before the devices
- Edit several lines or devices at once: shape, corners and arrows for all selected lines, location and notes for all selected devices
- Edit menu on right-click or long press, with the actions for the object or the empty place
- Replace a device while its cables stay connected
- Details panel with the attributes of the selected device, cable or room
- Find devices, cable IDs, rooms and texts on all sheets (Ctrl+F)
- Check drawing: lists unconnected devices, devices without connectors and duplicate cable IDs, also before a PDF export

**Documents**
- PDF drawing with title block and legend in A1 to A4, Tabloid or Letter, landscape or portrait (also per sheet)
- Spreadsheet (.xlsx) and CSV lists: equipment, cables and cable summary for ordering, and cable labels for label printers
- Images (PNG, SVG) of a sheet or of the selection, and a diagram file for draw.io
- Cable type, length and notes for many cables in one step
- File names generated from project name, drawing number, revision and date

**Device library**
- About 130 generic devices, including adapters and fiber extenders
- Own groups, categories and devices; import and export as JSON, spreadsheet (.xlsx) or CSV
- Device editor with inputs and outputs side by side, sorted by drag and drop; connectors can be duplicated, copied and pasted into other devices
- Favourites as references to library devices
- Jump from a device on the drawing straight to its library entry and update it
- Optional shared library on a web server, with a backup before every update and a warning before changed devices are replaced

## Documentation

- The [user guide](docs/AVLYNX-User-Guide.pdf) describes every function and the import format for device lists.
- The [administrator guide](docs/ADMIN-GUIDE.md) ([PDF](docs/AVLYNX-Administrator-Guide.pdf)) explains how to host AVLYNX on your own server, maintain a company device library and build a company edition.
- Company builds and add-ons (build switches, the `window.AVLYNX` interface, the cable check hook) are described in [docs/EXTENSIONS.md](docs/EXTENSIONS.md).

## Hosting AVLYNX in your organisation

AVLYNX runs from any static web server: copy `avlynx.html` from a release to a folder as `index.html`. To give the whole team the same device library, export it under **Manage library**, rename the file to `avlynx-library.json` and place it next to `index.html`. New users receive it immediately; all other users are offered an update when the file changes. Their own devices are kept. [`docs/example-library.json`](docs/example-library.json) is a small library to start from.

For a company edition with your name, accent colour and library built in, run:

```
python3 build/company-build.py --edition "Example Ltd edition" --company "Example Ltd" --library avlynx-library.json --accent "#2b4c9a"
```

Server examples (nginx, Apache, IIS, Docker), access control, updates and a roll-out checklist are in the [administrator guide](docs/ADMIN-GUIDE.md).

## Browser support

Current versions of Chrome, Edge, Safari and Firefox on desktop computers, tablets and phones. Safari requires version 15.4 or later.

## Security

- AVLYNX runs entirely in the browser. It has no server component, no account and no telemetry.
- A content security policy in the file permits connections only to the server the file was loaded from.
- Project and library files are validated when they are opened.
- The only third-party code is jsPDF 4.2.1 for the PDF export. Spreadsheet (.xlsx) and CSV files are written and read by AVLYNX itself.
- Data in the browser is not encrypted. On shared computers, use separate browser profiles.

Please report security issues as a private security advisory on GitHub, not as a public issue.

## Build from source

The editor is developed in `src/avlynx-source.html`. To build the release file `index.html`, run:

```
python3 build/build.py
```

The build adds the content security policy and embeds jsPDF, so that the finished file works offline.

## Contributing

Suggestions and bug reports are welcome as issues. Changes to the official version are reviewed before they are merged.

## Licence

AVLYNX is released under the [MIT License](LICENSE).
Copyright (c) 2026 Timo Schönmeier.

The bundled library jsPDF and the fonts have their own licences; see [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md).

## Trademarks

draw.io is a trademark of draw.io Ltd. Microsoft and Excel are trademarks of the Microsoft group of companies. HDMI, HDBaseT, Dante, DisplayPort, NDI, USB-C and other names of products, interfaces and file formats are trademarks of their owners. They are used only to describe compatibility; AVLYNX is not affiliated with or endorsed by these companies.
