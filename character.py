from attrs import define
import tcod.console


@define(eq=False)
class Character:
    character_x: int
    character_y: int
    icon: str

    def on_draw(self, console: tcod.console.Console) -> None:
        # Draws the character
        console.print(self.character_x, self.character_y, self.icon)
