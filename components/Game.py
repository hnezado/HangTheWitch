from components.Text import Text
from components.Word import Word


class Game:
	def __init__(self, disp, letter_conf) -> None:
		self.disp = disp
		self.images = None
		self.fonts = None
		self.gallow = None
		self.gallow_pos = None
		self.scratch = None
		self.tries = 10
		self.tries_buffer = -1
		self.letter_conf = letter_conf
		self.texts = None
		self.buttons = None
		self.word = None

	def update(self, images, fonts, texts, buttons):
		"""This method is called after loading all the content"""
		self.images = images
		self.fonts = fonts
		self.gallow = self.images["ingame_gallow"]
		self.gallow_pos = self.get_gallow_pos()
		self.scratch = images["ingame_scratch"]
		self.texts = texts
		self.buttons = buttons

	def get_gallow_pos(self) -> tuple:
		pos = (self.disp.w*0.5-self.gallow.w*0.5, self.disp.h*0.45-self.gallow.h*0.5)
		return pos

	def display(self):
		# Backgrounds
		self.disp.scr.blit(self.images["ingame_bg"].img, (0, 0))
		self.disp.scr.blit(self.images["ingame_gallow_bg"].img, (0, 0))

		# Gallow
		self.disp.scr.blit(self.gallow.img, self.gallow_pos, self.gallow.frames[10-self.tries])

		# Word
		if self.word:
			self.word.display()

			# Covers (anim)
			for letter in self.word.letters:
				if not letter.guessed:
					cover_pos = letter.text_surf.pos
					self.scratch.img.get_rect(center=cover_pos)
					self.disp.scr.blit(self.scratch.img, cover_pos, self.scratch.frames[11])

        # Sub-components
		if self.tries_buffer != self.tries:
			self.update_tries()
		for text in self.texts["game"].values():
			text.display()
		self.buttons["game"]["menu"].display()

	def update_tries(self):
		self.texts["game"]["tries"] = Text(
      		disp=self.disp,
        	text=self.tries,
			font=self.fonts["ingame_tries"],
			pos=(self.disp.w * 0.65, self.disp.h * 0.05),
			fg_color=(150, 0, 0)
      	)
		self.tries_buffer = self.tries

	def new_game(self, dif):
		self.word = Word(disp=self.disp, letter_conf=self.letter_conf, difficulty=dif)
		print("word:", self.word.word)
