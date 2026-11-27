# Changelog

## 1.4.0 – 27 November 2026

**Find, check and new exports**
- Find (button in the toolbar, or Ctrl+F): devices, models, cable IDs, cable types, rooms, texts and connector names on all sheets. AVLYNX switches to the sheet, centres the match and selects it; Enter and Shift+Enter step through the matches.
- Check drawing (More ▾): lists devices that are not connected, devices without connectors, cable IDs used more than once and a missing project name; click an entry to show it. The check also opens before a PDF export when it finds something, and can be switched off there.
- Export ▾ → Image (PNG) and Image (SVG): the current sheet, or only the area around the selection, always in light colours.
- Export ▾ → Cable labels as CSV: one row per cable end with "To:" and "From:" texts, for label printer software.
- Export ▾ → Diagram for draw.io (.drawio): one page per sheet with devices, connectors, cables on their routes, cable IDs, rooms and texts; cables stay attached to their connectors when devices are moved in draw.io.
- The PDF writes Central and Eastern European letters (for example ł, č, ő, ș) with the embedded Atkinson Hyperlegible font when a project contains them.

**Simpler to use**
- The right-click menu of several selected objects offers Align left, Align top, Distribute evenly and More alignment….
- Projects: the dialog shows the name of the current project, which can be changed there, and whether it has unsaved changes. Opening or starting a project asks only when there are unsaved changes. New project keeps the company details, logo, Drawn by, page and legend settings, from the welcome message and from the Projects dialog alike.
- More ▾ → Open the example project opens the example as its own project instead of placing it on the current sheet.
- The switch "Curved lines" for all lines was removed. Single lines can still be curved with Line ▾; curved lines in older projects stay curved.
- The device list and the library manager open with all groups closed, and windows open again at the top with folded sections closed.
- Menus name file types instead of other companies' programs ("spreadsheet (.xlsx)"); About AVLYNX and the guides contain a trademark notice.

**Documentation and tools** (published earlier)

- Administrator guide for hosting AVLYNX in an organisation: server examples for nginx, Apache, IIS and Docker, access control, the company device library, updates and a roll-out checklist (`docs/ADMIN-GUIDE.md`, also as PDF).
- `build/company-build.py` builds a company edition from a release file: edition name, company name, built-in library, accent colour and hidden parts.
- `docs/example-library.json`: a small example library to start a company library from.

## 1.3.1 – 24 November 2026

**Cable bundles**
- Many cables of one signal type between the same devices can now run as a bundle: each cable leaves its device on a short branch, all of them share one run, and they split again just before the far device. A tag on the shared run shows the number of cables.
- Right-click a device, then Bundle its cables: one bundle for each signal type on each side of the device. Or select several lines and choose Line ▾, then Bundle N lines (one bundle per signal type).
- Drag the round handle of a bundle to move its shared run; Reset bundle route puts it back. Right-click a bundled line for Select whole bundle and Remove from bundle; Unbundle turns the lines back into single lines.
- Bundles follow when devices move and lead between device blocks. Lines in one bundle do not jump over each other, and cable IDs stay on the branches. The PDF export shows bundles as on the screen.
- Copied and duplicated devices get their own bundle. Bundle data in opened files is checked like all other values.

**Page orientation**
- Project details offer Orientation next to the PDF page size: Landscape or Portrait.
- Each sheet can have its own orientation (⋯ next to the sheet name, then Landscape page or Portrait page), so one PDF can mix landscape and portrait pages.
- The Export menu names the page size and orientation. On narrow pages the legend continues on a second line, and the company name in the title block gets smaller type instead of being cut.

**Fixes**
- Dragging near the edge of the drawing scrolls only towards the edge the pointer moved to, so a selection frame started close to an edge no longer moves the view.

## 1.3.0 – 24 November 2026

**Working with several objects**
- Select an area: hold Shift and drag a frame. Everything completely inside is selected, including the cables between the selected devices. With Ctrl (Cmd on a Mac) as well, the framed objects are added to the selection.
- Copy, cut and paste with Ctrl+C, Ctrl+X and Ctrl+V (Cmd on a Mac). Cables come along when both of their devices are copied, and a room brings its devices and texts. Pasting puts the objects at the mouse pointer and keeps them selected, also in another sheet or project. Custom cable IDs are not copied, so every ID stays unique.
- Duplicate (Ctrl+D) works for several objects and for rooms.
- Duplicate sheet.
- Several lines at once: a Shift-frame drawn only across lines selects those lines. Line ▾ then changes all of them (Curved, Add corner, Reset, Show as arrows), and dragging one round handle moves the same part of every selected line.
- Edit devices: manufacturer, location detail, notes and "supplied by others" for several devices at once.
- Rooms behave like the other objects: copy, cut, paste and duplicate take the devices and texts inside along. Delete removes only the frame, as before; right-click offers Delete room with its contents.

**Navigation and editing**
- Move the view with the middle mouse button: press the wheel and drag, anywhere on the drawing.
- While a device, room, text, line or selection frame is dragged to the edge of the drawing area, the view moves along, so objects can be put down in a part that was not visible.
- Speaker connectors take any number of cables (70 V and 100 V systems), and a loudspeaker can be connected on to the next one (input to input). Analog audio connectors keep the limit of two.
- Connections between two connectors on the same side of neighbouring devices run around below the blocks instead of behind them.
- Lines lead around device blocks that stand in the way, through a free gap or channel.
- Cable IDs of lines that share their first part (several loudspeakers on one output) are placed along each line, so they no longer sit on top of each other.
- Edit in the device library: from a device on the drawing straight to its library entry, unlocked for this change. After saving, the device on the drawing takes over the change and keeps its cables wherever a matching connector exists.
- Device editor: duplicate a connector with ⧉ or Ctrl+D (the number in the name counts up); copy all inputs or outputs and paste them into another device.

**Menus and buttons**
- One menu style for right-click, line, sheet, library and connector actions, with shortcuts, check marks and keyboard control (arrow keys, Enter, Esc). On touch screens, press and hold for the right-click menu.
- Right-click on an empty place: Paste, Select all, Add room here, Add text here, Show the whole drawing. Right-click on an object: the actions for that object only.
- Signal type bar ("Highlight") shows only the signal types on the open sheet, so it always fits.
- Cables: the selection bar shows Edit, Line ▾ and Delete. Line ▾ holds Curved, Add corner, Reset line, Show as arrows and Select all cables of the same type.
- Sheets: double-click the open sheet to rename it; ⋯ next to it offers Rename, Duplicate and Delete sheet.
- Library manager: + Group, Import, Export ▾ and ⋯ (collapse or expand all, undo library update, reset to defaults). Manage library is a small button next to the Devices heading.
- The top bar button is called Projects. The More menu is grouped, with check marks for Curved lines and Details panel.
- Dialog footers stay visible on small screens. Consistent wording: Edit cable, Title block and legend, New project, Open project. Hints say Click with a mouse and Tap on touch screens. Tooltips with shortcuts on the selection bar buttons.

**Security**
- Pasted objects are checked like a project file; pasted connectors keep only known signal types.
- Limits against oversized or manipulated files: up to 5000 devices and 20000 cables per sheet, 256 connectors per device, coordinates within ±1,000,000 and length limits for all texts; the same limits apply to library imports.

## 1.2.0 – 20 November 2026

- Rooms have a quantity, for example six identical huddle rooms drawn once. The room label shows "× 6", the location in the lists reads "Huddle room (× 6)", and the equipment summary and the cable summary count devices and cables with the quantity.
- Devices can be marked "supplied by others": dashed outline and a note on the drawing and in the PDF, and a "Supplied by" column in the equipment summary.
- New signal type Power, with cable IDs PW001 and so on: a power supply output feeds a device's power input. New generic devices: power supply with one or four outputs. The Excel and CSV import accept power, power supply, DC, Strom and Netzteil.
- Custom device: a device made for one drawing only. It is saved with the project and never changes the library.
- Cable IDs never sit on top of a device block; when the usual place is covered, the ID moves beside the cable.
- Device libraries keep alternative model numbers (aliases), for example old and new SKUs; the device search finds them.
- File names fall back to the company name when the project has no name.
- For company builds and add-ons (see docs/EXTENSIONS.md):
  - build switches to turn off the library manager, the example drawing or the custom device, and to set the accent colour;
  - an extension interface, window.AVLYNX, to read the drawing, insert ready-made rooms, add buttons and store add-on data in the project;
  - a cable check hook: an add-on can judge each cable, and flagged cables get a yellow or red marker, a "!" badge and a tooltip.

## 1.1.0 – 17 November 2026

- New signal type Fiber (SFP) with cable IDs F001, F002 and so on. Fiber connects only to fiber; multimode or single mode is recorded as the cable type, and the cable dialog suggests OM3, OM4 and OS2 patch cables.
- New generic devices: fiber extender (transmitter and receiver), network switch with SFP uplinks, media converter.
- Analog audio and speaker connectors take up to two cables, for example a stereo output feeding two loudspeakers.
- Device editor: inputs on the left, outputs on the right; connectors are sorted and moved between the sides by drag and drop or with the arrow keys.
- The signal highlight is cleared by a second click on the signal type or by any click elsewhere on the drawing; clicking a cable highlights its type.
- Cable IDs no longer overlap when two cables leave the same connector.
- Excel and CSV import accept SFP, SFP+, fibre, glasfaser and LWL as fiber.

## 1.0.0 – 16 November 2026

First public release.
