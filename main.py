import tcod.tileset
import tcod.context
import tcod.event
from character import Character
from window import create_tileset, create_console


def main() -> None:
    console = create_console(80, 50)
    tileset = create_tileset('assets/Cheepicus_14x14.png', 16, 16)

    player = Character(x=console.width // 2, y=console.width // 2, icon='@')

    with tcod.context.new(console=console, tileset=tileset, title="PyRoguelike", vsync=True) as context:
        while True:
            console.clear()

            player.on_draw(console)

            context.present(console)

            for event in tcod.event.wait():
                print(event)  # event tracking
                if isinstance(event, tcod.event.Quit):
                    raise SystemExit()


if __name__ == '__main__':
    main()
