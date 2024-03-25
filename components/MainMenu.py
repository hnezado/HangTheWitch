

class MainMenu:
    def __init__(self, disp) -> None:
        self.disp = disp
        self.images = None
        self.buttons = None

    def update(self, images, buttons):
        self.images = images
        self.buttons = buttons

    def display(self):
        self.disp.scr.blit(self.images["menu_bg"].img, (0, 0))
        
        # Buttons
        self.buttons["main"]["play"].display()
        self.buttons["main"]["quit"].display()
        

