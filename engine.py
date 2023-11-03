"""Module for processing input and drawing."""
from tcod.console import Console
from tcod.context import Context
from tcod.event import wait
import config
from event_actions import EscapeAction, MovementAction
from event_handler import EventHandler
from player import Player


def process_input(player: Player) -> None:
    """ Handles controls, quitting, etc. """
    event_handler = EventHandler()

    # Starts the wait event that listens for events.
    for event in wait():

        # Event tracking
        if config.DEBUG:
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


def draw(console: Console, context: Context, entities: set, player: Player) -> None:
    """Draws all entities to console"""
    console.clear()

    # Draws all objects
    for item in entities:
        console.print(item.x, item.y, item.icon, fg=item.color)

    # Debug setting - Prints players X/Y
    if config.DEBUG:
        console.print(0, 0, "X: " + str(player.x) + " Y: " + str(player.y))

    # Writes to Console
    context.present(console)
