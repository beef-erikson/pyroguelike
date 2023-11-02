from attrs import define
from entity import Entity


@define(eq=False)
class Player(Entity):
    """
        All Player-specific things will be kept here.
    """
    pass
