class Intro:
    def __init__(self, disp):
        self.disp = disp
        self.bg = None
        self.space = None
        self.fixed_img_counter = 0

    def update(self, images, animations):
        self.bg = images["menu_bg"]
        self.space = animations["intro"]["space"]
        self.space.start_anim()

    def change_anim_mode(self):
        if self.space.frame <= 0:
            self.fixed_img_counter += 1
            if self.fixed_img_counter >= 20:
                self.space.start_anim(mode="ascend")
                self.fixed_img_counter = 0

        else:
            self.space.start_anim(mode="descend")

    def display(self):
        """Displays the intro animation"""
        self.disp.scr.blit(self.bg.img, (0, 0))
        self.space.display()
        if not self.space.anim_in_progress:
            self.change_anim_mode()
