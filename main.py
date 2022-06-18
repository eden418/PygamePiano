"""
This is a virtual piano made with pygame.
It makes a GUI that lets you click each key to play its sound.
You can also play with your keyboard.
After you quit the application it shows you the sheet music of what you played.
It uses lilypond for that purpose.

Creator: Eden Candelas
"""

import pygame
import os
import subprocess
from time import sleep

from button_class import Button

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1400, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Eden's Piano")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (211, 211, 211)
DARK_GRAY = (49, 49, 49)

C3 = Button("c", WHITE, 0, 0, 100, HEIGHT, "C3", pygame.K_a, 'Piano.ff.C3.mp3')
Db3 = Button("des", BLACK, 75, 0, 50, 250, "Db3", pygame.K_q, 'Piano.ff.Db3.mp3')
D3 = Button("d", WHITE, 100, 0, 100, HEIGHT, "D3", pygame.K_s, 'Piano.ff.D3.mp3')
Eb3 = Button("ees", BLACK, 175, 0, 50, 250, "Eb3", pygame.K_w, 'Piano.ff.Eb3.mp3')
E3 = Button("e", WHITE, 200, 0, 100, HEIGHT, "E3", pygame.K_d, 'Piano.ff.E3.mp3')
F3 = Button("f", WHITE, 300, 0, 100, HEIGHT, "F3", pygame.K_e, 'Piano.ff.F3.mp3')
Gb3 = Button("ges", BLACK, 375, 0, 50, 250, "Gb3", pygame.K_r, 'Piano.ff.Gb3.mp3')
G3 = Button("g", WHITE, 400, 0, 100, HEIGHT, "G3", pygame.K_f, 'Piano.ff.G3.mp3')
Ab3 = Button("aes", BLACK, 475, 0, 50, 250, "Ab3", pygame.K_t, 'Piano.ff.Ab3.mp3')
A3 = Button("a", WHITE, 500, 0, 100, HEIGHT, "A3", pygame.K_g, 'Piano.ff.A3.mp3')
Bb3 = Button("bes", BLACK, 575, 0, 50, 250, "Bb3", pygame.K_x, 'Piano.ff.Bb3.mp3')
B3 = Button("b", WHITE, 600, 0, 100, HEIGHT, "B3", pygame.K_c, 'Piano.ff.B3.mp3')
C4 = Button("c'", WHITE, 700, 0, 100, HEIGHT, "C4", pygame.K_h, 'Piano.ff.C4.mp3')
Db4 = Button("des'", BLACK, 775, 0, 50, 250, "Db4", pygame.K_y, 'Piano.ff.Db4.mp3')
D4 = Button("d'", WHITE, 800, 0, 100, HEIGHT, "D4", pygame.K_j, 'Piano.ff.D4.mp3')
Eb4 = Button("ees'", BLACK, 875, 0, 50, 250, "Eb4", pygame.K_u, 'Piano.ff.Eb4.mp3')
E4 = Button("e'", WHITE, 900, 0, 100, HEIGHT, "E4", pygame.K_k, 'Piano.ff.E4.mp3')
F4 = Button("f'", WHITE, 1000, 0, 100, HEIGHT, "F4", pygame.K_l, 'Piano.ff.F4.mp3')
Gb4 = Button("ges'", BLACK, 1075, 0, 50, 250, "Gb4", pygame.K_i, 'Piano.ff.Gb4.mp3')
G4 = Button("g'", WHITE, 1100, 0, 100, HEIGHT, "G4", pygame.K_SEMICOLON, 'Piano.ff.G4.mp3')
Ab4 = Button("aes'", BLACK, 1175, 0, 50, 250, "Ab4", pygame.K_o, 'Piano.ff.Ab4.mp3')
A4 = Button("a'", WHITE, 1200, 0, 100, HEIGHT, "A4", 39, 'Piano.ff.A4.mp3')
Bb4 = Button("bes'", BLACK, 1275, 0, 50, 250, "Bb4", pygame.K_p, 'Piano.ff.Bb4.mp3')
B4 = Button("b'", WHITE, 1300, 0, 100, HEIGHT, "B4", pygame.K_LEFTBRACKET, 'Piano.ff.B4.mp3')

keys_list = [C3, D3, Db3, E3, F3, Eb3, G3, Gb3, A3, Ab3, B3, Bb3, C4, D4, Db4, E4, F4, Eb4, G4, Gb4, A4, Ab4, B4, Bb4]

played_list = []
path = '/home/leo/Documents/PythonProjects/PygamePiano/sheet.pdf'

keybinds = {
    pygame.K_a: C3,
    pygame.K_q: Db3,
    pygame.K_s: D3,
    pygame.K_w: Eb3,
    pygame.K_d: E3,
    pygame.K_e: F3,
    pygame.K_r: Gb3,
    pygame.K_f: G3,
    pygame.K_t: Ab3,
    pygame.K_g: A3,
    pygame.K_x: Bb3,
    pygame.K_c: B3,
    pygame.K_h: C4,
    pygame.K_y: Db4,
    pygame.K_j: D4,
    pygame.K_u: Eb4,
    pygame.K_k: E4,
    pygame.K_l: F4,
    pygame.K_i: Gb4,
    pygame.K_SEMICOLON: G4,
    pygame.K_o: Ab4,
    39: A4,
    pygame.K_p: Bb4,
    pygame.K_LEFTBRACKET: B4
}

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
    if Db3.isOver(mouse_pos):
        Db3.play()
    elif C3.isOver(mouse_pos):
        C3.play()
    elif Eb3.isOver(mouse_pos):
        Eb3.play()
    elif D3.isOver(mouse_pos):
        D3.play()
    elif E3.isOver(mouse_pos):
        E3.play()
    elif Gb3.isOver(mouse_pos):
        Gb3.play()
    elif F3.isOver(mouse_pos):
        F3.play()
    elif Ab3.isOver(mouse_pos):
        Ab3.play()
    elif G3.isOver(mouse_pos):
        G3.play()
    elif Bb3.isOver(mouse_pos):
        Bb3.play()
    elif A3.isOver(mouse_pos):
        A3.play()
    elif B3.isOver(mouse_pos):
        B3.play()
    elif Db4.isOver(mouse_pos):
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
    try:
        keybinds[pressed_key].pressed()
        played_list.append(keybinds[pressed_key].name)
    except KeyError:
        pass


def handle_unpressed_key(unpressed_key):
    try:
        keybinds[unpressed_key].unpressed()
    except KeyError:
        pass

def write_sheet(notes):
    # The notes are written but they dont match the top and botton staff
    with open('sheet.ly', 'w') as sheet_file:
        sheet_file.write('\\version "2.22.2"\n')
        sheet_file.write("upper = {\n")
        sheet_file.write("\\clef treble\n")
        for note in notes:
            if note[-1] == "'":
                sheet_file.write(f" {note} ")
        sheet_file.write("\n}\nlower = {\n")
        sheet_file.write("\\clef bass")
        for note in notes:
            if note[-1] != "'":
                sheet_file.write(f" {note}")
        sheet_file.write("\n}\n\\score {\n")
        sheet_file.write("\\new PianoStaff\n")
        sheet_file.write('<<\\new Staff = "upper" \\upper\n')
        sheet_file.write('\\new Staff = "lower" \\lower>>')
        sheet_file.write("\n}")
    os.system('lilypond sheet.ly')
    subprocess.call(["xdg-open", path])
    
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
    write_sheet(played_list)

if __name__ == '__main__':
    main()
