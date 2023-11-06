# pyroguelike
A playground-in-development to test game ideas, skills, mechanics and so on easily and quickly.

While it's bare-bones at the moment, the skeleton is slowly being built. Expect daily updates.

## Installation
1. Most IDE's will do this automatically, but make certain you have the packages listed in requirements.txt installed. This can be done by running `pip install -r requirements.txt`.
2. Run main.py to execute the game.


## Configuring
Inside config.py, you will see numerous properties to change the game:
### Debug and Time Display
- **DEBUG = True** - False disables debug messages.
- **SHOW_TIME = True** - Displays time in window. Disable with False.
### Window Properties
- **WIDTH = 80** - The amount of tiles to use on the x-axis.
- **HEIGHT = 50** - The amount of tiles to use on the y-axis.
### Map Properties
- **MAP_BUFFER_X = 0** - Number of tiles before drawing map on the x-axis.
- **MAP_BUFFER_Y = 3** - Number of tiles before drawing map on the y-axis.
- **MAP_WIDTH = 75** - Tile number to stop drawing on the x-axis.
- **MAP_HEIGHT = 75** - Tile number to stop drawing on the y-axis.
### Movement
- **EIGHT_WAY_MOVEMENT = False** - Defaults to 4-way movement.


## Current Features
- 4-Way player controls (WASD, keypad, arrow keys).
- 8-Way player controls (keypad-only).
- Quit with 'q' or ESC.
- Can spawn in multiple entities, see main.py.
- Massive color list to draw from. See process/color.py for the full list that can be used.
- RGBA tile support.