from components.Text import Text
from components.Button import Button


class Dif:
    def __init__(self, disp, dif_btn_dim=(30, 40), gap=60):
        self.disp = disp
        self.fonts = None
        self.images = None
        self.pos_scroll = None
        self.btn_menu = None
        self.text = None
        self.dif_btn_dim = dif_btn_dim
        self.gap = gap
        self.dif_btns = None

    def update(self, fonts: dict, images: dict, buttons: dict) -> None:
        """Updates main attributes (called after components loading)"""
        self.fonts = fonts
        self.images = images
        self.pos_scroll = (
            self.disp.w * 0.5 - self.images["dif_scroll"].w * 0.5,
            self.disp.h * 0.5 - self.images["dif_scroll"].h * 0.5
        )
        self.btn_menu = buttons["game"]["menu"]
        self.text = Text(
            disp=self.disp,
            text='Choose difficulty',
            font=self.fonts["dif_txt"]
        )
        self.text.pos = (self.disp.w * 0.5 - self.text.w * 0.5,
                         self.disp.h * 0.35 - self.text.h * 0.5)
        self.dif_btns = self.generate_dif_btns()
    
    def generate_dif_btns(self) -> list:
        """Generates the difficulty menu buttons (10 Button() instances)"""
        btns = []
        w = self.dif_btn_dim[0]
        init_x = self.disp.w * 0.5 - (w * 5 + self.gap * 4) * 0.5 + 20
        for i in range(10):
            y = self.disp.h * 0.65 if i // 5 else self.disp.h * 0.5
            pos = (init_x + (w + self.gap) * (i % 5), y)
            btns.append(Button(
                disp=self.disp,
                dim=(self.dif_btn_dim[0], self.dif_btn_dim[1]),
                pos=pos,
                text=str(i+1),
                font=self.fonts["dif_btn"]
            ))
        return btns
    
    def display(self) -> None:
        """Displays all the difficulty menu components"""
        self.disp.scr.blit(self.images["ingame_bg"].img, (0, 0))
        self.disp.scr.blit(self.images["dif_scroll"].img, self.pos_scroll)
        self.text.display()

        # Buttons
        self.btn_menu.display()
        for btn in self.dif_btns:
            btn.display()
