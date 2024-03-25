from components.Text import Text
from components.Button import Button

class Dif:
    def __init__(self, disp, dif_btn_dim=(30, 40), gap=60):
        self.disp = disp
        self.fonts = None
        self.img_scroll = None
        self.pos_scroll = None
        self.btn_menu = None
        self.dif_btn_dim = dif_btn_dim
        self.gap = gap
        self.dif_btns = None

    def update(self, fonts, images, buttons):
        self.fonts = fonts
        self.images = images
        self.pos_scroll = (
            self.disp.w * 0.5 - images["dif_scroll"].w * 0.5,
            self.disp.h * 0.5 - images["dif_scroll"].h * 0.5
        )
        self.btn_menu = buttons["game"]["menu"]
        self.txt_choose = Text(
            disp=self.disp,
            text='Choose difficulty',
            font=self.fonts["dif_txt"]
        )
        self.txt_choose.pos = (self.disp.w * 0.5 - self.txt_choose.w * 0.5,
                 self.disp.h * 0.35 - self.txt_choose.h * 0.5)
        self.dif_btns = self.generate_dif_btns()
    
    def generate_dif_btns(self):
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
    
    def display(self):
        self.disp.scr.blit(self.images["ingame_bg"].img, (0, 0))
        self.disp.scr.blit(self.images["dif_scroll"].img, self.pos_scroll)
        self.txt_choose.display()

        # Buttons
        self.btn_menu.display()
        for btn in self.dif_btns:
            btn.display()


# 	def diff_blit(self):
# 		'''It blits the difficulty buttons on the dif choice menu'''
# 		bg_surface_rect = self.bg_surface.get_rect()
# 		self.surface.blit(self.bg_surface, (self.disp_w*0.5-bg_surface_rect.width*0.5, self.disp_h*0.5-bg_surface_rect.height*0.5))
# 		text_object(self.surface, 'Choose difficulty', txt_font=vars_2.font_dif_txt, pos=(self.disp_w*0.5, self.disp_h*0.32))

# 		for button in range(int(self.num_buttons*0.5)):
# 			b_dif = Button(self.surface, self.but_width, self.but_height, ((self.disp_w*0.5-(self.but_width+self.margin)
# 							*(self.num_buttons*0.25))+(self.but_width+self.margin)*0.5)+(self.but_width+self.margin)*button,
# 							bg_surface_rect.height*0.65, (130, 96, 94), (179, 104, 100), str(button+1), vars_2.font_dif_but,
# 							text_centered=(((self.disp_w*0.5-(self.but_width+self.margin)*(self.num_buttons*0.25))+
# 							(self.but_width+self.margin)*0.5)+(self.but_width+self.margin)*button,
# 							bg_surface_rect.height*0.65+self.but_height*0.5+4))
# 			b_dif.drawing()
# 			if len(vars_2.dif_but_list) < self.num_buttons:
# 				vars_2.dif_but_list.append(b_dif)
# 		for button in range(int(self.num_buttons*0.5), self.num_buttons):
# 			b_dif = Button(self.surface, self.but_width, self.but_height, ((self.disp_w*0.5-(self.but_width+self.margin)
# 							*(self.num_buttons*0.25))+(self.but_width+self.margin)*0.5)+(self.but_width+self.margin)*
# 							(button-self.num_buttons*0.5), bg_surface_rect.height*0.85, (130, 96, 94), (179, 104, 100),
# 							str(button+1), vars_2.font_dif_but,
# 							text_centered=(((self.disp_w*0.5-(self.but_width+self.margin)*(self.num_buttons*0.25))+
# 							(self.but_width+self.margin)*0.5)+(self.but_width+self.margin)*(button-self.num_buttons*0.5),
# 							bg_surface_rect.height*0.85+self.but_height*0.5+4))
# 			b_dif.drawing()
# 			if len(vars_2.dif_but_list) < self.num_buttons:
# 				vars_2.dif_but_list.append(b_dif)
