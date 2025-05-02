# Papa's + Jacksmith Save Editor Toolkit

This is a desktop save file editor for **Flipline Studios** games such as:
- Papa's Pizzeria DX
- Papa's Freezeria DX
- Jacksmith (coming soon — PC/Steam version support)

It allows editing of key game data such as:
- Money
- Season
- Tickets
- Stars
- Stickers
- Unlocking all minigames
- Unlocking all ingredients

## 🎮 How to Use

1. Run the script:
```bash
python papas_jacksmith_editor_github.py
```

2. Select your game from the dropdown.
3. Choose the input `.sol` file from your local system.
4. Set output location, modify your save, and click "Apply Changes".
5. A backup of your original file is automatically created.

> NOTE: Jacksmith editing will activate once the Steam version's save format is confirmed after release (May 13, 2025).

## 🧰 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

## 📁 File Compatibility

- `.sol` files from Adobe Flash Local Shared Objects or remastered DX versions.
- Ensure you have a backup of your saves!

## 🔒 Disclaimer

This tool is intended for personal use and education. Do not use to cheat in multiplayer environments or commercial versions without permission.

## 🖥️ OS Support

This tool works on:
- 🐧 Linux (including Steam Deck & SteamOS)
- 🍎 macOS
- 🪟 Windows

### Requirements
- Python 3.8+
- Tkinter (usually preinstalled)
- pyamf

### Run it on Linux/macOS:
```bash
pip install -r requirements.txt
python papas_jacksmith_editor_github.py
```

### Notes for Linux / Steam Deck
If you’re on Steam Deck or any Linux distro:
```bash
sudo apt install python3 python3-tk
pip install pyamf
```

### Notes for macOS Users
If `tkinter` is not working, install with:
```bash
brew install python-tk
```

Make sure Gatekeeper allows running unsigned Python scripts (System Preferences > Security).

## 🔒 Trust & Safety

This project is 100% open-source and transparent.

- 🔍 No malware, spyware, or hidden scripts
- 🛠️ Built using Python and open libraries only
- 📂 All code is available in this repository for review

If you’re downloading a precompiled `.exe`, you can:
- Verify it matches the source code here
- Scan it with [VirusTotal](https://www.virustotal.com/)
- Or build your own using `pyinstaller`:

```bash
pip install pyinstaller
pyinstaller --onefile papas_jacksmith_editor_github.py
```

We respect your trust. This is for fans, by fans 💙
