import Functions
import Settings
import pygame

from Text import Text

class Box:
    def __init__(self, position, size, color, color_click, is_active):
        """
        :param tuple position: center of the box
        :param int size: side size of the box
        :param tuple color: color of the text
        :param bool is_active: True: 'X' is displayed in box

        """
        self.position = position
        self.size = size
        self.color = color
        self.is_active = is_active
        self.color_click = color_click
        self.x = Text(position, 'X', self.size, color, self.color_click)

    def show(self, screen, color = None):
        if color == None:
            color = self.color

        pygame.draw.rect(screen, color, [self.position[0] - self.size // 2, self.position[1] - self.size // 2, \
                          self.size, self.size], 3)
        if self.is_active:
            self.x.show(screen, self.color)

        Functions.text_display(screen, self.position[0], self.position[1], 'X', self.size, color)

    def is_clicked(self):
        mouse_click_position = Settings.mouse_click_position

        if (mouse_click_position != None and \
            mouse_click_position[0] >= self.position[0] - self.size // 2 and \
            mouse_click_position[0] <= self.position[0] + self.size // 2 and \
            mouse_click_position[1] >= self.position[1] - self.size // 2 and \
            mouse_click_position[1] <= self.position[1] + self.size // 2):
            print('box clicked')
            return True

        else:
            return False

    def show_click(self, screen):
        pygame.draw.rect(screen, self.color, [self.position[0] - self.size // 2, self.position[1] - self.size // 2, \
                                         self.size, self.size], 3)
        if self.is_active:
            self.x.show(screen, self.color)
        else:
            self.x.show(screen, self.color_click)
