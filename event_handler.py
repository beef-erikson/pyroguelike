"""
    Overrides tcod's event system to make use of the actions in event_action.
"""
import tcod.event
import config
from event_actions import Action, EscapeAction, MovementAction


class EventHandler(tcod.event.EventDispatch[Action]):
    """ Event handler that implements functionality based on EventDispatch function overrides. """

    def ev_quit(self, event: tcod.event.Quit) -> None:
        """ This triggers when the X button is pressed, program terminated. """
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Action | None:
        """ This triggers whenever a key is depressed. """
        action = None
        key = event.sym

        # Player movement: 4-Way controls
        if not config.EIGHT_WAY_CONTROL:
            match key:
                case key.LEFT | key.a | key.KP_4:
                    action = MovementAction(x=-1, y=0)
                case key.RIGHT | key.d | key.KP_6:
                    action = MovementAction(x=1, y=0)
                case key.UP | key.w | key.KP_8:
                    action = MovementAction(x=0, y=-1)
                case key.DOWN | key.s | key.KP_2:
                    action = MovementAction(x=0, y=1)

        # Player movement: 8-Way controls
        else:
            match key:
                case key.KP_1:
                    action = MovementAction(x=-1, y=1)  # SW
                case key.KP_2:
                    action = MovementAction(x=0, y=1)  # S
                case key.KP_3:
                    action = MovementAction(x=1, y=1)  # SE
                case key.KP_4:
                    action = MovementAction(x=-1, y=0)  # W
                case key.KP_6:
                    action = MovementAction(x=1, y=0)  # E
                case key.KP_7:
                    action = MovementAction(x=-1, y=-1)  # NW
                case key.KP_8:
                    action = MovementAction(x=0, y=-1)  # N
                case key.KP_9:
                    action = MovementAction(x=1, y=-1)  # NE

        # Quit the game
        if key in (key.ESCAPE, key.q):
            action = EscapeAction()

        return action
