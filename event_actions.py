from attrs import define


class Action:
    pass


class EscapeAction(Action):
    pass


@define
class MovementAction(Action):
    x: int
    y: int
