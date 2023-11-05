""" Code to handle map bounds and rendering. """
from numpy import full
from tcod.console import Console

import config
from map import tiles
from process import color

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

    # TODO - Left off here.
    def render_map(self, console: Console) -> None:
        """ Renders the map to fill with tiles """
        console.rgba[0:config.MAP_WIDTH, 0:config.MAP_HEIGHT] = tiles.standard_floor['dark']
            # (ord(' '), color.get_rgba(color.BLACK, 255), color.get_rgba(color.DARK_BLUE, 255))

# tiles.standard_floor['dark']
