# 2048 Game (Python Tkinter)

A GUI implementation of the popular 2048 game using Python's Tkinter library.

## Features
- Default 4x4 board.
- Score tracking.
- Keyboard controls: Arrow keys.
- Merge tiles with same value to reach 2048.
- Restart button.
- Game Over and Win detection.

## Requirements
1. Install Python 3.x: https://www.python.org/downloads/
2. No external libraries required (Tkinter is included with Python).

## Installation
1. Clone the Repository
   - https://github.com/chethankumar-1/2048-tkinter-game.git
2. Navigate into the Project Folder
   - cd 2048-tkinter-game
3. Run the Game
   - python 2048_tk.py

## Deployed Application
1. You can download and play the packaged desktop version of the game from the link below:
   - https://drive.google.com/file/d/1wNt9BetwHf8l5Yo1R7hfsQEdgr_ixHdd/view?usp=drive_link
     
## How to Run the Game on Windows
1. Download the .exe file from the above link.
2. Locate the downloaded file in your Downloads folder.
3. Right-click the .zip file and select Extract All...
4. Open the extracted folder — you’ll find the file named 2048_tk
5. Go to inside folder.
6. Double-click the .exe file to run the game.
7. If you see a Windows Protected Your PC warning:
    - Click More info
    - Then click Run anyway
8. This warning appears because the file isn’t digitally signed — it’s safe if you downloaded it from this official Google Drive or GitHub link.
9. The game window will open, and you can start playing instantly!

## Notes
  - Always download from the official Google Drive or GitHub repository link to ensure safety.
  - No installation is required — just extract and play!
  - If the game doesn’t open, right-click the .exe and choose Run as Administrator.

## Gameplay Instructions
1. Objective:
   - Combine tiles with the same number to reach the 2048 tile.
2. How to Play:
   - Use the Arrow Keys to slide all tiles in that direction.
   - Tiles with the same value merge into one tile with their sum.
   - A new tile (2 or 4) appears after each move.
   - The game ends when no moves are left.
3. Winning Condition:
   - Reach the 2048 tile to win!
   - You can continue playing for a higher score.
4. Controls:
   - Keyboard controls: Arrow keys.
   - Move Up
   - Move Down
   - Move Left
   - Move Right
5. Tips:
   - Keep your highest tile in one corner.
   - Avoid unnecessary moves that shuffle the board.
   - Plan merges strategically to prevent blocking yourself.
  
## Implementation Details
1. Language: Python
2. GUI Library: Tkinter
3. Core Features:
   - 4x4 grid dynamically updated after each move
   - Random tile (2 or 4) generation
   - Tile merging logic (sum when two equal tiles collide)
   - Game-over condition check (no possible moves left)
   - Score tracking (optional feature if implemented)
