# Heroes of Might and Magic 3 Skip Intro Patch

This script creates a patched copy of the HoMM3 executable that allows skipping the intro movie.

This patch has only been tested with the English version of Heroes of Might and Magic 3: Complete (GOG), version `4.0 (3.2) GOG 0.1`. Other releases and language versions may not work.

## Prerequisites
- Python 3 (tested with Python 3.14.7)

## Usage

1. Copy `homm3_skip_intro_patch.py` into the same folder as the game executable.
2. Run:
```
python homm3_skip_intro_patch.py -i Heroes3.exe -o Heroes3_skip_intro.exe
```
3. Launch `Heroes3_skip_intro.exe`.

The game executable was reverse engineered using [Ghidra](https://github.com/NationalSecurityAgency/ghidra).
