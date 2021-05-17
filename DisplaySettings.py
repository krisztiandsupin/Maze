from Color import Color


class DisplaySettings:
    """
    Stores colors and font sizes for displaying text
    """
    def __init__(self, text_color=Color.navy, text_color_light=Color.navy_light, text_color_inprogress=Color.grey,
                 text_size=25):
        # colors
        self.text_color = text_color
        self.text_color_light = text_color_light
        self.text_color_inprogress = text_color_inprogress

        # font sizes
        self.text_size = text_size
        self.title_size = self.text_size * 3