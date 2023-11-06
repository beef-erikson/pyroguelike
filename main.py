"""
    Main file that should be run to play the game.
"""
from tcod.context import new

import config
from entities.entity import Entity
from entities.player import Player
from process import engine, window, color
from map.main_map import MainMap


def main() -> None:
    """ The main function where all the magic happens. """

    # Window and Tile_set configuration
    console = window.create_console()
    tile_set = window.create_tile_set('assets/Cheepicus_14x14.png', 16, 16)

    # TODO - Implement a MobFactory or something for spawning these in a 'better' way.
    # Characters
    player = Player(x=console.width // 2, y=console.height // 2,
                    icon='@', movement_speed=1, color=color.RED)
    npc = Entity(x=15, y=20, icon='&', movement_speed=1, color=color.DARK_SLATE_BLUE)
    npc2 = Entity(x=45, y=33, icon='L', movement_speed=1, color=color.BURLY_WOOD)
    item = Entity(x=20, y=26, icon='$', movement_speed=1, color=color.GOLD)

    # Store individual entity types here, we'll pass them on to draw iteratively.
    entities = {player, npc, npc2, item}

    # Create map
    main_map = MainMap(config.MAP_WIDTH, config.MAP_HEIGHT)

    # Main Game Loop
    with new(console=console, tileset=tile_set, title="PyRoguelike", vsync=True) as context:
        while True:
            # Draws debug, entities, and so on.
            engine.draw(console=console, context=context, entities=entities,
                        player=player, main_map=main_map)

            # Handles player movement, quitting, and so on.
            engine.process_input(player)


if __name__ == '__main__':
    main()
