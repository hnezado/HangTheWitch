from components.Text import Text

class Components:
    def __init__(self) -> None:
        self.texts = {
            "main": {},
            "dif": {},
            "game": {},
            "inmenu": {},
            "popup": {}
        }
        self.animations = {
            "main": {},
            "dif": {},
            "game": {},
            "inmenu": {}
        }
        self.buttons = {
            "main": {},
            "dif": {},
            "game": {},
            "inmenu": {},
            "popup": {}
        }

    def add_text(self, disp, name, text, font=None, pos=(0, 0), fg_color=(0, 0, 0)):
        self.texts[name] = Text(disp=disp, text=text, font=font, pos=pos, fg_color=fg_color)
