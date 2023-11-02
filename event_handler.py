from event_actions import Action, EscapeAction, MovementAction
import tcod.event


class EventHandler(tcod.event.EventDispatch[Action]):
    """
        Event handler that implements functionality based on EventDispatch function overrides.
    """

    # This triggers when the X button is pressed, program terminated.
    def ev_quit(self, event: tcod.event.Quit) -> None:
        raise SystemExit()

    # This triggers whenever a key is depressed.
    def ev_keydown(self, event: tcod.event.KeyDown) -> Action | None:
        action = None
        key = event.sym

        # Player movement
        if key == key.LEFT or key == key.a or key == key.KP_4:
            action = MovementAction(x=-1, y=0)
        elif key == key.RIGHT or key == key.d or key == key.KP_6:
            action = MovementAction(x=1, y=0)
        elif key == key.UP or key == key.w or key == key.KP_8:
            action = MovementAction(x=0, y=-1)
        elif key == key.DOWN or key == key.s or key == key.KP_2:
            action = MovementAction(x=0, y=1)

        # Quit the game
        elif key == key.ESCAPE or key == key.q:
            action = EscapeAction()

        return action
