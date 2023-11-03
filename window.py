"""
    Window helper functions and settings will be here.
"""
import config
import tcod.console


def create_console() -> tcod.console.Console:
    """ Creates and returns a console based on the given width and height. """
    try:
        return tcod.console.Console(config.WIDTH, config.HEIGHT)
    except Exception as e:
        print('The console window could not be created. Error:', e)
        raise SystemExit()


def create_tile_set(filepath: str, cols: int, rows: int) -> tcod.tileset.Tileset:
    """ Creates and returns a tile set based on CP437. """
    try:
        tile_set = tcod.tileset.load_tilesheet(filepath, cols, rows, tcod.tileset.CHARMAP_CP437)
        tcod.tileset.procedural_block_elements(tileset=tile_set)

        return tile_set
    except Exception as e:
        print('The tile set could not be created. Error:', e)
        raise SystemExit()
