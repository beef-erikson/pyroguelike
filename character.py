from attrs import define
import tcod.console


@define(eq=False)
class Character:
    x: int
    y: int
    icon: str

    def on_draw(self, console: tcod.console.Console) -> None:
        # Draws the character
        console.print(self.x, self.y, self.icon)

    # TODO - Move into Player class and add some more inputs. Bounds are also broken, but might take care of itself.
    def on_event(self, event: tcod.event.Event) -> None:
        match event:
            case tcod.event.Quit():
                raise SystemExit()
            case tcod.event.KeyDown(sym=tcod.event.KeySym.LEFT):
                self.x -= 1
            case tcod.event.KeyDown(sym=tcod.event.KeySym.RIGHT):
                self.x += 1
            case tcod.event.KeyDown(sym=tcod.event.KeySym.UP):
                self.y -= 1
            case tcod.event.KeyDown(sym=tcod.event.KeySym.DOWN):
                self.y += 1
