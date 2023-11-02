from attrs import define
import tcod.console


@define(eq=False)
class Entity:
    """
    Any mob, item, player and so on that displays on the map inherits this class.
    """
    x: int
    y: int
    icon: str
    color: tuple
    movement_speed: int

    # Draws the entity
    def on_draw(self, console: tcod.console.Console) -> None:
        console.print(self.x, self.y, self.icon, fg=self.color)

    # Todo - fix bounds.
    # Moves the entity
    def move(self, x: int, y: int) -> None:
        self.x += x
        self.y += y
