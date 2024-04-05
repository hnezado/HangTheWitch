

class MainMenu:
    def __init__(self, disp) -> None:
        self.disp = disp
        self.images = None
        self.title = None
        self.title_pos = None
        self.title_final_y = self.disp.h * 0.1
        self.buttons = None
        self.anim_in_progress = True

    def update(self, images: dict, buttons: dict, texts:dict) -> None:
        """This method is called after loading all the content (media and components)"""
        self.images = images
        self.title = texts["main"]["title"]
        self.buttons = buttons
        self.reset_anim()

    def reset_anim(self) -> None:
        """Resets the falling title animation"""
        self.anim_in_progress = True
        self.title_pos = [self.disp.w * 0.5, - self.title.h]

    def display(self) -> None:
        """Displays all the Main Menu components"""
        self.disp.scr.blit(self.images["menu_bg"].img, (0, 0))
        if self.anim_in_progress:
            self.anim_title()
        else:
            self.buttons["main"]["play"].display()
            self.buttons["main"]["quit"].display()
        self.title.display()

    def anim_title(self) -> None:
        """Updates the title falling animation"""
        if self.title_pos[1] < self.title_final_y:
            self.title_pos[1] += 3
        else:
            self.anim_in_progress = False
        self.title.pos = self.title_pos
        self.title.update()
