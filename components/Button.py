import pygame as pg
from typing import Any, Callable
from pygame import Surface, Rect, draw, SRCALPHA, mouse
from components.Text import Text


class Button:
    def __init__(self, disp, dim, pos, text, font,
                 i_color=(130, 96, 94),
                 a_color=(179, 104, 100),
                 enabled=True,
                 i_font_color=(20, 20, 20),
                 a_font_color=(200, 50, 50),
                 act_margin=6,
                 btn_transp=False,
                 txt_pos_mod=None,
                 fn=lambda: None):
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
        self.txt_pos_mod = txt_pos_mod
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
        self.fn_buffer = None
        self.fn = fn
        print(f"init Button() fn: {self.fn} - fn_buffer: {self.fn_buffer}")

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)
        if name == "pos":
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
        elif name == "fn":
            print(f"Setting {self.text} fn: {value} - fn_buffer: {self.fn_buffer}")
            # print("Setting accept_btn: name:", name, "and value:", value.__name__)
            self.fn_buffer = value
            super().__setattr__(name, self.check_enabled)
            print(f"All fn set -> fn: {self.fn}, fn_buffer: {self.fn_buffer}")

    def check_enabled(self, *args, **kwargs) -> Callable:
        if self.enabled:
            return self.fn_buffer(*args, **kwargs)
        else:
            return lambda: None

    def generate_text_surfaces(self) -> dict:
        """Generates the surfaces for the button text"""
        text_surfaces = {}
        text_pos = (
                self.inact_rect.x + self.inact_rect.w * 0.5,
                self.inact_rect.y + self.inact_rect.h * 0.5 - 3
            )
        if self.txt_pos_mod:
            text_pos = (
                text_pos[0] + self.txt_pos_mod[0],
                text_pos[1] + self.txt_pos_mod[1]
            )
            
        text_surfaces["inact"] = Text(
            disp=self.disp,
            text=self.text,
            font=self.font,
            pos=text_pos,
            fg_color=self.i_font_color,
            centered=True
        )
        text_surfaces["act"] = Text(
            disp=self.disp,
            text=self.text,
            font=self.font,
            pos=text_pos,
            fg_color=self.a_font_color,
            centered=True
        )
        text_surfaces["disabled"] = Text(
            disp=self.disp,
            text=self.text,
            font=self.font,
            pos=text_pos,
            fg_color=(80, 80, 80),
            centered=True
        )
        return text_surfaces

    def display(self) -> None:
        """Displays the button and its text"""
        if self.enabled:
            if self.btn_transp:
                self.disp.scr.blit(self.transp_surf, self.pos)
                # draw.rect(self.disp.scr, self.i_color, self.inact_rect)
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
