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
