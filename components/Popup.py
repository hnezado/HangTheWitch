import pygame as pg

class Popup:
    def __init__(self, font_txt=None, font_btn=None, padding=10, type="verify") -> None:
        self.fonts = None
        self.images = None
        self.texts = None
        self.w, self.h = self.get_win_dim()
        self.font_txt = font_txt
        self.font_btn = self.media.fonts["popup_btn"] if not font_btn else font_btn
        self.padding = padding
        self.windows_rects = {}
        self.opened = False

    def update(self, fonts, images, texts, buttons):
        """This method is called after loading all the content"""
        self.fonts = fonts
        self.images = images
        self.texts = texts
        self.buttons = buttons
        self.fade = self.images["fade"]

    def display(self):
        if self.opened:
            
            # self.windows_rects["outer"] = pg.draw.rect(self.disp.scr, (130, 96, 94), (self.disp.w * 0.5 - w * 0.5, self.disp.h * 0.5 - 50, 220, 100)) # adaptar tamaño window al texto
            # # Inner Window Rect
            # self.windows_rects["inner"] = None
            
            # pg.draw.rect(self.disp.scr, (130, 96, 94), (self.disp.w * 0.5 - 110, self.disp.h * 0.5 - 50, 220, 100)) # adaptar tamaño window al texto
            # pg.draw.rect(self.disp.scr, (192, 138, 117), (self.disp.w * 0.5 - 105, self.disp.h * 0.5 - 45, 210, 90)) # aquí lo mismo que arriba

            # Displaying self made question_mark due to the lack of it in the font
            self.disp.scr.blit(self.images["question"], (self.disp.w * 0.59, self.disp.h * 0.44))
            
            # but_verify_yes_main.drawing()
            # but_verify_no.drawing()

    def get_win_dim(self):
        text_w, text_h = self.texts["popup"]["txt"].w, self.texts["popup"]["txt"].h
        btn_h = self.buttons["popup"]["accept"].height
        win_w = text_w + self.padding * 2
        win_h = text_h + btn_h + self.padding * 3
        return win_w, win_h
