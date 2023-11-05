""" Code to handle map bounds and rendering. """
from numpy import full
from tcod.console import Console
import tiles


class MainMap:
    """ MainMap class used for making the dungeon maps. """
    def __init__(self, width: int, height: int):
        """ Map size and tiles (currently set to standard_floor and standard_wall) """
        self.width, self.height = width, height
        self.map_tiles = full((width, height), fill_value=tiles.standard_floor, order="F")
        self.map_tiles[20:30, 10] = tiles.standard_wall

    # TODO - Implement this check into the entity class
    def is_in_bounds(self, x: int, y: int):
        """ Checks to see if entity is in bounds of the map. """
        return 0 <= x < self.width and 0 <= y < self.height

    def render_map(self, console: Console) -> None:
        """ Renders the map to fill with tiles """
        console.rgba[0:self.width, 0:self.height] = self.map_tiles["dark"]
