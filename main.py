import pygame
from config import *
from pipe import Pipe
from evaluator import *
from canvas import *
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()
# success_sound = pygame.mixer.Sound('success.wav')
screen = pygame.display.set_mode((WIDTH,HEIGHT))

my_font = pygame.font.init()

my_font = pygame.font.SysFont('Arial',10)


pygame.display.set_caption("copy cat")

clock = pygame.time.Clock()

drawing_surface = pygame.Surface((CANVAS_WIDTH,HEIGHT))

clear_canvas(drawing_surface)


pipe_list = []

for pipes in range(150):
    pipe_list.append(Pipe())




current_surface = render_pipe(pipe_list)
running = True

total_generations = 0
frog_hits = 0
accuracy = 0.0
has_started = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:            
            if event.key == pygame.K_c:
                clear_canvas(drawing_surface)

    if handle_mouse(drawing_surface, True):
        has_started = True

    if has_started:
        current_loss = calculate_loss(drawing_surface, current_surface)

        for _ in range(20):
            mutated_list = [p.copy() for p in pipe_list]
            random_pipe = random.choice(mutated_list)
            did_frog_jump = random_pipe.mutate()
            total_generations += 1
            if did_frog_jump:
                frog_hits += 1
            
            maximum_possible_loss = CANVAS_WIDTH * HEIGHT * 705

            accuracy = 100 - ((current_loss / maximum_possible_loss)) * 100
            if accuracy > 99.99:
                running = False
                break
            mutated_surf = render_pipe(mutated_list)
            mutated_loss = calculate_loss(drawing_surface,mutated_surf)

            if mutated_loss <= current_loss:
                # if did_frog_jump:
                #     success_sound.play()
                
                pipe_list = mutated_list
                current_loss = mutated_loss
                current_surface = mutated_surf

    screen.fill(COLOR_BG)
    
    # 2. Paste your drawing canvas on the left half (0, 0)
    screen.blit(drawing_surface, (0, 0))
    
    # 3. Paste the winning AI pipe canvas on the right half (CANVAS_WIDTH, 0)
    # We render the current optimized pipe_list directly here
    screen.blit(current_surface, (CANVAS_WIDTH, 0))
    
    # 4. Draw the divider line down the exact middle
    pygame.draw.line(screen, COLOR_GRID, (CANVAS_WIDTH, 0), (CANVAS_WIDTH, HEIGHT), 2)
    
    text_surface = my_font.render(f"Accuracy: {accuracy:.2f}% Frog hits: {frog_hits} Total Generations: {total_generations}", True,(255,255,255))
    screen.blit(text_surface,(10,410))
    # 5. Push the completed visual frames to your desktop monitor
    pygame.display.flip()
    
    # 6. Keep the program running at your stable FPS setting
    clock.tick(FPS)

pygame.quit()
