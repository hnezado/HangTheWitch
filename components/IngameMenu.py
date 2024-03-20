class IngameMenu:
    def __init__(self, disp) -> None:
        self.disp = disp
        self.images = None
        self.texts = None
        self.animations = None
        self.buttons = None
        self.opened = False
        self.fade = None
        self.scroll = None
        self.scroll_pos = None

    def update(self, images, texts, animations, buttons):
        """This method is called after loading all the content"""
        self.images = images
        self.texts = texts
        self.animations = animations
        self.buttons = buttons
        self.fade = self.images["fade"]
        self.scroll = self.images["inmenu_scroll"]
        self.scroll_pos = (self.disp.w * 0.5 - self.scroll.w * 0.5, self.disp.h * 0.5 - self.scroll.h * 0.5)

    def display(self):
        if self.opened:
            self.disp.scr.blit(self.fade.img, (0, 0))
            self.disp.scr.blit(self.scroll.img, self.scroll_pos)
            self.buttons["inmenu"]["resume"].display()
            self.buttons["inmenu"]["new"].display()
            self.buttons["inmenu"]["music"].display()
            self.buttons["inmenu"]["sound"].display()
            self.buttons["inmenu"]["main"].display()
            self.animations["inmenu_toggle_music"].display()
            self.animations["inmenu_toggle_sound"].display()
