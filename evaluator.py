import pygame
import numpy as np
from config import CANVAS_WIDTH,HEIGHT,COLOR_BG,COLOR_PIPE

def render_pipe(pipe_list):
    new_surface = pygame.Surface((CANVAS_WIDTH,HEIGHT))
    new_surface.fill(COLOR_BG)
   

    for pipe in pipe_list:
        start_point = (pipe.x,pipe.y)
        end_point = (pipe.x,pipe.y + pipe.length)
        width = pipe.thickness
        pygame.draw.line(
            new_surface,
            COLOR_PIPE,
            start_point,
            end_point,
            width
        )

    return new_surface


def calculate_loss(target_surf,test_surf):
    # converting target and test surface both to a np 3d array
    target_arr = pygame.surfarray.pixels3d(target_surf)
    test_arr = pygame.surfarray.pixels3d(test_surf)
    # converting both the arrays to 16 bit instead of 8 bit so that there is no mathematical error
    target_16bit = target_arr.astype(np.int16)
    test_16bit = test_arr.astype(np.int16)

    pixel_differences = target_16bit - test_16bit

    positive_difference = np.abs(pixel_differences)

    total_error = np.sum(positive_difference)

    return total_error
