import pygame


class Button:
    def __init__(self, color, x, y, width, height, text='', text_color=(0,0,0)):
        self.color = color
        if color == (0,0,0):
            self.isWhite = False
        else:
            self.isWhite = True
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_color = text_color


    def draw(self, win, outline=None):
        if outline:
            # The way to draw an outline is to go back two in the origin
            # And add 4 (two from each side) to the width and height
            pygame.draw.rect(win, outline,
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
