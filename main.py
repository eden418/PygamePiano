import pygame
import os

from button_class import Button

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1200, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Eden's Piano")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

MIDDLE_C = Button(WHITE, 0, 0, 100, HEIGHT, "C4")
MIDDLE_C_SOUND = pygame.mixer.Sound(os.path.join('piano notes', 'Piano.ff.C4.mp3'))
C_SHARP = Button(BLACK, 75, 0, 50, 250, "C4#", WHITE)
C_SHARP_SOUND = pygame.mixer.Sound(os.path.join('piano notes', 'Piano.ff.Db4.mp3'))


keys_list = [MIDDLE_C, C_SHARP]

def draw_window():
    WIN.fill(WHITE)
    MIDDLE_C.draw(WIN, BLACK)
    C_SHARP.draw(WIN, BLACK)

    pygame.display.update()

def handle_motion(mouse_pos):
    for key in keys_list:
        if key.isWhite:
            if key.isOver(mouse_pos):
                key.color = (211, 211, 211)
            else:
                key.color = (250, 250, 250)
        if not key.isWhite:
            if key.isOver(mouse_pos):
                key.color = (49, 49, 49)
            else:
                key.color = (0, 0, 0)

def handle_click(mouse_pos):
    if MIDDLE_C.isOver(mouse_pos):
        MIDDLE_C_SOUND.play()


def main():
    run = True
    while run:
        draw_window()
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                handle_motion(mouse_pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_click(mouse_pos)
            if event.type == pygame.MOUSEBUTTONUP:
                MIDDLE_C_SOUND.stop()

if __name__ == '__main__':
    main()
