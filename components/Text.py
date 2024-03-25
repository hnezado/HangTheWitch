import pygame as pg

class Text:
    def __init__(self, disp, text, font=None, pos=(0, 0), fg_color=(20, 20, 20), centered=False) -> None:
        self.disp = disp
        self.text = str(text)
        self.font = pg.font.Font(font, 45) if not font else font
        self.pos = pos
        self.fg_color = fg_color
        self.surface = self.get_surface()
        self.rect = self.surface.get_rect()
        self.w, self.h = self.rect.w, self.rect.h
        self.centered = centered
        self.updated = False

    def get_surface(self) -> object:
        '''Generates the text using the specified font and color'''
        txt_surf = self.font.render(self.text, True, self.fg_color)
        return txt_surf

    def get_rect_centered(self):
        self.rect = self.surface.get_rect(center=self.pos)

    def update(self):
        self.updated = True
        if self.centered:
            self.rect.center = self.pos

    def display(self) -> None:
        '''Displays the text surface on the specified position'''
        if not self.updated:
            self.update()
        if self.centered:
            self.disp.scr.blit(self.surface, self.rect)
        else:
            self.disp.scr.blit(self.surface, self.pos)
