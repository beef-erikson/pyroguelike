"""
    Main file that should be run to play the game.
"""
from tcod.context import new
from entities.entity import Entity
from entities.player import Player
from process import engine, window


def main() -> None:
    """ The main function where all the magic happens. """

    # Window and Tile_set configuration
    console = window.create_console()
    tile_set = window.create_tile_set('assets/Cheepicus_14x14.png', 16, 16)

    # TODO - Implement a MobFactory or something for spawning these in a 'better' way.
    # Characters
    player = Player(x=console.width // 2, y=console.height // 2,
                    icon='@', movement_speed=1, color=(25, 255, 255))
    npc = Entity(x=15, y=20, icon='&', movement_speed=1, color=(44, 255, 33))
    npc2 = Entity(x=45, y=33, icon='L', movement_speed=1, color=(3, 55, 255))
    item = Entity(x=20, y=2, icon='$', movement_speed=1, color=(255, 215, 0))

    # Store individual entity types here, we'll pass them on to draw iteratively.
    entities = {player, npc, npc2, item}

    # Main Game Loop
    with new(console=console, tileset=tile_set, title="PyRoguelike", vsync=True) as context:
        while True:
            # Draws debug, entities, and so on.
            engine.draw(console, context, entities, player)

            # Handles player movement, quitting, and so on.
            engine.process_input(player)


if __name__ == '__main__':
    main()
