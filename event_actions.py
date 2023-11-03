from attrs import define
"""
    Used in conjunction with the event handler to define action classes we can use elsewhere.
"""


class Action:
    pass


class EscapeAction(Action):
    pass


@define
class MovementAction(Action):
    x: int
    y: int
