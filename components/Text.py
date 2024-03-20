import pygame as pg

class Text:
    def __init__(self, disp, text, font=None, pos=(0, 0), fg_color=(0, 0, 0)) -> None:
        self.disp = disp
        self.text = str(text)
        self.font = pg.font.Font(font, 45) if not font else font
        self.pos = pos
        self.fg_color = fg_color
        self.text_surface = self.get_text_surface()
        self.rect = self.text_surface.get_rect()
        self.w, self.h = self.rect.w, self.rect.h

    def display(self) -> None:
        '''Displays the text surface on the specified position'''
        self.disp.scr.blit(self.text_surface, self.pos)

    def get_text_surface(self) -> object:
        '''Generates the text using the specified font and color'''
        txt_surf = self.font.render(self.text, True, self.fg_color)
        return txt_surf
