class IngameMenu:
    def __init__(self, disp, fonts, images, buttons, animations) -> None:
        self.disp = disp
        self.fonts = fonts
        self.images = images
        self.buttons = buttons
        self.animations = animations
        self.opened = False
        self.scroll = {}
        self.scroll["rect"] = self.images["scroll_menu"].get_rect()
        self.scroll["pos"] = (self.disp["w"]*0.5-self.scroll["rect"].w*0.5, self.disp["h"]*0.5-self.scroll["rect"].h*0.5)

    def display(self):
        if self.opened:
            self.disp["disp"].blit(self.images["scroll_bg_fade"], (0, 0))
            self.disp["disp"].blit(self.images["scroll_menu"], self.scroll["pos"])
            self.buttons["scroll_resume"].display()
            self.buttons["scroll_new"].display()
            self.buttons["scroll_music"].display()
            self.buttons["scroll_sound"].display()
            self.buttons["scroll_main"].display()
            self.animations["scroll_music_toggle"].display()
            self.animations["scroll_sound_toggle"].display()
