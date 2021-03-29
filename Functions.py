import pygame
import Settings
from Color import Color

def text_display(screen, x, y, string, size, color = Color.black, background = Color.white, allign = 'center'):  # centered text display
    """

    :param screen:
    :param x:
    :param y:
    :param string:
    :param size:
    :param color:
    :param background:
    :param allign:
    """
    myfont = pygame.font.SysFont('cabria', size)
    text = myfont.render(string, True, color, background)

    if allign == 'center': #text display in center allignment
        textrect = text.get_rect()  #center of textbox
        textrect.centerx = x
        textrect.centery = y
        screen.blit(text, textrect)

    elif allign == 'left':
        text = myfont.render(string, True, color, background) #(x,y): upper left corner of textbox
        screen.blit(text, (x, y))

def text_box(x, y, string, size):
    """

    :param x:
    :param y:
    :param string:
    :param size:
    :return:
    """
    myfont = pygame.font.SysFont('cabria', size)
    text = myfont.render(string, True, (0,0,0), (0,0,0))

    textrect = text.get_rect()  # center of textbox
    textrect.centerx = x
    textrect.centery = y

    return textrect

def update_delay(milisecond):
    """

    :param milisecond:
    """
    pygame.display.flip()
    pygame.time.delay(milisecond)


def buttonpress_detect():
    """

    """
    RUNNING, PAUSE = 0, 1
    state = RUNNING
    while True:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    raise SystemExit

                if e.key == pygame.K_SPACE:
                    Settings.keyboard_space_press = True

                if e.key == pygame.K_LEFT:
                    Settings.keyboard_left_press = True

                if e.key == pygame.K_RIGHT:
                    Settings.keyboard_right_press = True

                if e.key == pygame.K_UP:
                    Settings.keyboard_up_press = True

                if e.key == pygame.K_DOWN:
                    Settings.keyboard_down_press = True

                if e.key == pygame.K_r:
                    Settings.keyboard_r_press = True

                elif e.key == pygame.K_BACKSPACE:
                    Settings.keyboard_back_press = True

                elif e.key == pygame.K_w:
                    Settings.keyboard_w_press = True

                elif e.key == pygame.K_s:
                    Settings.keyboard_s_press = True

                elif e.key == pygame.K_a:
                    Settings.keyboard_a_press = True

                elif e.key == pygame.K_d:
                    Settings.keyboard_d_press = True


            elif e.type == pygame.MOUSEBUTTONUP:
                Settings.mouse_click_position = pygame.mouse.get_pos()

        while state == PAUSE:
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        pygame.quit()
                        raise SystemExit
                    elif e.key == pygame.K_SPACE:
                        state = RUNNING
        break

def buttonpress_reset():
    """

    """
    Settings.keyboard_space_press = None
    Settings.keyboard_left_press = None
    Settings.keyboard_right_press = None
    Settings.keyboard_up_press = None
    Settings.keyboard_down_press = None
    Settings.keyboard_r_press = None
    Settings.keyboard_back_press = None
    Settings.keyboard_w_press = None
    Settings.keyboard_s_press = None
    Settings.keyboard_a_press = None
    Settings.keyboard_d_press = None

def mouse_reset():
    """

    """
    Settings.mouse_click_position = None

def wait_for_arrow():
    """

    :return:
    """
    if Settings.keyboard_left_press or \
            Settings.keyboard_right_press or \
            Settings.keyboard_up_press or \
            Settings.keyboard_down_press or \
            Settings.keyboard_w_press or \
            Settings.keyboard_s_press or \
            Settings.keyboard_a_press or \
            Settings.keyboard_d_press:
        return True

def timer_string(time_int):
    """
    :param int time_sec: time in seconds
    :param str: time on format mm:ss (e.g.: 01:23 = 1 minute and 23 seconds)
    """
    time_sec = str(time_int % 60)
    if len(time_sec) < 2:
        time_sec = '0' + time_sec

    time_min = str(time_int // 60)
    return time_min + ':' + time_sec