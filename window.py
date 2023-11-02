import config
import tcod.console


# Creates and returns a console based on the given width and height
def create_console() -> tcod.console.Console:
    try:
        return tcod.console.Console(config.width, config.height)
    except Exception as e:
        print('The console window could not be created. Error:', e)


# Creates and returns a tile set based on CP437.
def create_tile_set(filepath: str, cols: int, rows: int) -> tcod.tileset.Tileset:
    try:
        tile_set = tcod.tileset.load_tilesheet(filepath, cols, rows, tcod.tileset.CHARMAP_CP437)
        tcod.tileset.procedural_block_elements(tileset=tile_set)

        return tile_set
    except Exception as e:
        print('The tile set could not be created. Error:', e)
