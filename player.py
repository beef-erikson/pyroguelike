from character import Character
from attrs import define
import tcod.event


@define(eq=False)
class Player(Character):
    def on_move(self, event: tcod.event.Event) -> None:
        match event:
            case tcod.event.KeyDown(sym=tcod.event.KeySym.LEFT):
                self.x -= self.movement_speed
            case tcod.event.KeyDown(sym=tcod.event.KeySym.RIGHT):
                self.x += self.movement_speed
            case tcod.event.KeyDown(sym=tcod.event.KeySym.UP):
                self.y -= self.movement_speed
            case tcod.event.KeyDown(sym=tcod.event.KeySym.DOWN):
                self.y += self.movement_speed
