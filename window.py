import tcod.console


# Creates and returns a console based on the given width and height
def create_console(width: int, height: int) -> tcod.console.Console:
    try:
        return tcod.console.Console(width, height)
    except Exception as e:
        print('The console window could not be created. Error:', e)


def create_tileset(filepath: str, cols: int, rows: int) -> tcod.tileset.Tileset:
    try:
        tileset = tcod.tileset.load_tilesheet(filepath, cols, rows, tcod.tileset.CHARMAP_CP437)
        tcod.tileset.procedural_block_elements(tileset=tileset)

        return tileset
    except Exception as e:
        print('The tileset could not be created. Error:', e)
