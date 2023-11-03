"""Module for processing input and drawing."""
from tcod.console import Console
from tcod.context import Context
from tcod.event import wait
import process.color as color
import config
from datetime import datetime
from process.event_actions import EscapeAction, MovementAction
from process.event_handler import EventHandler
from entities.player import Player


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
        console.print(1, 1, "X: " + str(player.x) + " Y: " + str(player.y), fg=color.DARK_OLIVE_GREEN)

    # Displays the time
    if config.SHOW_TIME:
        print_time(console)

    # Writes to Console
    context.present(console)


def print_time(console: Console) -> None:
    """ Prints the current time """
    console.print(console.width - 12, console.height - 2,
                  datetime.now().strftime("%H:%M:%S %p"), fg=color.DARK_GRAY)