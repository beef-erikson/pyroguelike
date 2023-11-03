import config
from event_actions import EscapeAction, MovementAction
from event_handler import EventHandler
from player import Player
from tcod.console import Console
from tcod.context import Context
from tcod.event import wait


# Handles controls, quitting, etc.
def process_input(player: Player) -> None:
    event_handler = EventHandler()

    # Starts the wait event that listens for events.
    for event in wait():

        # Event tracking
        if config.debug:
            print(event)

        action = event_handler.dispatch(event)

        # Event handler responses
        if action is None:
            continue

        # Move the player based on movement speed.
        if isinstance(action,  MovementAction):
            speed = player.movement_speed
            player.move(action.x * speed, action.y * speed)

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
