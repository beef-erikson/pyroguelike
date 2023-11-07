""" Manage tiles for mapping. """
from numpy import dtype, bool_, ndarray, array
from process import color

# Holds the character, foreground and background colors.
tile_graphic = dtype(
    [
        ('character', '4B'),  # 4 bytes need to hold unicode values.
        ('fg', '4B'),  # 4 bytes needs to hold color values for rgba.
        ('bg', '4B')
    ]
)

# Holds the tile properties.
tile_props = dtype(
    [
        ('walkable', bool_),  # Can the player walk through it?
        ('transparent', bool_),  # Can this tile been seen through?
        ('dark', tile_graphic)  # Can the player see this in his FOV?
    ]
)


def create_tile(walkable: int, transparent: int,
                # dark is defined with the character to draw,
                # followed by the foreground RGBA, then the background RGBA.
                dark: (int, (int, int, int, int), (int, int, int, int))) -> ndarray:
    """ Returns a tile in the tile_props struct type"""
    return array((walkable, transparent, dark), dtype=tile_props)


# Create tiles here
standard_floor = create_tile(walkable=True, transparent=True,
                             dark=(ord(" "), color.get_rgba(color.BLACK, 255),
                                   color.get_rgba(color.SLATE_GRAY, 255)))

standard_wall = create_tile(walkable=False, transparent=False,
                            dark=(ord(" "), color.get_rgba(color.BLACK, 255),
                                  color.get_rgba(color.SLATE_BLUE, 255)))
