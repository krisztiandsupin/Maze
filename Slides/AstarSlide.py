import Functions
import MazeFunctions
import Settings

from Color import Color
from Text import Text
from Settings import screen as screen_settings

screen_size = screen_settings.screen_size

def astar_slide(screen, display_settings, maze_solve):
    text_title = Text((screen_size[0] // 2, int(screen_size[1] * 0.1)), 'A* Algorithm',
                      int(display_settings.title_size), display_settings.text_color)
    screen.fill(Color.white)
    text_title.show(screen)
    astar_slide1(screen, maze_solve)

def draw_candidates(screen, candidates_list, index_text_size=30, delay=100):
    for cell, distance in candidates_list:
        cell.color(screen, Color.gold_light, graph_bool=True)
        cell.text_display(screen, str(distance), index_text_size, text_color=Color.black, background_color=Color.gold_light)
    MazeFunctions.update_delay(delay)

def astar_slide1(screen, maze_solve):
    """

    """
    maze_solve.draw(screen, visibility_bool=False)
    MazeFunctions.update_delay(1000)
    maze_solve.solve(algorithm='astar')

    print(maze_solve.maze_candidates)
    print(maze_solve.solution_path)
    step = 0
    while step < len(maze_solve.visited):
        Functions.buttonpress_detect()
        candidates_step = maze_solve.maze_candidates[step]
        if Settings.keyboard_space_press or Settings.keyboard_arrows_pressed() or Settings.keyboard_wsad_pressed():
            Functions.buttonpress_reset()
            highlight_counter = 0
            while not Settings.keyboard_space_press:
                Functions.buttonpress_detect()
                if (Settings.keyboard_right_press or Settings.keyboard_d_press) and step < len(maze_solve.visited):
                    if highlight_counter % 2 == 0 and (step < len(maze_solve.visited) - 1):
                        draw_candidates(screen, candidates_step, index_text_size=30, delay=100)
                        highlight_counter += 1
                    else:
                        maze_solve.visited[step][0][0].color(screen, Color.gold, graph_bool=True)
                        MazeFunctions.update_delay(200)
                        highlight_counter += 1
                        step += 1


        Functions.buttonpress_reset()
        candidates_step = maze_solve.maze_candidates[step]
        draw_candidates(screen, candidates_step, index_text_size=30, delay=100)

        maze_solve.visited[step][0][0].color(screen, Color.gold, graph_bool=True)
        MazeFunctions.update_delay(200)
        step += 1

    last_candidates = [element[0] for element in maze_solve.maze_candidates[-1]]
    last_candidates.remove(maze_solve.end)
    for cell in last_candidates:
        cell.color(screen, Color.white, graph_bool=True)

    for cell_index in maze_solve.solution_path:
        maze_solve.cell_list[cell_index].color(screen, Color.blue_light, graph_bool=True)
        MazeFunctions.update_delay(100)


    while True:
        MazeFunctions.update_delay(1000)
    # maze_kruskal.draw_frame(screen)

