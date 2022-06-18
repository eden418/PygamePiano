import pygame
import os


class Button:
    def __init__(self, name, color, x, y, width, height, text='', sound_filename=''):
        self.color = color
        if color == (0,0,0):
            self.isWhite = False
            self.text_color = (255,255,255)
        else:
            self.isWhite = True
            self.text_color = (0,0,0)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.sound = pygame.mixer.Sound(os.path.join('piano notes', sound_filename))
        self.name = name

    def draw(self, win):
        if self.isWhite:
            # The way to draw an outline is to go back two in the origin
            # And add 4 (two from each side) to the width and height
            pygame.draw.rect(win, (0,0,0),
                             (self.x - 2, self.y - 2,
                              self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 40)
            text = font.render(self.text, True, self.text_color)
            # Center the text by starting in x adding, half the width
            # of the button minus half the width of the text
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                                    self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False

    def play(self):
        self.sound.play()

    def stop(self):
        self.sound.stop()

    def pressed(self):
        self.sound.play()
        if self.isWhite:
            self.color = (211, 211, 211)
        elif not self.isWhite:
            self.color = (49, 49, 49)

    def unpressed(self):
        self.sound.stop()
        if self.isWhite:
            self.color = (250, 250, 250)
        elif not self.isWhite:
            self.color = (0, 0, 0)
