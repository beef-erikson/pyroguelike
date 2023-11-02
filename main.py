import tcod.tileset
import tcod.context
import tcod.event
from player import Player
from entity import Entity
import window


def main() -> None:
    # Window and Tileset configuration
    console = window.create_console(80, 50)
    tileset = window.create_tileset('assets/Cheepicus_14x14.png', 16, 16)

    # Characters
    player = Player(x=console.width // 2, y=console.height // 2, icon='@', movement_speed=1, color=(25, 255, 255))
    npc = Entity(x=15, y=20, icon='&', movement_speed=1, color=(44, 255, 33))

    # Main Game Loop
    with tcod.context.new(console=console, tileset=tileset, title="PyRoguelike", vsync=True) as context:
        while True:
            console.clear()

            # Characters
            player.on_draw(console)
            npc.on_draw(console)

            # Debug
            console.print(0, 0, "X: " + str(player.x) + " Y: " + str(player.y))

            context.present(console)

            # Events
            for event in tcod.event.wait():
                print(event)  # event tracking

                # player movement
                player.on_move(event)

                # quits
                if isinstance(event, tcod.event.Quit):
                    raise SystemExit()


if __name__ == '__main__':
    main()
