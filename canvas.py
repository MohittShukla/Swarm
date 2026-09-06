import pygame
from config import CANVAS_WIDTH,COLOR_BG,COLOR_WHITE


def clear_canvas(drawing_surface):
    drawing_surface.fill(COLOR_BG)
def handle_mouse(drawing_surface,is_drawing_flag): 
    mouse_btns = pygame.mouse.get_pressed()
    if mouse_btns[0] and is_drawing_flag:
        mouse_x,mouse_y = pygame.mouse.get_pos()
        if mouse_x < CANVAS_WIDTH:
            pygame.draw.circle(drawing_surface,COLOR_WHITE,(mouse_x,mouse_y),8)
    
    if mouse_btns[0]:
        return True
    return False

