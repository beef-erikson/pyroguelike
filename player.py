from entity import Entity
from attrs import define
import tcod.event


@define(eq=False)
class Player(Entity):
    def on_move(self, event: tcod.event.Event) -> None:
        match event:
            case tcod.event.KeyDown(sym=tcod.event.KeySym.LEFT) | tcod.event.KeyDown(sym=tcod.event.KeySym.a):
                self.x -= self.movement_speed
            case tcod.event.KeyDown(sym=tcod.event.KeySym.RIGHT) | tcod.event.KeyDown(sym=tcod.event.KeySym.d):
                self.x += self.movement_speed
            case tcod.event.KeyDown(sym=tcod.event.KeySym.UP) | tcod.event.KeyDown(sym=tcod.event.KeySym.w):
                self.y -= self.movement_speed
            case tcod.event.KeyDown(sym=tcod.event.KeySym.DOWN) | tcod.event.KeyDown(sym=tcod.event.KeySym.s):
                self.y += self.movement_speed
