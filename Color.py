class Color:
    black = (0, 0, 0)
    white = (255, 255, 255)

    grey = (192, 192, 192)
    grey_light = (211, 211, 211)
    grey_dark = (169, 169, 169)
    grey_extra_dark = (100, 100, 100)

    red = (255, 0, 0)
    red_light = (250, 160, 150)
    red_dark = (250, 65, 80)
    red_extra_dark = (180, 40, 10)

    salmon = (250, 128, 114)
    salmon_light = (250, 200, 200)

    blue = (0, 110, 162)
    blue_light = (135, 206, 235)
    blue_dark = (0, 74, 111)

    navy = (0, 0, 128)
    navy_light = (127, 127, 255)

    green = (0, 170, 85)
    green_light = (145, 243, 96)
    green_extra_light = (200, 255, 200)
    green_dark = (0, 128, 64)

    yellow_light = (240, 230, 140)

    gold = (219, 186, 0)
    gold_light = (255, 215, 0)


class MazeColor:
    # basic
    background = Color.white
    line = Color.black
    start = Color.green_light
    end = Color.salmon

    # generation and solving
    highlight = Color.red_light
    select = Color.red_dark

    # solving
    visited = Color.yellow_light
    path = Color.blue_light