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
        self.scroll_sound = None

    def update(self, images: dict, sounds: dict, texts: dict, animations: dict, buttons: dict) -> None:
        """This method is called after loading all the content (media and components)"""
        self.images = images
        self.texts = texts
        self.animations = animations
        self.buttons = buttons
        self.fade = self.images["fade"]
        self.scroll = self.images["inmenu_scroll"]
        self.scroll_pos = (self.disp.w * 0.5 - self.scroll.w * 0.5, self.disp.h * 0.5 - self.scroll.h * 0.5)
        self.scroll_sound = sounds["scroll"]

    def display(self) -> None:
        """Displays all the Ingame Menu components"""
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

    def open(self) -> None:
        """Opens the Ingame Menu"""
        self.scroll_sound.play()
        self.opened = True

    def close(self) -> None:
        """Closes the Ingame Menu"""
        self.scroll_sound.play()
        self.opened = False
