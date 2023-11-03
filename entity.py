"""Any mob, item, player and son on that displays on the map."""
from attrs import define
import tcod.console


@define(eq=False)
class Entity:
    x: int
    y: int
    icon: str
    color: tuple
    movement_speed: int

    # Draws the entity
    def on_draw(self, console: tcod.console.Console) -> None:
        console.print(self.x, self.y, self.icon, fg=self.color)

    # pylint: disable=E1101
    def move(self, x: int, y: int) -> None:
        """ Moves the Entity. """
        # pylint: disable=E1101
        self.x += x
        # pylint: disable=E1101
        self.y += y
