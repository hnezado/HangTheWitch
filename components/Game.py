import pygame as pg
from components.Text import Text
from components.Word import Word
from components.Animation import Animation


class Game:
	def __init__(self, disp, letter_conf) -> None:
		self.disp = disp
		self.fonts = None
		self.images = None
		self.sounds = None
		self.gallow = None
		self.gallow_pos = None
		self.pop = None
		self.tries = 10
		self.tries_buffer = -1
		self.letter_conf = letter_conf
		self.texts = None
		self.buttons = None
		self.word = None

	def update(self, fonts, images, sounds, texts, buttons):
		"""This method is called after loading all the content"""
		self.fonts = fonts
		self.images = images
		self.sounds = sounds
		self.gallow = self.images["ingame_gallow"]
		self.gallow_pos = self.get_gallow_pos()
		self.pops = self.generate_pops()
		self.texts = texts
		self.buttons = buttons

	def get_gallow_pos(self) -> tuple:
		pos = (self.disp.w*0.5-self.gallow.w*0.5, self.disp.h*0.45-self.gallow.h*0.5)
		return pos

	def generate_pops(self):
		pops = []
		pos = [ # -37
			(self.gallow_pos[0]+113, self.gallow_pos[1]+253),
			(self.gallow_pos[0]+3, self.gallow_pos[1]+113),
			(self.gallow_pos[0]+113, self.gallow_pos[1]-22),
			(self.gallow_pos[0]+63, self.gallow_pos[1]+32),
			(self.gallow_pos[0]+198, self.gallow_pos[1]+43),
			(self.gallow_pos[0]+211, self.gallow_pos[1]+113),
			(self.gallow_pos[0]+189, self.gallow_pos[1]+103),
			(self.gallow_pos[0]+233, self.gallow_pos[1]+103),
			(self.gallow_pos[0]+201, self.gallow_pos[1]+178),
			(self.gallow_pos[0]+218, self.gallow_pos[1]+178)
		]
		for i in range(10):
			pops.append(Animation(disp=self.disp, image=self.images["ingame_pop"], pos=pos[i], anim_times=1, delay=2, reset_frame=False))
		return pops

	def get_pop_pos(self):
		pos = (self.gallow_pos[0], self.gallow_pos[1])
		return pos

	def update_tries(self):
		self.texts["game"]["tries"] = Text(
      		disp=self.disp,
        	text=self.tries,
			font=self.fonts["ingame_tries"],
			pos=(self.disp.w * 0.65, self.disp.h * 0.05),
			fg_color=(150, 0, 0)
      	)
		self.tries_buffer = self.tries

	def display(self):
		# Backgrounds
		self.disp.scr.blit(self.images["ingame_bg"].img, (0, 0))
		self.disp.scr.blit(self.images["ingame_gallow_bg"].img, (0, 0))

		# Pops
		for pop in self.pops:
			if pop.anim_in_progress:
				pop.display()

		# Gallow
		self.disp.scr.blit(self.gallow.img, self.gallow_pos, self.gallow.frames[10-self.tries])

		# Word
		if self.word:
			self.word.display()

        # Sub-components
		if self.tries_buffer != self.tries:
			self.update_tries()
		for text in self.texts["game"].values():
			text.display()
		self.buttons["game"]["menu"].display()

	def new_game(self, dif):
		self.word = Word(disp=self.disp, scratch=self.images["ingame_scratch"], letter_conf=self.letter_conf, difficulty=dif)
		print("word:", self.word.word)

	def failed_guess(self):
		self.tries -= 1
		self.sounds["ingame_pop"].play()
		list(reversed(self.pops))[self.tries].start_anim()

