import vars


def f_quit():
	vars.pg.quit()
	quit()


def text_object(surface, txt, txt_font=None, pos=(0, 0), fg_color=(0, 0, 0)):
	'''It renders the font with a text, text font, text color and displays it in the given position'''

	if txt_font == None:
		font = vars.pg.font.Font(txt_font, 45)
	else:
		font = txt_font
	text_surface = font.render(txt, True, fg_color)
	surface.blit(text_surface, text_surface.get_rect(center=pos))


def en_dis_music(music_on, force_off=False):
	'''It enables or disables the music'''

	if music_on:
		if not force_off:
			vars.pg.mixer.music.set_volume(0)
	else:
		vars.pg.mixer.music.set_volume(1)
		if force_off:
			vars.pg.mixer.music.set_volume(0)


def en_dis_sound(sound_on):
	'''It enables or disables the sound'''

	if sound_on:
		for rs_sound in vars.raw_sounds:
			rs_sound.set_volume(0)
	else:
		for rs_sound in vars.raw_sounds:
			rs_sound.set_volume(1)


def f_sorting():
	'''It sorts the words in the list by difficulty (rarity and length)'''
	for word in vars.words:
		[vars.dif10.append(word) for char in word if char in vars.dif_rare[4] and len(word) > 5 and not any(word in sublist for sublist in vars.dif_all)]
		[vars.dif9.append(word) for char in word if char in vars.dif_rare[4] and len(word) <= 5 and not any(word in sublist for sublist in vars.dif_all)]
		[vars.dif8.append(word) for char in word if char in vars.dif_rare[3] and len(word) > 5 and not any(word in sublist for sublist in vars.dif_all)]
		[vars.dif7.append(word) for char in word if char in vars.dif_rare[3] and len(word) <= 5 and not any(word in sublist for sublist in vars.dif_all)]
		[vars.dif6.append(word) for char in word if char in vars.dif_rare[2] and len(word) > 5 and not any(word in sublist for sublist in vars.dif_all)]
		[vars.dif5.append(word) for char in word if char in vars.dif_rare[2] and len(word) <= 5 and not any(word in sublist for sublist in vars.dif_all)]
		[vars.dif4.append(word) for char in word if char in vars.dif_rare[1] and len(word) > 5 and not any(word in sublist for sublist in vars.dif_all)]
		[vars.dif3.append(word) for char in word if char in vars.dif_rare[1] and len(word) <= 5 and not any(word in sublist for sublist in vars.dif_all)]
		[vars.dif2.append(word) for char in word if char in vars.dif_rare[0] and len(word) > 5 and not any(word in sublist for sublist in vars.dif_all)]
		[vars.dif1.append(word) for char in word if char in vars.dif_rare[0] and len(word) <= 5 and not any(word in sublist for sublist in vars.dif_all)]


class Button:
	def __init__(self, surface, width, height, x, y, i_color, a_color, text, font, enabled=True, i_font_color=(0, 0, 0),
				a_font_color=(255, 0, 0), act_margin=6, but_transp=False, text_centered=None):
		self.surface = surface
		self.width = width
		self.height = height
		self.x = x - self.width * 0.5  # Center of the button (width)
		self.y = y
		self.i_color = i_color
		self.a_color = a_color
		self.text = text
		self.font = font
		self.enabled = enabled
		self.i_font_color = i_font_color
		self.a_font_color = a_font_color
		self.act_margin = act_margin
		self.inact_rectangle = self.x, self.y, self.width, self.height

		# Sets default active zone margin with the option to modify it:
		self.act_rectangle = self.x+self.act_margin, self.y+self.act_margin, self.width-self.act_margin*2, self.height-self.act_margin*2
		self.but_transp = but_transp
		self.text_centered = text_centered


	def text_object_but(self, txt, txt_font, fg_color, x, y):
		'''It renders the font with a text, text font, and text color centering it on the button by default'''

		text_surface = txt_font.render(txt, True, fg_color)
		if self.text_centered == None:
			return text_surface, text_surface.get_rect(center=(x + (self.width * 0.5), y + (self.height * 0.5) - 3))
		else:
			return text_surface, text_surface.get_rect(center=self.text_centered)

	def drawing(self):
		'''It draws the button with the text (text itself, text font and text color), button size and position given in the arguments'''

		if self.enabled:
			if self.but_transp:
				surf = vars.pg.Surface((self.width, self.height), vars.pg.SRCALPHA)
				surf.fill((255, 255, 255, 0))
				self.surface.blit(surf, (self.x, self.y))
				text_surface, text_rectangle = self.text_object_but(self.text, self.font, self.i_font_color, self.x, self.y)
				if vars.pg.Rect(self.inact_rectangle).collidepoint(vars.pg.mouse.get_pos()):
					text_surface, text_rectangle = self.text_object_but(self.text, self.font, self.a_font_color, self.x, self.y)
				self.surface.blit(text_surface, text_rectangle)
			else:
				vars.pg.draw.rect(self.surface, self.i_color, self.inact_rectangle)
				text_surface, text_rectangle = self.text_object_but(self.text, self.font, self.i_font_color, self.x, self.y)
				if vars.pg.Rect(self.inact_rectangle).collidepoint(vars.pg.mouse.get_pos()):
					vars.pg.draw.rect(self.surface, self.a_color, self.act_rectangle)
					text_surface, text_rectangle = self.text_object_but(self.text, self.font, self.a_font_color, self.x, self.y)
				self.surface.blit(text_surface, text_rectangle)
		else:
			vars.pg.draw.rect(self.surface, (150, 150, 150), self.inact_rectangle)
			text_surface, text_rectangle = self.text_object_but(self.text, self.font, (80, 80, 80), self.x, self.y)
			self.surface.blit(text_surface, text_rectangle)


class Sound:
	def __init__(self, track, times_played=1, fadeout=1000, fade_ms=2000, music_on=True, sound_on=True):
		self.track = track
		self.times_played = times_played
		self.fadeout = fadeout
		self.fade_ms = fade_ms
		self.music_on = music_on
		self.sound_on = sound_on

	def play_music(self):
		'''Plays in loop the music file in the given path fading out the current music before'''

		vars.pg.mixer.music.fadeout(self.fadeout)
		vars.pg.mixer.music.load(self.track)
		vars.pg.mixer.music.play(self.times_played)

	def play_sound(self):
		'''Plays once the sound file in the given path'''

		vars.pg.mixer.Sound.play(self.track)


class Anim:
	def __init__(self, surface, img_anim, img_anim_bg=None, num_frames=0, frame=0,
					switch_music=False, switch_sound=False, title_done=False, font_menu_title=vars.font_menu_title,
					font_menu_but=vars.font_menu_but, clock=vars.pg.time.Clock(), sound=None):
		self.surface = surface
		self.img_anim = img_anim
		self.img_anim_bg = img_anim_bg
		self.num_frames = num_frames
		self.frame = frame
		self.switch_music = switch_music
		self.switch_sound = switch_sound
		self.title_done = title_done
		self.font_menu_title = font_menu_title
		self.font_menu_but = font_menu_but
		self.clock = clock
		self.sound = sound
		self.disp_w, self.disp_h = self.surface.get_size()

	def anim_space(self):
		'''It executes the blinking text in the intro'''

		space_rect = self.img_anim.get_rect()
		frame_w, frame_h = space_rect.width, space_rect.height / self.num_frames
		frame_list = list([(0, frame_h * frame, frame_w, frame_h) for frame in range(self.num_frames)])
		self.surface.blit(vars.img_menu_bg, (0, 0))
		self.surface.blit(vars.img_menu_space, (self.disp_w*0.5 - (frame_w / 2), self.disp_h*0.75), frame_list[self.frame])

	def anim_title(self):
		'''It executes once the title animation in the main menu screen'''

		movement = -200
		if self.title_done == False:
			while movement < self.disp_h * 0.125 + 5:
				self.surface.blit(vars.img_menu_bg, (0, 0))
				text_object(self.surface, 'hang_the_witch', txt_font=vars.font_menu_title, pos=(self.disp_w*0.5, movement), fg_color=(122, 76, 122))
				movement += 5
				vars.pg.display.update()
				self.clock.tick(30)
			vars.pg.time.delay(1000)
		else:
			self.surface.blit(vars.img_menu_bg, (0, 0))
			text_object(self.surface, 'hang_the_witch', txt_font=vars.font_menu_title, pos=(self.disp_w*0.5, self.disp_h * 0.125), fg_color=(122, 76, 122))

	def anim_boards(self):
		'''It initializes the boards animation pre-game'''

		vars.pg.mouse.set_visible(False)
		boards_bg_rect = self.img_anim.get_rect()
		frame, mov = 0, 0
		frame_w, frame_h = boards_bg_rect.width, boards_bg_rect.height / self.num_frames
		frame_list = list([(0, frame_h * frame, frame_w, frame_h) for frame in range(self.num_frames)])
		for frm in range(0, self.num_frames):
			if frm % 2 == 0:
				mov = -self.disp_w
				while mov <= 0:
					self.surface.blit(self.img_anim, (mov, frame * frame_h), frame_list[frame])
					mov += 20
					vars.pg.display.update()
					self.clock.tick(150)
					# if mov == -200:                       # with sound is good in mov=10 / tick(150)
					# 	Sound.play_sound(self.sound)
			else:
				mov = self.disp_w
				while mov >= 0:
					self.surface.blit(self.img_anim, (mov, frame * frame_h), frame_list[frame])
					mov -= 20
					vars.pg.display.update()
					self.clock.tick(150)
					# if mov == 200:
					# 	Sound.play_sound(self.sound)
			frame += 1
			vars.pg.display.update()
			self.clock.tick(200)

	def anim_fade_out(self):
		'''It fades out from one screen to the other'''
		self.img_anim = self.img_anim.convert()
		self.img_anim_bg = self.img_anim_bg.convert()
		i = 0
		for event in vars.pg.event.get():
			if event.type == 12:
				f_quit()
		while i < 150:
			self.img_anim.set_alpha(i)
			self.surface.blit(self.img_anim, (0, 0))
			i += 10
			vars.pg.time.delay(60)
			vars.pg.display.update()
		i = 0
		while i < 150:
			self.img_anim_bg.set_alpha(i)
			self.surface.blit(self.img_anim_bg, (0, 0))
			i += 10
			vars.pg.time.delay(60)
			vars.pg.display.update()

	def anim_music_but(self):
		'''It executes the sound button animation in the scroll menu'''

		position = (self.disp_w * 0.56, self.disp_h * 0.49)
		scroll_music_but_rect = vars.img_scroll_but_sound.get_rect()
		frame_w, frame_h = scroll_music_but_rect.width, scroll_music_but_rect.height / self.num_frames
		frame_list = list([(0, frame_h * frame, frame_w, frame_h) for frame in range(self.num_frames)])
		inverse_frame_list = frame_list[::-1]
		if vars.music_on:
			self.surface.blit(vars.img_scroll_but_sound, position, frame_list[0])
			if self.switch_music:
				for i in range(self.num_frames):
					self.surface.blit(vars.img_scroll_but_sound, position, frame_list[i])
					vars.pg.display.update()
					self.clock.tick(20)
				self.switch_music = not self.switch_music
		else:
			self.surface.blit(vars.img_scroll_but_sound, position, frame_list[4])
			if self.switch_music:
				for i in range(self.num_frames):
					self.surface.blit(vars.img_scroll_but_sound, position, inverse_frame_list[i])
					vars.pg.display.update()
					self.clock.tick(20)
				self.switch_music = not self.switch_music

	def anim_sound_but(self):
		'''It executes the sound button animation in the scroll menu'''

		position = (self.disp_w * 0.57, self.disp_h * 0.59)
		scroll_sound_but_rect = vars.img_scroll_but_sound.get_rect()
		frame_w, frame_h = scroll_sound_but_rect.width, scroll_sound_but_rect.height / self.num_frames
		frame_list = list([(0, frame_h * frame, frame_w, frame_h) for frame in range(self.num_frames)])
		inverse_frame_list = frame_list[::-1]
		if vars.sound_on:
			self.surface.blit(vars.img_scroll_but_sound, position, frame_list[0])
			if self.switch_sound:
				for i in range(self.num_frames):
					self.surface.blit(vars.img_scroll_but_sound, position, frame_list[i])
					vars.pg.display.update()
					self.clock.tick(20)
				self.switch_sound = not self.switch_sound
		else:
			self.surface.blit(vars.img_scroll_but_sound, position, frame_list[4])
			if self.switch_sound:
				for i in range(self.num_frames):
					self.surface.blit(vars.img_scroll_but_sound, position, inverse_frame_list[i])
					vars.pg.display.update()
					self.clock.tick(20)
				self.switch_sound = not self.switch_sound

	def anim_pop(self):
		'''It displays the pop animation with every fail in-game'''

		pop_rect = self.img_anim.get_rect()
		frame_w, frame_h = pop_rect.width / self.num_frames, pop_rect.height
		frame_list = list([(frame_w*frame, 0, frame_w, frame_h) for frame in range(self.num_frames)])

		witch_rect = vars.img_ingame_witch.get_rect()
		witch_frame_w, witch_frame_h = witch_rect.width, int(witch_rect.height / 11)
		witch_frame_list = list([(0, witch_frame_h * witch_frame, witch_frame_w, witch_frame_h) for witch_frame in range(11)])
		witch_frame_list.reverse()

		self.frame = 0
		Sound.play_sound(snd_ingame_pop)
		if vars.tries == 10: pass
		elif vars.tries == 9:
			pos = (400, 380)
			while self.frame < self.num_frames:
				self.surface.blit(vars.img_ingame_witch_bg, (pos[0]-frame_w*0.5, pos[1]-frame_h*0.5), (pos[0], pos[1], frame_w, frame_h))
				self.surface.blit(vars.img_ingame_pop, (pos[0]-frame_w*0.5, pos[1]-frame_h*0.5), frame_list[self.frame])
				self.frame += 1

				vars.pg.display.update()
				vars.clock.tick(20)

		elif vars.tries == 8:
			pos = (290, 250)
			while self.frame < self.num_frames:
				self.surface.blit(vars.img_ingame_witch_bg, (pos[0] - frame_w * 0.5, pos[1] - frame_h * 0.5), (pos[0], pos[1], frame_w, frame_h))
				self.surface.blit(vars.img_ingame_pop, (pos[0] - frame_w * 0.5, pos[1] - frame_h * 0.5), frame_list[self.frame])
				self.frame += 1

				vars.pg.display.update()
				vars.clock.tick(20)

		elif vars.tries == 7:
			pos = (400, 110)
			while self.frame < self.num_frames:
				self.surface.blit(vars.img_ingame_witch_bg, (pos[0] - frame_w * 0.5, pos[1] - frame_h * 0.5), (pos[0], pos[1], frame_w, frame_h))
				self.surface.blit(vars.img_ingame_pop, (pos[0] - frame_w * 0.5, pos[1] - frame_h * 0.5), frame_list[self.frame])
				self.frame += 1

				vars.pg.display.update()
				vars.clock.tick(20)

		elif vars.tries == 6:
			pos = (350, 165)
			while self.frame < self.num_frames:
				self.surface.blit(vars.img_ingame_witch_bg, (pos[0] - frame_w * 0.5, pos[1] - frame_h * 0.5), (pos[0], pos[1], frame_w, frame_h))
				self.surface.blit(vars.img_ingame_pop, (pos[0] - frame_w * 0.5, pos[1] - frame_h * 0.5), frame_list[self.frame])
				self.frame += 1

				vars.pg.display.update()
				vars.clock.tick(20)

		elif vars.tries == 5:
			pos = (490, 165)
			while self.frame < self.num_frames:
				self.surface.blit(vars.img_ingame_witch_bg, (pos[0]-frame_w*0.5, pos[1]-frame_h*0.5), (pos[0], pos[1], frame_w, frame_h))
				self.surface.blit(vars.img_ingame_pop, (pos[0]-frame_w*0.5, pos[1]-frame_h*0.5), frame_list[self.frame])
				self.frame += 1

				vars.pg.display.update()
				vars.clock.tick(20)

		elif vars.tries == 4:
			pos = (500, 240)
			while self.frame < self.num_frames:
				self.surface.blit(vars.img_ingame_witch_bg, (pos[0] - frame_w * 0.5, pos[1] - frame_h * 0.5), (pos[0], pos[1], frame_w, frame_h))
				self.surface.blit(vars.img_ingame_pop, (pos[0] - frame_w * 0.5, pos[1] - frame_h * 0.5), frame_list[self.frame])
				self.frame += 1

				vars.pg.display.update()
				vars.clock.tick(20)
		elif vars.tries == 3:
			pos = (475, 235)
			while self.frame < self.num_frames:
				self.surface.blit(vars.img_ingame_witch_bg, (pos[0]-frame_w*0.5, pos[1]-frame_h*0.5), (pos[0], pos[1], frame_w, frame_h))
				self.surface.blit(vars.img_ingame_witch, (pos[0]-frame_w*0.5, pos[1]-frame_h*0.5),(pos[0]-frame_w*0.5-(vars.disp_w*0.5-witch_frame_h*0.5),
									witch_frame_list[vars.tries][1]+(pos[1]-frame_h*0.5-vars.disp_h*0.4-witch_frame_h*0.5), frame_w, frame_h))
				self.surface.blit(vars.img_ingame_pop, (pos[0]-frame_w*0.5, pos[1]-frame_h*0.5), frame_list[self.frame])
				self.frame += 1

				vars.pg.display.update()
				vars.clock.tick(20)

		elif vars.tries == 2:
			pos = (520, 235)
			while self.frame < self.num_frames:
				self.surface.blit(vars.img_ingame_witch_bg, (pos[0] - frame_w * 0.5, pos[1] - frame_h * 0.5), (pos[0], pos[1], frame_w, frame_h))
				self.surface.blit(vars.img_ingame_witch, (pos[0]-frame_w*0.5, pos[1]-frame_h*0.5),(pos[0]-frame_w*0.5-(vars.disp_w*0.5-witch_frame_h*0.5),
									witch_frame_list[vars.tries][1]+(pos[1]-frame_h*0.5-vars.disp_h*0.4-witch_frame_h*0.5), frame_w, frame_h))
				self.surface.blit(vars.img_ingame_pop, (pos[0] - frame_w * 0.5, pos[1] - frame_h * 0.5), frame_list[self.frame])
				self.frame += 1

				vars.pg.display.update()
				vars.clock.tick(20)

		elif vars.tries == 1:
			pos = (488, 315)
			while self.frame < self.num_frames:
				self.surface.blit(vars.img_ingame_witch_bg, (pos[0] - frame_w * 0.5, pos[1] - frame_h * 0.5), (pos[0], pos[1], frame_w, frame_h))
				self.surface.blit(vars.img_ingame_witch, (pos[0]-frame_w*0.5, pos[1]-frame_h*0.5),(pos[0]-frame_w*0.5-(vars.disp_w*0.5-witch_frame_h*0.5),
									witch_frame_list[vars.tries][1]+(pos[1]-frame_h*0.5-vars.disp_h*0.4-witch_frame_h*0.5), frame_w, frame_h))
				self.surface.blit(vars.img_ingame_pop, (pos[0] - frame_w * 0.5, pos[1] - frame_h * 0.5), frame_list[self.frame])
				self.frame += 1

				vars.pg.display.update()
				vars.clock.tick(20)

		elif vars.tries == 0:
			pos = (505, 315)
			while self.frame < self.num_frames:
				self.surface.blit(vars.img_ingame_witch_bg, (pos[0] - frame_w * 0.5, pos[1] - frame_h * 0.5), (pos[0], pos[1], frame_w, frame_h))
				self.surface.blit(vars.img_ingame_witch, (pos[0]-frame_w*0.5, pos[1]-frame_h*0.5),(pos[0]-frame_w*0.5-(vars.disp_w*0.5-witch_frame_h*0.5),
									witch_frame_list[vars.tries][1]+(pos[1]-frame_h*0.5-vars.disp_h*0.4-witch_frame_h*0.5), frame_w, frame_h))
				self.surface.blit(vars.img_ingame_pop, (pos[0] - frame_w * 0.5, pos[1] - frame_h * 0.5), frame_list[self.frame])
				self.frame += 1

				vars.pg.display.update()
				vars.clock.tick(20)

	def anim_scratch(self, letter):
		'''It executes the scratching over the letters in the game'''

		# Coords list of the char that equals the letter key_down
		pos_index_list = [vars.letter_pos[index] for index, char in enumerate(vars.char_list) if char == letter]

		# Removes the guessed char from 'removable_char_list'
		[vars.removable_char_list.remove(char) for char in vars.char_list if char == letter]
		vars.letters_guessed = list(set(vars.char_list) - set(vars.removable_char_list))

		underlines_rect = self.img_anim.get_rect()
		frame_w, frame_h = underlines_rect.width, underlines_rect.height / self.num_frames
		frame_list = list([(0, frame_h * frame, frame_w, frame_h) for frame in range(self.num_frames)])

		for pos in pos_index_list:                  # 'pos' are the coords of each letter
			self.frame = 0
			Sound.play_sound(snd_ingame_scratch)
			while self.frame < self.num_frames:

				# Instead of blitting the whole bg, it blits a crop of the size and position of each letter
				self.surface.blit(vars.img_ingame_witch_bg, pos, (pos[0], pos[1], frame_w, frame_h))

				# Blitting the letters independently
				text_object(self.surface, letter, pos=(pos[0]+16, pos[1]+25))

				# Blitting the scratch_animation itself, also independently
				self.surface.blit(vars.img_ingame_scratch, pos, frame_list[self.frame])
				self.frame += 1

				vars.pg.display.update()
				vars.clock.tick(15)

	def anim_or_not(self):
		'''It displays the 'or not...' message at the end of the game over screen'''

		or_not_rect = self.img_anim.get_rect()
		frame_w, frame_h = or_not_rect.width, int(or_not_rect.height/self.num_frames)
		frame_list = list([(0, frame_h*frame, frame_w, frame_h) for frame in range(self.num_frames)])

		while self.frame < self.num_frames:
			self.surface.blit(self.img_anim, (vars.disp_w*0.5-frame_w*0.5, vars.disp_h*0.5-frame_h*0.5), frame_list[self.frame])
			self.frame += 1

			vars.pg.display.update()
			vars.clock.tick(5)


class Diff:
	def __init__(self, surface=vars.screen, bg_surface=vars.img_scroll_dif, but_width=30, but_height=40,
				num_buttons=10, margin=60):
		self.surface = surface
		self.disp_w, self.disp_h = self.surface.get_size()
		self.bg_surface = bg_surface
		self.but_width = but_width
		self.but_height = but_height
		self.num_buttons = num_buttons
		self.margin = margin

	def diff_blit(self):
		'''It blits the difficulty buttons on the dif choice menu'''
		bg_surface_rect = self.bg_surface.get_rect()
		self.surface.blit(self.bg_surface, (self.disp_w*0.5-bg_surface_rect.width*0.5, self.disp_h*0.5-bg_surface_rect.height*0.5))
		text_object(self.surface, 'Choose difficulty', txt_font=vars.font_dif_txt, pos=(self.disp_w*0.5, self.disp_h*0.32))

		for button in range(int(self.num_buttons*0.5)):
			b_dif = Button(self.surface, self.but_width, self.but_height, ((self.disp_w*0.5-(self.but_width+self.margin)
							*(self.num_buttons*0.25))+(self.but_width+self.margin)*0.5)+(self.but_width+self.margin)*button,
							bg_surface_rect.height*0.65, (130, 96, 94), (179, 104, 100), str(button+1), vars.font_dif_but,
							text_centered=(((self.disp_w*0.5-(self.but_width+self.margin)*(self.num_buttons*0.25))+
							(self.but_width+self.margin)*0.5)+(self.but_width+self.margin)*button,
							bg_surface_rect.height*0.65+self.but_height*0.5+4))
			b_dif.drawing()
			if len(vars.dif_but_list) < self.num_buttons:
				vars.dif_but_list.append(b_dif)
		for button in range(int(self.num_buttons*0.5), self.num_buttons):
			b_dif = Button(self.surface, self.but_width, self.but_height, ((self.disp_w*0.5-(self.but_width+self.margin)
							*(self.num_buttons*0.25))+(self.but_width+self.margin)*0.5)+(self.but_width+self.margin)*
							(button-self.num_buttons*0.5), bg_surface_rect.height*0.85, (130, 96, 94), (179, 104, 100),
							str(button+1), vars.font_dif_but,
							text_centered=(((self.disp_w*0.5-(self.but_width+self.margin)*(self.num_buttons*0.25))+
							(self.but_width+self.margin)*0.5)+(self.but_width+self.margin)*(button-self.num_buttons*0.5),
							bg_surface_rect.height*0.85+self.but_height*0.5+4))
			b_dif.drawing()
			if len(vars.dif_but_list) < self.num_buttons:
				vars.dif_but_list.append(b_dif)

	def f_randomize(self):
		'''Generates a random word from the chosen difficulty list'''

		diff_choice = vars.dif_all[vars.diff_num_choice-1]
		vars.random_word = vars.r.choice(diff_choice)
		vars.char_list = list([char for char in vars.random_word])
		vars.removable_char_list = list([char for char in vars.random_word])


class Hang:
	def __init__(self, surface=vars.screen, letter_num=0, letter_width=32, letter_height=50, margin=20):
		self.surface = surface
		self.disp_w, self.disp_h = self.surface.get_size()
		self.letter_num = letter_num
		self.letter_width = letter_width
		self.letter_height = letter_height
		self.margin = margin

	def f_witch(self):
		'''It displays the hanged witch in-game'''

		witch_rect = vars.img_ingame_witch.get_rect()
		frame_w, frame_h = witch_rect.width, witch_rect.height / 11
		frame_list = list([(0, frame_h * frame, frame_w, frame_h) for frame in range(11)])
		frame_list.reverse()
		self.surface.blit(vars.img_ingame_witch, (self.disp_w*0.5-frame_w*0.5, self.disp_h*0.4-frame_h*0.5), frame_list[vars.tries])

	def f_letters(self):
		'''It blits the letters behind the covers in-game'''

		vars.letter_pos.clear()
		for letter in range(self.letter_num):
			pos = (self.disp_w * 0.5 - ((self.letter_width + self.margin) * self.letter_num * 0.5) + (
						self.letter_width + self.margin) * letter + self.margin * 0.5, self.disp_h * 0.7)
			vars.letter_pos.append(pos)

		vars.letters_guessed = list(set(vars.char_list) - set(vars.removable_char_list))
		for letter_g in vars.letters_guessed:
			[text_object(self.surface, letter_g, pos=(vars.letter_pos[index][0]+self.letter_width*0.5, vars.letter_pos[index][1]+self.letter_height*0.5)) for index, char in enumerate(vars.char_list) if char == letter_g]

	def f_covers(self, letter=None):
		'''It blits the covers over the letters in-game'''

		if letter in vars.removable_char_list:
			anim_scratch.anim_scratch(letter)
		else:
			for index, char1 in enumerate(vars.char_list):
				if len(vars.removable_char_list) > 0:

					# If 'char1' is not guessed blit the cover
					if char1 in vars.removable_char_list:
						self.surface.blit(vars.img_ingame_scratch, vars.letter_pos[index], (0, 0, 32, 50))

					# If 'char1' is guessed blit the underline
					else:
						self.surface.blit(vars.img_ingame_scratch, vars.letter_pos[index], (0, 600, 32, 50))

				# If all the letters are guessed (empty removable_char_list), blit underlines
				else:
					self.surface.blit(vars.img_ingame_scratch, vars.letter_pos[index], (0, 600, 32, 50))


# Sound #
snd_but_click = Sound(vars.rs_but_click)
snd_menu_wind = Sound(vars.rm_menu_wind, -1)
snd_menu_but_play = Sound(vars.rs_menu_but_play)
snd_ingame_music = Sound(vars.rm_ingame_music, -1)
snd_ingame_scratch = Sound(vars.rs_ingame_scratch)
snd_ingame_pop = Sound(vars.rs_ingame_pop)
snd_won = Sound(vars.rs_won)
snd_gameover = Sound(vars.rs_gameover)
snd_scroll = Sound(vars.rs_scroll)

# Animations #
anim_menu_title = Anim(vars.screen, img_anim=vars.img_menu_bg)
anim_ingame_boards = Anim(surface=vars.screen, img_anim=vars.img_ingame_bg_board, num_frames=6)
anim_scroll_music_but = Anim(vars.screen, img_anim=vars.img_scroll_but_sound, num_frames=5)
anim_scroll_sound_but = Anim(vars.screen, img_anim=vars.img_scroll_but_sound, num_frames=5)
anim_scratch = Anim(surface=vars.screen, img_anim=vars.img_ingame_scratch, num_frames=13)

# Buttons #
but_menu_play = Button(vars.screen, 200, 50, vars.disp_w*0.5, vars.disp_h*0.7, (130, 96, 94), (179, 104, 100), 'Play', vars.font_menu_but)
but_menu_quit = Button(vars.screen, 200, 50, vars.disp_w*0.5, vars.disp_h*0.8, (130, 96, 94), (179, 104, 100), 'Quit', vars.font_menu_but)
but_ingame_menu = Button(vars.screen, 100, 25, vars.disp_w*0.9, vars.disp_h*0.05, (130, 96, 94), (179, 104, 100), 'Menu', vars.font_ingame_but, act_margin=3)
but_gameover_play = Button(vars.screen, 200, 50, vars.disp_w*0.3, vars.disp_h*0.6, (130, 96, 94), (179, 104, 100), 'Play again', vars.font_menu_but, act_margin=3)
but_gameover_menu = Button(vars.screen, 200, 50, vars.disp_w*0.7, vars.disp_h*0.6, (130, 96, 94), (179, 104, 100), 'Main menu', vars.font_menu_but, act_margin=3)
but_scroll_resume = Button(vars.screen, 195, 30, vars.disp_w*0.5, vars.disp_h*0.3, (255, 255, 255), (255, 255, 255), 'Resume game', vars.font_scroll_menu_but, but_transp=True)
but_scroll_new = Button(vars.screen, 150, 30, vars.disp_w*0.49, vars.disp_h*0.4, (255, 255, 255), (255, 255, 255), 'New game', vars.font_scroll_menu_but, but_transp=True)
but_scroll_music = Button(vars.screen, 180, 30, vars.disp_w*0.52, vars.disp_h*0.5, (130, 96, 94), (179, 104, 100), 'Music', vars.font_scroll_menu_but, text_centered=(370, vars.disp_h*0.5+15), but_transp=True)
but_scroll_sound = Button(vars.screen, 175, 30, vars.disp_w*0.52, vars.disp_h*0.6, (130, 96, 94), (179, 104, 100), 'Sound', vars.font_scroll_menu_but, text_centered=(375, vars.disp_h*0.6+15), but_transp=True)
but_scroll_main = Button(vars.screen, 150, 30, vars.disp_w*0.5, vars.disp_h*0.7, (255, 255, 255), (255, 255, 255), 'Main menu', vars.font_scroll_menu_but, but_transp=True)
but_verify_yes_main = Button(vars.screen, 80, 25, vars.disp_w*0.43, vars.disp_h*0.525, (130, 96, 94), (179, 104, 100), 'Yes', vars.font_verify_but)
but_verify_no = Button(vars.screen, 80, 25, vars.disp_w*0.57, vars.disp_h*0.525, (130, 96, 94), (179, 104, 100), 'No', vars.font_verify_but)
but_accept = Button(vars.screen, 80, 25, vars.disp_w*0.5, vars.disp_h*0.525, (130, 96, 94), (179, 104, 100), 'Accept', vars.font_verify_but)
