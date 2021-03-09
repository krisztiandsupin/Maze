import Functions
import Settings
import pygame

from Color import Color

class Text:
    def __init__(self, position, text, size, color, color_click):
        """
        :param tuple position: center of the text
        :param str text: text string
        :param int size: size of the string
        :param tuple color: color of the text
        :param tuple color: color of the text if clicked

        """
        self.position = position
        self.text = text
        self.size = size
        self.color = color
        self.color_click = color_click

        # frame of the text tuple with 4 corners
        self.box = self.calculate_box()

    def calculate_box(self):
        rectangle = Functions.text_box(self.position[0], self.position[1], self.text, self.size)

        return ((rectangle[0] - 1, rectangle[1] - 1),
                (rectangle[0] + 1 + rectangle[2], rectangle[1] - 1),
                (rectangle[0] + 1 + rectangle[2], rectangle[1] + rectangle[3] + 1),
                (rectangle[0] - 1, rectangle[1] + rectangle[3] + 1))


    def show(self, screen, color = None):
        if color == None:
            color = self.color
        Functions.text_display(screen, self.position[0], self.position[1], self.text, self.size, color)

    def show_box(self, screen, color = None, line_thickness = 1):
        if color == None:
            color = self.color
        pygame.draw.polygon(screen, color, self.box, line_thickness)

    def is_clicked(self):
        mouse_click_position = Settings.mouse_click_position

        if (mouse_click_position != None and \
            mouse_click_position[0] >= self.box[0][0] and \
            mouse_click_position[0] <= self.box[1][0] and \
            mouse_click_position[1] >= self.box[0][1] and \
            mouse_click_position[1] <= self.box[2][1]):
            print('{0} clicked'.format(self.text))
            return True

        else:
            return False

    def show_click(self, screen):
        Functions.text_display(screen, self.position[0], self.position[1], self.text, self.size, self.color_click)
        Functions.update_delay(100)
        Functions.text_display(screen, self.position[0], self.position[1], self.text, self.size, self.color)
        Functions.update_delay(10)