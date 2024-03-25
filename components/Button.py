import pygame as pg
from typing import Any
from pygame import Surface, Rect, draw, SRCALPHA, mouse
from components.Text import Text

class Button:
    def __init__(self, disp, dim, pos, text, font,
                 i_color=(130, 96, 94), a_color=(179, 104, 100), enabled=True, i_font_color=(0, 0, 0), a_font_color=(255, 0, 0), act_margin=6, btn_transp=False, text_centered=None, fn=lambda: None):
        self.disp = disp
        self.w, self.h = dim
        self.text = text
        self.font = font
        self.i_color = i_color
        self.a_color = a_color
        self.enabled = enabled
        self.i_font_color = i_font_color
        self.a_font_color = a_font_color
        self.act_margin = act_margin
        self.btn_transp = btn_transp
        self.text_centered = text_centered
        self.transp_surf = Surface((self.w, self.h), SRCALPHA)
        self.transp_surf.fill((255, 255, 255, 0))
        
        self.pos = pos
        self.inact_rect = pg.Rect(
            self.pos[0] - self.w * 0.5,
            self.pos[1] - self.h * 0.5,
            self.w,
            self.h
        )
        self.act_rect = pg.Rect(
            self.inact_rect.x + self.act_margin,
            self.inact_rect.y + self.act_margin,
            self.inact_rect.w - self.act_margin * 2,
            self.inact_rect.h - self.act_margin * 2
        )
        self.text_surfaces = self.generate_text_surfaces()
        self.fn = fn
        self.fn_buffer = None

    def __setattr__(self, __name: str, __value: Any) -> None:
        super().__setattr__(__name, __value)
        if __name == "pos":
            self.inact_rect = pg.Rect(
                self.pos[0] - self.w * 0.5,
                self.pos[1] - self.h * 0.5,
                self.w,
                self.h
            )
            self.act_rect = pg.Rect(
                self.inact_rect.x + self.act_margin,
                self.inact_rect.y + self.act_margin,
                self.inact_rect.w - self.act_margin * 2,
                self.inact_rect.h - self.act_margin * 2
            )
            self.text_surfaces = self.generate_text_surfaces()
        elif __name == "fn":
            self.fn_buffer = __value
            super().__setattr__(__name, self.check_enabled)

    def check_enabled(self):
        if self.enabled:
            return self.fn_buffer
        else:
            return lambda: None

    def generate_text_surfaces(self):
        text_surfaces = {}
        if self.text_centered:
            text_pos = self.text_centered
        else:
            text_pos = (
                self.inact_rect.x + self.inact_rect.w * 0.5,
                self.inact_rect.y + self.inact_rect.h * 0.5 - 3
            )
        text_surfaces["inact"] = Text(disp=self.disp, text=self.text, font=self.font, pos=text_pos, fg_color=self.i_font_color, centered=True)
        text_surfaces["act"] = Text(disp=self.disp, text=self.text, font=self.font, pos=text_pos, fg_color=self.a_font_color, centered=True)
        text_surfaces["disabled"] = Text(disp=self.disp, text=self.text, font=self.font, pos=text_pos, fg_color=(80, 80, 80), centered=True)
        return text_surfaces

    # TODO Esto hay que cambiarlo, por probablemente objetos Text()
    def text_object_old(self, txt, txt_font, fg_color, x, y):
        '''It renders the font with a text, text font, and text color centering it on the button by default'''

        text_surface = txt_font.render(txt, True, fg_color)# = Text().surface
        if not self.text_centered:
            return text_surface, text_surface.get_rect(center=(x + (self.w * 0.5), y + (self.h * 0.5) - 3))
        else:
            return text_surface, text_surface.get_rect(center=self.text_centered)

    def display(self):
        '''It draws the button with the text (text itself, text font and text color), button size and position given in the arguments'''

        if self.enabled:
            if self.btn_transp:
                self.disp.scr.blit(self.transp_surf, self.pos)
                if Rect(self.inact_rect).collidepoint(mouse.get_pos()):
                    self.text_surfaces["act"].display()
                else:
                    self.text_surfaces["inact"].display()
            else:
                draw.rect(self.disp.scr, self.i_color, self.inact_rect)
                if Rect(self.inact_rect).collidepoint(mouse.get_pos()):
                    draw.rect(self.disp.scr, self.a_color, self.act_rect)
                    self.text_surfaces["act"].display()
                else:
                    self.text_surfaces["inact"].display()
        else:
            draw.rect(self.disp.scr, (150, 150, 150), self.inact_rect)
            self.text_surfaces["disabled"].display()
