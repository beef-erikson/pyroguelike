import config
import player
from tcod.event import KeyDown, KeySym, Quit, wait
from tcod.console import Console
from tcod.context import Context


# Handles controls, quitting, etc.
def event_handling(player_object: player.Player) -> None:
    for event in wait():
        # Event tracking
        if config.debug:
            print(event)

        # Event handling for general / player movement.
        match event:
            # Player Movement
            case KeyDown(sym=KeySym.LEFT) | KeyDown(sym=KeySym.a) | KeyDown(sym=KeySym.KP_4):
                player_object.x -= player_object.movement_speed
            case KeyDown(sym=KeySym.RIGHT) | KeyDown(sym=KeySym.d) | KeyDown(sym=KeySym.KP_6):
                player_object.x += player_object.movement_speed
            case KeyDown(sym=KeySym.UP) | KeyDown(sym=KeySym.w) | KeyDown(sym=KeySym.KP_8):
                player_object.y -= player_object.movement_speed
            case KeyDown(sym=KeySym.DOWN) | KeyDown(sym=KeySym.s) | KeyDown(sym=KeySym.KP_2):
                player_object.y += player_object.movement_speed

            # Quit
            case KeyDown(sym=KeySym.q) | Quit():
                raise SystemExit()


# Draws all entities to console
def draw(console: Console, context: Context, entities: set, player_object: player.Player) -> None:
    console.clear()

    # Draws all objects
    for item in entities:
        console.print(item.x, item.y, item.icon, fg=item.color)

    # Debug setting - Prints players X/Y
    if config.debug:
        console.print(0, 0, "X: " + str(player_object.x) + " Y: " + str(player_object.y))

    # Writes to Console
    context.present(console)
