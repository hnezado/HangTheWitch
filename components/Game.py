from components.Text import Text
from components.Word import Word


class Game:
	def __init__(self, disp, word_config_presets) -> None:
		self.disp = disp
		self.images = None
		self.fonts = None
		self.gallow = None
		self.gallow_pos = None
		self.scratch = None
		self.tries = 5
		self.tries_buffer = -1
		self.word_config_presets = word_config_presets
		self.texts = None
		self.buttons = None
		self.word = ""
		self.letters_properties = []
		self.letters_texts = []

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
		for letter_text in self.letters_texts:
			letter_text.display()

		# Covers (anim)
		for letter_props in self.letters_properties:
			if not letter_props["guessed"]:
				scratch_pos = [letter_props["pos"][0]-self.word_config_presets["letter"]["dim"]["w"]*0.5, letter_props["pos"][1]-self.word_config_presets["letter"]["dim"]["h"]*0.5]
				self.disp.scr.blit(self.scratch.img, scratch_pos, self.scratch.frames[11])

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
		w = Word(dif)
		self.word = w.generate_word()
		self.letters_properties = w.parse_word(disp=self.disp, word=self.word, word_config_presets=self.word_config_presets
		)
		self.letters_texts = w.generate_letter_texts_objs(disp=self.disp, letters_properties=self.letters_properties)
		print("word:", self.word)
