# jbua-scripts (Jackbox Games UA Scripts)

A collection of Python automation scripts used to facilitate the Ukrainian localization of Jackbox Party Pack games. 

These scripts process raw translation files (like tab-separated `.txt` dumps) and automatically generate the `.jet` (JSON) format files, folder structures, and subtitle text replacements required by the Jackbox game engines.

## 🎮 Supported Games
The repository includes dedicated scripts for specific mini-games across various Jackbox Party Packs, organized below in chronological order of their original release:

**The Jackbox Party Pack 3 (2016)**
* **Fakin' It** (`fakinit`)
* **Tee K.O.** (`teeko` / internally referenced as *AwShirt*)

**The Jackbox Party Pack 6 (2019)**
* **Dictionarium** (`ridictionary`)
* **Joke Boat** (`jokeboat`)
* **Push The Button** (`pushthebutton`)
* **Trivia Murder Party 2** (`triviadeath2`)

**The Jackbox Party Pack 7 (2020)**
* **Talking Points** (`talkingpoints`)

**The Jackbox Party Pack 8 (2021)**
* **Drawful Animate** (`animate`)
* **Job Job** (`jobjob`)
* **The Poll Mine** (`surveybomb`)
* **The Wheel of Enormous Proportions** (`thewheel`)
* **Weapons Drawn** (`weaponsdrawn`)

**The Jackbox Party Pack 9 (2022)**
* **Nonsensory** (`nonsensory`)
* **Quixort** (`quixort`)

**The Jackbox Party Pack 10 (2023)**
* **Timejinx** (`timetrivia`)
* **Hypnotorious** (`usthem`)

## 🛠️ Script Types & Functionality

While each game has its own unique data structure, the repository generally uses a standard set of script types within each game's folder:

* **`make.py` (Content Generators)**: Reads from a tab-separated text file (usually named `base.txt`) containing localized strings and outputs a main `[GameName].jet` and/or `[GameName]Tech.jet` file. This handles the primary JSON compilation.
* **`makedata.py` / `newmakedata.py` (Data Injectors)**: Iterates through generated prompt IDs, creates necessary subdirectories, and modifies or creates individual `data.jet` files. This is used to map specific localized strings and audio file references to the correct prompt IDs.
* **`parse.py` (Subtitle/Dubbing Parsers)**: Typically found in `dub/` or `озвучка/` directories. These scripts take a `start.txt` file containing the original English subtitle strings and use a `base.txt` dictionary to find and replace them with localized text, outputting a `fin.txt` file ready to be injected into the game's code.
* **`audiothrower.py` (Audio Organizers)**: Searches an `audio/` directory for localized `.ogg` voiceover files and automatically copies them into the correct game subdirectories based on their prompt IDs.
* **`wizard.py` (CLI Tools)**: Interactive command-line interfaces (like in `timetrivia`) to help users choose which categories and steps (make jets vs. make folders) to execute without manually running every script.

## 🚀 How to Use

### Prerequisites
* **Python 3.6+** is required. 
* No external dependencies are needed; the scripts rely entirely on Python's standard library (`json`, `os`, `shutil`, `copy`, `re`, `asyncio`).

### Standard Workflow
1. Place your translated tab-separated text file inside the target game's directory and name it `base.txt` (or as required by the specific script).
2. Open a terminal and navigate to the specific game's module.
3. Run the generator script:
   ```bash
   python make.py
