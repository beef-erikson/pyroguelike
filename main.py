import tcod.tileset
import tcod.context
import window


def main() -> None:
    console = window.create_console(80, 50)
    tileset = window.create_tileset('assets/Cheepicus_14x14.png', 16, 16)

    with tcod.context.new(console=console, tileset=tileset, title="pyroguelike", vsync=True) as context:
        while True:
            console.print(x=1, y=1, string="@")
            context.present(console)
            for event in tcod.event.wait():
                print(event)  # event tracking
                if isinstance(event, tcod.event.Quit):
                    raise SystemExit()


if __name__ == '__main__':
    main()
