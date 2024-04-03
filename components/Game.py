from components.Text import Text
from components.Animation import Animation


class Game:
    def __init__(self, disp) -> None:
        self.disp = disp
        self.fonts = None
        self.images = None
        self.sounds = None
        self.gallow = None
        self.gallow_pos = None
        self.pops = None
        self.tries = 10
        self.tries_buffer = -1
        self.texts = None
        self.buttons = None
        self.word = None
        self.is_victory = False
        self.is_gameover = False
        self.victory_texts = None
        self.gameover_texts = None

    def update(self, fonts: dict, images: dict, sounds: dict, texts: dict, buttons: dict):
        """This method is called after loading all the content"""
        self.fonts = fonts
        self.images = images
        self.sounds = sounds
        self.gallow = self.images["ingame_gallow"]
        self.gallow_pos = self.get_gallow_pos()
        self.pops = self.generate_pops()
        self.texts = texts
        self.buttons = buttons
        self.victory_texts = [
            Text(
                disp=self.disp,
                text='The Witch will live one more day',
                font=self.fonts["victory"],
                pos=(self.disp.w * 0.5,
                     self.disp.h * 0.45),
                fg_color=(150, 50, 50),
                centered=True
            ),
            Text(
                disp=self.disp,
                text='CONGRATULATIONS !',
                font=self.fonts["victory"],
                pos=(self.disp.w * 0.5,
                     self.disp.h * 0.3),
                fg_color=(150, 50, 50),
                centered=True
            )
        ]
        self.gameover_texts = [
            Text(
                disp=self.disp,
                text='The Witch Died',
                font=self.fonts["gameover"],
                pos=(self.disp.w * 0.5,
                     self.disp.h * 0.34),
                fg_color=(255, 0, 0),
                centered=True
            ),
            Text(
                disp=self.disp,
                text='GAME OVER',
                font=self.fonts["gameover"],
                pos=(self.disp.w * 0.5,
                     self.disp.h * 0.48),
                fg_color=(255, 0, 0),
                centered=True
            ),
        ]

    def get_gallow_pos(self) -> tuple:
        """Retrieves the gallow position"""
        pos = (self.disp.w * 0.5 - self.gallow.w * 0.5, self.disp.h * 0.45 - self.gallow.h * 0.5)
        return pos

    def generate_pops(self) -> list:
        """Generates all the pop Animation() instances with its positions"""
        pops = []
        pos = [
            (self.gallow_pos[0] + 113, self.gallow_pos[1] + 253),
            (self.gallow_pos[0] + 3, self.gallow_pos[1] + 113),
            (self.gallow_pos[0] + 113, self.gallow_pos[1] - 22),
            (self.gallow_pos[0] + 63, self.gallow_pos[1] + 32),
            (self.gallow_pos[0] + 198, self.gallow_pos[1] + 43),
            (self.gallow_pos[0] + 211, self.gallow_pos[1] + 113),
            (self.gallow_pos[0] + 189, self.gallow_pos[1] + 103),
            (self.gallow_pos[0] + 233, self.gallow_pos[1] + 103),
            (self.gallow_pos[0] + 201, self.gallow_pos[1] + 178),
            (self.gallow_pos[0] + 218, self.gallow_pos[1] + 178)
        ]
        for i in range(10):
            pops.append(Animation(disp=self.disp, image=self.images["ingame_pop"], pos=pos[i], anim_times=1, delay=2,
                                  reset_frame=False))
        return pops

    def update_tries(self) -> None:
        """Updates the shown tries Text() surface when changed"""
        self.texts["game"]["tries"] = Text(
            disp=self.disp,
            text=self.tries,
            font=self.fonts["ingame_tries"],
            pos=(self.disp.w * 0.65, self.disp.h * 0.05),
            fg_color=(150, 0, 0)
        )
        self.tries_buffer = self.tries

    def display(self) -> None:
        """Displays all the game components"""
        # Backgrounds
        self.disp.scr.blit(self.images["ingame_bg"].img, (0, 0))
        self.disp.scr.blit(self.images["ingame_gallow_bg"].img, (0, 0))

        # Pops
        for pop in self.pops:
            if pop.anim_in_progress:
                pop.display()

        # Gallow
        self.disp.scr.blit(self.gallow.img, self.gallow_pos, self.gallow.frames[10 - self.tries])

        # Word
        if self.word:
            self.word.display()

        # Sub-components
        if self.tries_buffer != self.tries:
            self.update_tries()
        for text in self.texts["game"].values():
            text.display()
        self.buttons["game"]["menu"].display()

        # Victory and Gameover
        if self.is_victory:
            self.disp.scr.blit(self.images["fade"].img, (0, 0))
            for txt in self.victory_texts:
                txt.display()
            for btn in self.buttons["game"].values():
                btn.display()
        elif self.is_gameover:
            self.disp.scr.blit(self.images["fade"].img, (0, 0))
            self.disp.scr.blit(self.images["gameover_brush"].img, (225, self.disp.h * 0.24))
            for txt in self.gameover_texts:
                txt.display()
            for btn in self.buttons["game"].values():
                btn.display()

    def victory(self) -> None:
        """Displays victory screen"""
        self.is_victory = True
        self.sounds["victory"].play()

    def gameover(self) -> None:
        """Displays game over screen"""
        self.is_gameover = True
        self.sounds["gameover"].play()

    def success_guess(self, letter_index: int) -> None:
        """Set the given letter to guessed"""
        self.word.letters[letter_index].guessed = True
        self.word.covers[letter_index].start_anim()
        self.word.scratch_snd.play()
        if all([letter.guessed for letter in self.word.letters]):
            self.victory()

    def failed_guess(self) -> None:
        """Registers a failed guess and subtracts a try from the total"""
        self.tries -= 1
        self.sounds["ingame_pop"].play()
        list(reversed(self.pops))[self.tries].start_anim()
        if self.tries <= 0:
            self.gameover()
