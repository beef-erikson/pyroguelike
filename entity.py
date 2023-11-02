from attrs import define
import tcod.console


# Any mob, item, player and so on that displays on the map inherits this class.
@define(eq=False)
class Entity:
    x: int
    y: int
    icon: str
    color: tuple
    movement_speed: int

    def on_draw(self, console: tcod.console.Console) -> None:
        # Draws the character
        console.print(self.x, self.y, self.icon)
