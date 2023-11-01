import tcod.tileset
import tcod.context
import tcod.event
from character import Character
from player import Player
import window


def main() -> None:
    console = window.create_console(80, 50)
    tileset = window.create_tileset('assets/Cheepicus_14x14.png', 16, 16)

    player = Player(x=console.width // 2, y=console.height // 2, icon='@', movement_speed=1)

    with tcod.context.new(console=console, tileset=tileset, title="PyRoguelike", vsync=True) as context:
        while True:
            console.clear()

            player.on_draw(console)

            # debug
            console.print(0, 0, "X: " + str(player.x) + " Y: " + str(player.y))

            context.present(console)

            for event in tcod.event.wait():

                print(event)  # event tracking
                player.on_move(event)

                # Quits out
                if isinstance(event, tcod.event.Quit):
                    raise SystemExit()


if __name__ == '__main__':
    main()
