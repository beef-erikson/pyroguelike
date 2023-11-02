from entity import Entity
from attrs import define
from tcod.event import KeyDown, Event, KeySym, Quit


@define(eq=False)
class Player(Entity):
    # Todo - Implement bounds
    def on_event(self, event: Event) -> None:
        match event:
            # Movement
            case KeyDown(sym=KeySym.LEFT) | KeyDown(sym=KeySym.a) | KeyDown(sym=KeySym.KP_4):
                self.x -= self.movement_speed
            case KeyDown(sym=KeySym.RIGHT) | KeyDown(sym=KeySym.d) | KeyDown(sym=KeySym.KP_6):
                self.x += self.movement_speed
            case KeyDown(sym=KeySym.UP) | KeyDown(sym=KeySym.w) | KeyDown(sym=KeySym.KP_8):
                self.y -= self.movement_speed
            case KeyDown(sym=KeySym.DOWN) | KeyDown(sym=KeySym.s) | KeyDown(sym=KeySym.KP_2):
                self.y += self.movement_speed

            # Quit
            case KeyDown(sym=KeySym.q) | Quit():
                raise SystemExit()
