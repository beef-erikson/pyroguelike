""" Code to handle map bounds and rendering. """
from numpy import full
from tcod.console import Console
import config
from map import tiles


class MainMap:
    """ MainMap class used for making the dungeon maps. """
    def __init__(self, width: int, height: int, width_buffer: int, height_buffer: int):
        """ Map size and tiles (currently set to standard_floor and standard_wall) """
        self.width, self.height = width, height
        self.width_buffer = width_buffer
        self.height_buffer = height_buffer
        self.map_tiles = full((height - height_buffer, width - width_buffer),
                              fill_value=tiles.standard_floor, order="F")

    # TODO - Implement this check into the entity class
    def is_in_bounds(self, x: int, y: int):
        """ Checks to see if entity is in bounds of the map. """
        return 0 <= x < self.width and 0 <= y < self.height

    def render_map(self, console: Console) -> None:
        """ Renders the map to fill with tiles """
        console.rgba[self.height_buffer:self.height, self.width_buffer:self.width]\
            = self.map_tiles['dark']
        console.rgba[20, 35:45] = tiles.standard_wall['dark']
        console.rgba[20:31, 45] = tiles.standard_wall['dark']
        console.rgba[30, 35:45] = tiles.standard_wall['dark']
