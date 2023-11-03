"""
    Used in conjunction with the event handler to define action classes we can use elsewhere.
"""
from attrs import define


class Action:
    """ Used for all handling. """
    pass


class EscapeAction(Action):
    """ Used when a 'quit' key is pressed. """
    pass


@define
class MovementAction(Action):
    """ Used when a movement key is pressed. """
    x: int
    y: int
