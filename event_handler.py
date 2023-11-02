import tcod.event
from event_actions import Action, EscapeAction, MovementAction


class EventHandler(tcod.event.EventDispatch[Action]):
    # This triggers when the X button is pressed, program terminated.
    def ev_quit(self, event: tcod.event.Quit):
        raise SystemExit()

    # This triggers whenever a key is depressed.
    def ev_keydown(self, event: tcod.event.KeyDown) -> Action | None:
        action = None
        key = event.sym

        if key == key.LEFT or key == key.a or key == key.KP_4:
            action = MovementAction()
        elif key == key.RIGHT or key == key.d or key == key.KP_6:
            action = MovementAction()
        elif key == key.UP or key == key.w or key == key.KP_8:
            action = MovementAction()
        elif key == key.DOWN or key == key.s or key == key.KP_2:
            action = MovementAction()

        # Quit the game
        elif key == key.ESCAPE or key == key.q:
            action = EscapeAction()

        return action
