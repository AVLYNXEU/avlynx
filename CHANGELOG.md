# Changelog

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
