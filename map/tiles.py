""" Manage tiles for mapping. """
from numpy import dtype, char, bool_, ndarray, array
from process import color

# Holds the character, foreground and background colors.
tile_graphic = dtype(
    [
        ('character', char),
        ('fg', '3B'),  # 3 bytes needs to hold color values.
        ('bg', '3B')
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
                # followed by the foreground RBG, then the background RGB.
                dark: (int, (int, int, int), (int, int, int))) -> ndarray:
    """ Returns a tile in the tile_props struct type"""
    return array((walkable, transparent, dark), dtype=tile_props)


# Create tiles here
standard_floor = create_tile(walkable=True, transparent=True,
                             dark=(ord(" "), color.BLACK, color.MIDNIGHT_BLUE))

standard_wall = create_tile(walkable=False, transparent=False,
                            dark=(ord(" "), color.BLACK, color.DARK_BLUE))
