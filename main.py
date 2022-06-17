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
LIGHT_GRAY = (211, 211, 211)
DARK_GRAY = (49, 49, 49)

C4 = Button(WHITE, 0, 0, 100, HEIGHT, "C4", 'Piano.ff.C4.mp3')
Db4 = Button(BLACK, 75, 0, 50, 250, "Db4", 'Piano.ff.Db4.mp3')
D4 = Button(WHITE, 100, 0, 100, HEIGHT, "D4", 'Piano.ff.D4.mp3')
Eb4 = Button(BLACK, 175, 0, 50, 250, "Eb4", 'Piano.ff.Eb4.mp3')
E4 = Button(WHITE, 200, 0, 100, HEIGHT, "E4", 'Piano.ff.E4.mp3')
F4 = Button(WHITE, 300, 0, 100, HEIGHT, "F4", 'Piano.ff.F4.mp3')
Gb4 = Button(BLACK, 375, 0, 50, 250, "Gb4", 'Piano.ff.Gb4.mp3')
G4 = Button(WHITE, 400, 0, 100, HEIGHT, "G4", 'Piano.ff.G4.mp3')
Ab4 = Button(BLACK, 475, 0, 50, 250, "Ab4", 'Piano.ff.Ab4.mp3')
A4 = Button(WHITE, 500, 0, 100, HEIGHT, "A4", 'Piano.ff.A4.mp3')
Bb4 = Button(BLACK, 575, 0, 50, 250, "Bb4", 'Piano.ff.Bb4.mp3')
B4 = Button(WHITE, 600, 0, 100, HEIGHT, "B4", 'Piano.ff.B4.mp3')

keys_list = [C4, D4, Db4, E4, F4, Eb4, G4, Gb4, A4, Ab4, B4, Bb4]

def draw_window():
    WIN.fill(WHITE)
    for key in keys_list:
        key.draw(WIN)

    pygame.display.update()

def handle_motion(mouse_pos):
    for key in keys_list:
        if key.isWhite:
            if key.isOver(mouse_pos):
                key.color = LIGHT_GRAY
            else:
                key.color = WHITE
        if not key.isWhite:
            if key.isOver(mouse_pos):
                key.color = DARK_GRAY
            else:
                key.color = BLACK

def handle_click(mouse_pos):
    if Db4.isOver(mouse_pos):
        Db4.play()
    elif C4.isOver(mouse_pos):
        C4.play()
    elif Eb4.isOver(mouse_pos):
        Eb4.play()
    elif D4.isOver(mouse_pos):
        D4.play()
    elif E4.isOver(mouse_pos):
        E4.play()
    elif Gb4.isOver(mouse_pos):
        Gb4.play()
    elif F4.isOver(mouse_pos):
        F4.play()
    elif Ab4.isOver(mouse_pos):
        Ab4.play()
    elif G4.isOver(mouse_pos):
        G4.play()
    elif Bb4.isOver(mouse_pos):
        Bb4.play()
    elif A4.isOver(mouse_pos):
        A4.play()
    elif B4.isOver(mouse_pos):
        B4.play()

def handle_pressed_key(pressed_key):
    if pressed_key == pygame.K_a:
        C4.play()
        C4.color = LIGHT_GRAY
    if pressed_key == pygame.K_w:
        Db4.play()
        Db4.color = DARK_GRAY
    if pressed_key == pygame.K_s:
        D4.play()
        D4.color = LIGHT_GRAY
    if pressed_key == pygame.K_e:
        Eb4.play()
        Eb4.color = DARK_GRAY
    if pressed_key == pygame.K_d:
        E4.play()
        E4.color = LIGHT_GRAY
    if pressed_key == pygame.K_f:
        F4.play()
        F4.color = LIGHT_GRAY
    if pressed_key == pygame.K_t:
        Gb4.play()
        Gb4.color = DARK_GRAY
    if pressed_key == pygame.K_g:
        G4.play()
        G4.color = LIGHT_GRAY
    if pressed_key == pygame.K_y:
        Ab4.play()
        Ab4.color = DARK_GRAY
    if pressed_key == pygame.K_h:
        A4.color = LIGHT_GRAY
        A4.play()
    if pressed_key == pygame.K_u:
        Bb4.play()
        Bb4.color = DARK_GRAY
    if pressed_key == pygame.K_j:
        B4.play()
        B4.color = LIGHT_GRAY



def handle_unpressed_key(unpressed_key):
    if unpressed_key == pygame.K_a:
        C4.stop()
        C4.color = WHITE
    if unpressed_key == pygame.K_w:
        Db4.stop()
        Db4.color = BLACK
    if unpressed_key == pygame.K_s:
        D4.stop()
        D4.color = WHITE
    if unpressed_key == pygame.K_e:
        Eb4.stop()
        Eb4.color = BLACK
    if unpressed_key == pygame.K_d:
        E4.stop()
        E4.color = WHITE
    if unpressed_key == pygame.K_f:
        F4.stop()
        F4.color = WHITE
    if unpressed_key == pygame.K_t:
        Gb4.stop()
        Gb4.color = BLACK
    if unpressed_key == pygame.K_g:
        G4.stop()
        G4.color = WHITE
    if unpressed_key == pygame.K_y:
        Ab4.stop()
        Ab4.color = BLACK
    if unpressed_key == pygame.K_h:
        A4.stop()
        A4.color = WHITE
    if unpressed_key == pygame.K_u:
        Bb4.stop()
        Bb4.color = BLACK
    if unpressed_key == pygame.K_j:
        B4.stop()
        B4.color = WHITE


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
                pygame.mixer.stop()
            if event.type == pygame.KEYDOWN:
                handle_pressed_key(event.key)
            if event.type == pygame.KEYUP:
                handle_unpressed_key(event.key)

if __name__ == '__main__':
    main()
