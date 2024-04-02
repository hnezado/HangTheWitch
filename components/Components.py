from components.Text import Text


class Components:
    def __init__(self) -> None:
        self.texts = {
            "main": {},
            "game": {},
            "popup": {}
        }
        self.animations = {
            "intro": {},
            "main": {},
            "game": {},
            "inmenu": {}
        }
        self.buttons = {
            "main": {},
            "game": {},
            "inmenu": {},
            "popup": {}
        }

    # TODO check if this class/method is necessary
    def add_text(self, disp: object, name: str, text: str,
                 font=None, pos=(0, 0), fg_color=(0, 0, 0)) -> None:
        """Adds a new Text object"""
        self.texts[name] = Text(
            disp=disp,
            text=text,
            font=font,
            pos=pos,
            fg_color=fg_color
        )
