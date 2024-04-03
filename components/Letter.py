from components.Text import Text


class Letter:
    def __init__(self, disp: object, txt: str) -> None:
        self.disp = disp
        self.txt = txt
        self.guessed = False
        self.text_surf = Text(disp=self.disp, text=self.txt, centered=True)
