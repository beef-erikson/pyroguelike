# pyroguelike
A playground-in-development to test game ideas, skills, mechanics and so on easily and quickly.

While it's bare-bones at the moment, the skeleton is slowly being built. Expect daily updates.

### Installation
1. Most IDE's will do this automatically, but make certain you have the packages listed in requirements.txt installed.
2. Run main.py to execute the game.


### Configuring
Inside config.py, you will see numerous properties to change the game:
- **debug = True** - Change this to False to disable debug messages.
- **width = 80** - The amount of tiles to use on the x-axis.
- **height = 50** - The amount of tiles to use on the y-axis.
- **eight_way_movement = False** - Defaults to 4-way movement.

### Current Features
- 4-Way player controls (WASD, keypad, arrow keys).
- 8-Way player controls (keypad-only).
- Quit with 'q' or ESC.
- Can spawn in multiple entities with color, see main.py.