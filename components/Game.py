from functions import text_object
from components.Word import Word


class Game:
	def __init__(self, disp, fonts, images, subcomponents, word_config_presets) -> None:
		self.disp = disp
		self.fonts = fonts
		self.images = images
		self.gallow = self.get_frames(self.images["ingame_gallows"], 11)
		self.scratchs = self.get_frames(self.images["ingame_scratch"], 13)
		self.tries = 5
		self.word_config_presets = word_config_presets
		self.subcomponents = subcomponents
		self.word = ""
		self.letters_properties = []
  
		self.get_gallow_pos()

	@staticmethod
	def get_frames(img, frames_num):
		img_rect = img.get_rect()
		props = {}
		props["w"] = img_rect.width
		props["h"] = img_rect.height / frames_num
		props["frames"] = list([(0, props["h"] * frame, props["w"], props["h"]) for frame in range(frames_num)])
		return props

	def get_gallow_pos(self):
		self.gallow["pos"] = (self.disp["w"]*0.5-self.gallow["w"]*0.5, self.disp["h"]*0.4-self.gallow["h"]*0.5)

	def display(self):
		self.disp["disp"].blit(self.images["ingame_bg_board"], (0, 0))
		self.disp["disp"].blit(self.images["ingame_witch_bg"], (0, 0))
		text_object(self.disp["disp"], 'Remaining tries: ', txt_font=self.fonts["ingame_tries"], pos=(self.disp["w"]*0.47, self.disp["h"]*0.07), fg_color=(150, 0, 0))
		text_object(self.disp["disp"], txt='{}'.format(self.tries), txt_font=self.fonts["ingame_tries"], pos=(self.disp["w"]*0.62, self.disp["h"]*0.07), fg_color=(150, 0, 0))

		# Display Gallow
		self.disp["disp"].blit(self.images["ingame_gallows"], self.gallow["pos"], self.gallow["frames"][10-self.tries])

		# Display Word
		for letter_props in self.letters_properties:
			text_object(surface=self.disp["disp"], txt=letter_props["letter"], pos=letter_props["pos"])

		# Display Covers (anim)
		for letter_props in self.letters_properties:
			if not letter_props["guessed"]:
				pos = [letter_props["pos"][0]-self.word_config_presets["letter"]["dim"]["w"]*0.5, letter_props["pos"][1]-self.word_config_presets["letter"]["dim"]["h"]*0.5]
				self.disp["disp"].blit(self.images["ingame_scratch"], pos, self.scratchs["frames"][11])
        
        # Sub-components
		for button in self.subcomponents["buttons"]:
			button.display()

	def toggle_dif_menu(self):
		pass

	def new_game(self, dif):
		word_instance = Word(dif)
		self.word = word_instance.generate_word()
		self.letters_properties = word_instance.parse_word(disp=self.disp, word=self.word, word_config_presets=self.word_config_presets
		)
		print("word:", self.word)

# class Dif:
# 	def __init__(self, surface=vars_2.screen, bg_surface=vars_2.img_scroll_dif, but_width=30, but_height=40,
# 				num_buttons=10, margin=60):
# 		self.surface = surface
# 		self.disp_w, self.disp_h = self.surface.get_size()
# 		self.bg_surface = bg_surface
# 		self.but_width = but_width
# 		self.but_height = but_height
# 		self.num_buttons = num_buttons
# 		self.margin = margin

# 	def diff_blit(self):
# 		'''It blits the difficulty buttons on the dif choice menu'''
# 		bg_surface_rect = self.bg_surface.get_rect()
# 		self.surface.blit(self.bg_surface, (self.disp_w*0.5-bg_surface_rect.width*0.5, self.disp_h*0.5-bg_surface_rect.height*0.5))
# 		text_object(self.surface, 'Choose difficulty', txt_font=vars_2.font_dif_txt, pos=(self.disp_w*0.5, self.disp_h*0.32))

# 		for button in range(int(self.num_buttons*0.5)):
# 			b_dif = Button(self.surface, self.but_width, self.but_height, ((self.disp_w*0.5-(self.but_width+self.margin)
# 							*(self.num_buttons*0.25))+(self.but_width+self.margin)*0.5)+(self.but_width+self.margin)*button,
# 							bg_surface_rect.height*0.65, (130, 96, 94), (179, 104, 100), str(button+1), vars_2.font_dif_but,
# 							text_centered=(((self.disp_w*0.5-(self.but_width+self.margin)*(self.num_buttons*0.25))+
# 							(self.but_width+self.margin)*0.5)+(self.but_width+self.margin)*button,
# 							bg_surface_rect.height*0.65+self.but_height*0.5+4))
# 			b_dif.drawing()
# 			if len(vars_2.dif_but_list) < self.num_buttons:
# 				vars_2.dif_but_list.append(b_dif)
# 		for button in range(int(self.num_buttons*0.5), self.num_buttons):
# 			b_dif = Button(self.surface, self.but_width, self.but_height, ((self.disp_w*0.5-(self.but_width+self.margin)
# 							*(self.num_buttons*0.25))+(self.but_width+self.margin)*0.5)+(self.but_width+self.margin)*
# 							(button-self.num_buttons*0.5), bg_surface_rect.height*0.85, (130, 96, 94), (179, 104, 100),
# 							str(button+1), vars_2.font_dif_but,
# 							text_centered=(((self.disp_w*0.5-(self.but_width+self.margin)*(self.num_buttons*0.25))+
# 							(self.but_width+self.margin)*0.5)+(self.but_width+self.margin)*(button-self.num_buttons*0.5),
# 							bg_surface_rect.height*0.85+self.but_height*0.5+4))
# 			b_dif.drawing()
# 			if len(vars_2.dif_but_list) < self.num_buttons:
# 				vars_2.dif_but_list.append(b_dif)

# 	def f_randomize(self):
# 		'''Generates a random word from the chosen difficulty list'''

# 		diff_choice = vars_2.dif_all[vars_2.diff_num_choice-1]
# 		vars_2.random_word = vars_2.r.choice(diff_choice)
# 		vars_2.char_list = list([char for char in vars_2.random_word])
# 		vars_2.removable_char_list = list([char for char in vars_2.random_word])
