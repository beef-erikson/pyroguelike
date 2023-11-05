""" Manage tiles for mapping. """
import numpy

# Holds the character, foreground and background colors.
tile_graphic = numpy.dtype(
    [
        ('character', numpy.character),
        ('fg', '3B'),  # 3 bytes needs to hold color values.
        ('bg', '3B')
    ]
)

# Tile properties.
tile_props = numpy.dtype(
    [
        ('walkable', numpy.bool),  # Can the player walk through it?
        ('transparent', numpy.bool),  # Can this talk been seen through?
        ('dark', tile_graphic)  # Used when the player can't see from FOV.
    ]
)

