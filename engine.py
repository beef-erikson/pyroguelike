import config
import player
from tcod.event import KeyDown, KeySym, Quit, wait
from tcod.console import Console
from tcod.context import Context
from event_handler import EventHandler
from event_actions import EscapeAction, MovementAction


# Handles controls, quitting, etc.
def event_handling(player_object: player.Player) -> None:
    event_handler = EventHandler()

    for event in wait():
        # Event tracking
        if config.debug:
            print(event)

        action = event_handler.dispatch(event)
        if action is None:
            continue

        if isinstance(action,  MovementAction):
            player_object.move(1, 0)

        # Quits
        if isinstance(action, EscapeAction):
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
