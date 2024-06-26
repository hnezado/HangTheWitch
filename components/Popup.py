import pygame as pg
from components.Text import Text
from components.Button import Button


class Popup:
    def __init__(self, disp, text, padding=10, type="verify", is_question=True, question_mod_pos=(0, 0)) -> None:
        self.disp = disp
        self.text = text
        self.padding = padding
        self.type = type
        self.fonts = None
        self.images = None
        self.text_surface = None
        self.buttons = None
        self.fade = None
        self.is_question = is_question
        self.question = None
        self.question_pos = None
        self.question_mod_pos = question_mod_pos
        self.font_txt = None
        self.font_btn = None
        self.rect_outer = pg.Rect(self.disp.w * 0.5 - 110, self.disp.h * 0.5 - 50, 220, 100)
        self.rect_inner = pg.Rect(self.disp.w * 0.5 - 105, self.disp.h * 0.5 - 45, 210, 90)
        self.sound_btn_click = None
        self.accept_btn = None
        self.cancel_btn = None
        self.opened = False

    def update(self, fonts, images, sound_btn_click, buttons):
        """This method is called after loading all the content (media and components)"""
        self.fonts = fonts
        self.images = images
        self.text_surface = Text(
            disp=self.disp,
            text=self.text,
            font=self.fonts["popup_txt"],
            pos=(self.rect_outer.x + self.rect_outer.w * 0.5, self.rect_outer.y + self.rect_outer.h * 0.2),
            centered=True
        )
        self.buttons = buttons
        self.fade = self.images["fade"]
        self.question = self.images["question"]
        self.question_pos = (
            self.rect_inner.x + self.rect_inner.w - 12 + self.question_mod_pos[0],
            self.rect_inner.y + self.question_mod_pos[1]
        )
        self.font_txt = self.fonts["popup_txt"]
        self.font_btn = self.fonts["popup_btn"]
        self.sound_btn_click = sound_btn_click
        
        if self.type == "verify":
            self.accept_btn = Button(self.disp, (80, 30), (0, 0), 'Accept', self.fonts["popup_btn"])
            self.accept_btn.pos = (
                self.rect_inner.x + self.padding + self.accept_btn.inact_rect.w * 0.5,
                self.rect_inner.y + self.rect_inner.h - self.padding - self.accept_btn.inact_rect.h * 0.5
            )
            self.cancel_btn = Button(self.disp, (80, 30), (0, 0), 'Cancel', self.fonts["popup_btn"])
            self.cancel_btn.pos = (
                self.rect_inner.x + self.rect_inner.w - self.padding - self.cancel_btn.inact_rect.w * 0.5,
                self.rect_inner.y + self.rect_inner.h - self.padding - self.cancel_btn.inact_rect.h * 0.5
            )
        else:
            self.accept_btn = Button(self.disp, (80, 30), (0, 0), 'Accept', self.fonts["popup_btn"])
            self.accept_btn.pos = (
                self.rect_inner.x + self.rect_inner.w * 0.5,
                self.rect_inner.y + self.rect_inner.h * 0.7
            )

    def close(self):
        """Closes the popup"""
        if self.opened:
            self.opened = False

    def display(self):
        """Displays all the popup components"""
        if self.opened:
            self.disp.scr.blit(self.fade.img, (0, 0))
            pg.draw.rect(self.disp.scr, (130, 96, 94), self.rect_outer)
            pg.draw.rect(self.disp.scr, (192, 138, 117), self.rect_inner)
            self.text_surface.display()
            if self.is_question:
                self.disp.scr.blit(self.question.img, self.question_pos)
            self.accept_btn.display()
            if self.type == "verify":
                self.cancel_btn.display()
