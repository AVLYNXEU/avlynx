# Company builds and add-ons

AVLYNX stays one generic editor. A company can build its own edition from the same source, and an add-on can extend it, without changing the editor itself. This page describes both. It applies from version 1.2.

## Build switches

`src/avlynx-source.html` contains placeholders of the form `/*@NAME@*/`. A company build script replaces them before running `build/build.py`. Without a build script, every switch keeps its default.

| Placeholder | Default | Purpose |
| --- | --- | --- |
| `EDITION` | `''` | Text shown next to the version, for example "Example Ltd edition" |
| `COMPANY` | `''` | Company name pre-filled in new projects and used for file names |
| `BAKED_LIBRARY` | `null` | A device library built into the file: `{stamp, groups, retired}` |
| `FEATURES` | `{}` | Turn parts off: `{libraryManager: false, example: false, customDevice: false}` |
| `ACCENT` | `'#0e6e7a'` | Accent colour for new projects, the legend and the PDF |

A switched-off part is hidden in the interface. Hidden is not protected: anything that must stay private (prices, keys, an official library) belongs on a server, not in the file.

## Extension interface

The editor publishes `window.AVLYNX`, a frozen object. Add-on scripts are placed after the editor's own script. All data is returned as a copy; changing it does not change the drawing.

| Member | Description |
| --- | --- |
| `version` | Editor version, for example `'1.2'` |
| `on('change', fn)` | Called after every saved change |
| `doc()` | Project data: name, customer, number, revision, page and so on |
| `rooms()` | Rooms on all sheets: `{id, sheet, name, qty}` |
| `setRoomQty(id, qty)` | Sets a room's quantity (1 to 999) |
| `equipment()` | Every device: `{sheet, room, roomId, roomQty, name, mfr, model, byOthers}` |
| `cables()` | Every cable: `{sheet, type, signal, cable, len, room, roomQty}` |
| `library()` | The device library (groups, categories, devices) |
| `insertRoom(template)` | Draws a ready-made room, see below. Returns `{devices, links, missing}` |
| `setExample(template)` | Uses a template as the example drawing |
| `getExt(key)`, `setExt(key, value)` | Add-on data stored inside the project, so it is saved, exported and undone with it. Use one key per add-on |
| `newProject()` | Starts an empty project |
| `setCableCheck(fn)` | Judges cables, see below |
| `cableIssues()` | All flagged cables: `{sheet, id, level, note, a, b}` |
| `addButton(label, fn, {id, title, primary})` | Adds a button to the header |
| `toast(text)` | Shows a short message |

Changes to this interface are listed in the changelog. Members are only removed in a new major version.

### Room templates

```js
AVLYNX.insertRoom({
  name: 'Huddle room', qty: 1,
  devices: [ // a device by library model, or a generic device by its library name
    { key: 'pc',  lib: 'Laptop', col: 0, row: 0 },
    { key: 'bar', model: 'EXAMPLE-BAR-1', col: 1, row: 0, label: 'Video bar', byOthers: false }
  ],
  links: [ ['pc', 'HDMI', 'bar', 'HDMI In'] ] // [device, port name, device, port name]
});
```

Devices are laid out in columns and rows; the room frame is drawn around them. A link is skipped if the ports do not exist or the signal types do not match.

### Cable check

```js
AVLYNX.setCableCheck(c => {
  // c = {type, a: {model, name, mfr, port, dir}, b: {...}}
  if (c.type === 'dante' && c.a.mfr !== c.b.mfr) return { level: 'warn', note: 'Check the Dante versions.' };
  return null; // no remark
});
```

`level` is `'warn'` (yellow) or `'bad'` (red). Flagged cables get a coloured marker, a "!" badge and the note as a tooltip. The editor itself contains no rules; it never blocks a connection because of this check.
