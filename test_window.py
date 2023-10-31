import window


def test_create_console():
    assert str(type(
        window.create_console(500, 400))) == "<class 'tcod.console.Console'>"


def test_create_tileset():
    assert (str(type(window.create_tileset('assets/Cheepicus_14x14.png', 16, 16)))
            == "<class 'tcod.tileset.Tileset'>")
