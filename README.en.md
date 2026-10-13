[中文](README.md) · **English**

# Z.A.T.O. // I Love the World and Everything in It — Localization Patch
An unofficial Simplified Chinese localization patch for **Z.A.T.O. // I Love the World and Everything in It**.

Original by Ferry (Nopanamaman), 2025 · Engine: Ren'Py 8.0.3

- **Steam store page**: <https://store.steampowered.com/app/4122860/ZATO__I_Love_the_World_and_Everything_In_It/> (App ID `4122860`, free game)
- **itch.io page**: <https://nopanamaman.itch.io/z-a-t-o-i-love-the-world-and-everything-in-it>

## Game and compatibility information
| Item | Info |
| --- | --- |
| Game title | Z.A.T.O. // I Love the World and Everything in It |
| Developer / Publisher | Ferry // Nopanamaman |
| Supported game version | **v1.0** (current Steam version, `config.version = "1.0"`) |
| Engine | Ren'Py **8.0.3** (script version `(8, 0, 3)`) |
| Supported platforms | Windows (Steam release; Mac / Linux should in principle work, untested) |
| Localization basis | Full text of the Steam version's `scripts.rpa` (16 script files) |
| Patch version | v1.0 |

> [!NOTE]
> The patch injects text into `game/tl/chinese/` and does not modify any original game file or archive. If a game update leaves the script text unchanged, the patch can usually continue to be used as-is; if a future official version ships an official Chinese translation, prefer the official one.

## Features
- **Complete localization**: Covers the prologue, all seven days of Chapters 1 and 2, and the finale (roughly 12,300 lines of dialogue and interface text), including chapter navigation, the gallery, settings, controls help, credits, and all other UI.
- **Bilingual**: Body text uses a "Chinese primary, English original appended in small grey text" bilingual layout, so you can read alongside the source text; the style stays close to the original.
- **Chinese on boot**: Forces the Chinese language pack to load via `config.language`, with no configuration required.
- **Full UI adaptation**: Replaces the original Courier font with [Source Han Sans](https://github.com/adobe-fonts/source-han-sans) (SIL OFL open-source license, redistributed with the patch) and adjusts font sizes; Cyrillic automatically falls back to the bundled DejaVu Sans, so the Russian text in the ending credits displays correctly.
- **Preserves the original feel**: Text effects (`{w}`, `{cps}`, `{size}`, `{i}` italics, etc.), typewriter pacing, NVL paragraphs, and easter-egg text are all preserved unchanged.

## Installation
1. Locate the game directory (Steam default):
   ```
   C:\Program Files (x86)\Steam\steamapps\common\Z.A.T.O.  I Love the World and Everything In It\
   ```
   (You can also reach it from your Steam library by right-clicking the game → Manage → Browse local files.)
2. **Copy the patch's entire `game/` folder** into the game directory and choose "Replace the files in the destination". When done, the game directory should contain:
   ```
   Z.A.T.O. ...\
   ├─ game\
   │  ├─ 00zh_override.rpy          ← new
   │  └─ tl\
   │     └─ chinese\                ← new (includes fonts)
   └─ ...
   ```
3. Launch the game. Saves are fully compatible with the original.

### Uninstall
Delete the two items `game/00zh_override.rpy` and `game/tl/` to restore the original.

## Font notes
The patch uses **SourceHanSansLite.ttf**, a slimmed-down build of Source Han Sans from the official Ren'Py SDK, distributed under the [SIL Open Font License](https://openfontlicense.org/) and freely redistributable. The original Courier font contains no Chinese glyphs, so the Chinese interface requires replacing the font.

## Known issues
- A small amount of English baked into the original artwork (such as the logo on the title screen) is not text and cannot be localized.
- Russian personal names in the credits — such as the voice credit "Воробушек" — are proper nouns and are kept in the original.

## License
- The patch's translated text is for learning and exchange only and may not be used commercially; all rights to the game belong to its original author, Ferry (Nopanamaman).
- `fonts/SourceHanSansLite.ttf` is distributed under SIL OFL 1.1, copyright © Adobe.
- The game itself is **free** on both Steam and itch.io — please visit the official pages to support the author.
