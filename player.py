from entity import Entity
from attrs import define
from tcod.event import KeyDown, Event, KeySym


@define(eq=False)
class Player(Entity):
    # Todo - Implement bounds
    def on_move(self, event: Event) -> None:
        match event:
            # Movement
            case KeyDown(sym=KeySym.LEFT) | KeyDown(sym=KeySym.a):
                self.x -= self.movement_speed
            case KeyDown(sym=KeySym.RIGHT) | KeyDown(sym=KeySym.d):
                self.x += self.movement_speed
            case KeyDown(sym=KeySym.UP) | KeyDown(sym=KeySym.w):
                self.y -= self.movement_speed
            case KeyDown(sym=KeySym.DOWN) | KeyDown(sym=KeySym.s):
                self.y += self.movement_speed
