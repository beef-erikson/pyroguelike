"""
    Used in conjunction with the event handler to define action classes we can use elsewhere.
"""
from attrs import define


class Action:
    """ Used for all handling. """


class EscapeAction(Action):
    """ Used when a 'quit' key is pressed. """


@define
class MovementAction(Action):
    """ Used when a movement key is pressed. """
    x: int
    y: int
