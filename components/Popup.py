import pygame as pg
from components.Text import Text
from components.Button import Button


class Popup:
    def __init__(self, disp, text, padding=10, type="verify") -> None:
        self.disp = disp
        self.text = text
        self.padding = padding
        self.type = type
        self.fonts = None
        self.images = None
        self.text_surface = None
        self.buttons = None
        self.fade = None
        self.question = None
        self.font_txt = None
        self.font_btn = None
        self.rect_outer = pg.Rect(self.disp.w * 0.5 - 110, self.disp.h * 0.5 - 50, 220, 100)
        self.rect_inner = pg.Rect(self.disp.w * 0.5 - 105, self.disp.h * 0.5 - 45, 210, 90)
        self.sound_btn_click = None
        self.accept_btn = None
        self.cancel_btn = None
        self.opened = False

    def update(self, fonts, images, sound_btn_click, buttons):
        """This method is called after loading all the content"""
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
        self.font_txt = self.fonts ["popup_txt"]
        self.font_btn = self.fonts["popup_btn"]
        self.sound_btn_click = sound_btn_click
        
        if self.type == "verify":
            self.accept_btn = Button(self.disp, (80, 30), (0, 0), 'Accept', self.fonts["popup_btn"])
            self.accept_btn.pos = (
                self.rect_inner.x + self.padding + self.accept_btn.inact_rect.w * 0.5,
                self.rect_inner.y + self.rect_inner.h - self.padding - self.accept_btn.inact_rect.h * 0.5
            )
            self.cancel_btn = Button(self.disp, (80, 30), (0, 0), 'Cancel', self.fonts["popup_btn"])
            self.cancel_btn.fn=self.close
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
        if self.opened:
            self.sound_btn_click.play()
            self.opened = False

    def display(self):
        if self.opened:
            self.disp.scr.blit(self.fade.img, (0, 0))
            pg.draw.rect(self.disp.scr, (130, 96, 94), self.rect_outer)
            pg.draw.rect(self.disp.scr, (192, 138, 117), self.rect_inner)
            self.text_surface.display()
            self.disp.scr.blit(self.question.img, (self.rect_outer.x + 180, self.rect_outer.y + 10))
            self.accept_btn.display()
            if self.type == "verify":
                self.cancel_btn.display()

            # for btn in self.buttons["popup"].values():
            #     btn.display()
            
            # self.windows_rects["outer"] = pg.draw.rect(self.disp.scr, (130, 96, 94), (self.disp.w * 0.5 - w * 0.5, self.disp.h * 0.5 - 50, 220, 100)) # adaptar tamaño window al texto
            # # Inner Window Rect
            # self.windows_rects["inner"] = None
            
            # pg.draw.rect(self.disp.scr, (130, 96, 94), (self.disp.w * 0.5 - 110, self.disp.h * 0.5 - 50, 220, 100)) # adaptar tamaño window al texto
            # pg.draw.rect(self.disp.scr, (192, 138, 117), (self.disp.w * 0.5 - 105, self.disp.h * 0.5 - 45, 210, 90)) # aquí lo mismo que arriba

            # Displaying self made question_mark due to the lack of it in the font
            # self.disp.scr.blit(self.images["question"], (self.disp.w * 0.59, self.disp.h * 0.44))
            
            # but_verify_yes_main.drawing()
            # but_verify_no.drawing()
