# pyroguelike
A playground-in-development to test game ideas, skills, mechanics and so on easily and quickly.

While it's bare-bones at the moment, the skeleton is slowly being built. Expect daily updates.

## Installation
1. Most IDE's will do this automatically, but make certain you have the packages listed in requirements.txt installed. This can be done by running `pip install -r requirements.txt`.
2. Run main.py to execute the game.


## Configuring
Inside config.py, you will see numerous properties to change the game:
- **DEBUG = True** - False disables debug messages.
- **SHOW_TIME = True** - Displays time in window. Disable with False.
- **WIDTH = 80** - The amount of tiles to use on the x-axis.
- **HEIGHT = 50** - The amount of tiles to use on the y-axis.
- **MAP_WIDTH = 75** - The amount of tiles to draw for the main map on the x-axis.
- **MAP_HEIGHT = 75** - The amount of tiles to draw for the main map on the y-axis.
- **EIGHT_WAY_MOVEMENT = False** - Defaults to 4-way movement.


## Current Features
- 4-Way player controls (WASD, keypad, arrow keys).
- 8-Way player controls (keypad-only).
- Quit with 'q' or ESC.
- Can spawn in multiple entities, see main.py.
- Massive color list to draw from. See process/color.py for the full list that can be used.