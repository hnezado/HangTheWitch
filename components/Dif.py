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