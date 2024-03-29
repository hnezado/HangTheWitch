


def f_sorting():
	'''It sorts the words in the list by difficulty (rarity and length)'''
	for word in vars_2.words:
		[vars_2.dif10.append(word) for char in word if char in vars_2.dif_rare[4] and len(word) > 5 and not any(word in sublist for sublist in vars_2.dif_all)]
		[vars_2.dif9.append(word) for char in word if char in vars_2.dif_rare[4] and len(word) <= 5 and not any(word in sublist for sublist in vars_2.dif_all)]
		[vars_2.dif8.append(word) for char in word if char in vars_2.dif_rare[3] and len(word) > 5 and not any(word in sublist for sublist in vars_2.dif_all)]
		[vars_2.dif7.append(word) for char in word if char in vars_2.dif_rare[3] and len(word) <= 5 and not any(word in sublist for sublist in vars_2.dif_all)]
		[vars_2.dif6.append(word) for char in word if char in vars_2.dif_rare[2] and len(word) > 5 and not any(word in sublist for sublist in vars_2.dif_all)]
		[vars_2.dif5.append(word) for char in word if char in vars_2.dif_rare[2] and len(word) <= 5 and not any(word in sublist for sublist in vars_2.dif_all)]
		[vars_2.dif4.append(word) for char in word if char in vars_2.dif_rare[1] and len(word) > 5 and not any(word in sublist for sublist in vars_2.dif_all)]
		[vars_2.dif3.append(word) for char in word if char in vars_2.dif_rare[1] and len(word) <= 5 and not any(word in sublist for sublist in vars_2.dif_all)]
		[vars_2.dif2.append(word) for char in word if char in vars_2.dif_rare[0] and len(word) > 5 and not any(word in sublist for sublist in vars_2.dif_all)]
		[vars_2.dif1.append(word) for char in word if char in vars_2.dif_rare[0] and len(word) <= 5 and not any(word in sublist for sublist in vars_2.dif_all)]


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

		vars_2.pg.mixer.music.fadeout(self.fadeout)
		vars_2.pg.mixer.music.load(self.track)
		vars_2.pg.mixer.music.play(self.times_played)

	def play_sound(self):
		'''Plays once the sound file in the given path'''

		vars_2.pg.mixer.Sound.play(self.track)


class Anim:
	def __init__(self, surface, img_anim, img_anim_bg=None, num_frames=0, frame=0,
					switch_music=False, switch_sound=False, title_done=False, font_menu_title=vars_2.font_menu_title,
					font_menu_but=vars_2.font_menu_but, clock=vars_2.pg.time.Clock(), sound=None):
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
		self.surface.blit(vars_2.img_menu_bg, (0, 0))
		self.surface.blit(vars_2.img_menu_space, (self.disp_w*0.5 - (frame_w / 2), self.disp_h*0.75), frame_list[self.frame])

	def anim_title(self):
		'''It executes once the title animation in the main menu screen'''

		movement = -200
		if self.title_done == False:
			while movement < self.disp_h * 0.125 + 5:
				self.surface.blit(vars_2.img_menu_bg, (0, 0))
				text_object(self.surface, 'hang_the_witch', txt_font=vars_2.font_menu_title, pos=(self.disp_w*0.5, movement), fg_color=(122, 76, 122))
				movement += 5
				vars_2.pg.display.update()
				self.clock.tick(30)
			vars_2.pg.time.delay(1000)
		else:
			self.surface.blit(vars_2.img_menu_bg, (0, 0))
			text_object(self.surface, 'hang_the_witch', txt_font=vars_2.font_menu_title, pos=(self.disp_w*0.5, self.disp_h * 0.125), fg_color=(122, 76, 122))

	def anim_boards(self):
		'''It initializes the boards animation pre-game'''

		vars_2.pg.mouse.set_visible(False)
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
					vars_2.pg.display.update()
					self.clock.tick(150)
					# if mov == -200:                       # with sound is good in mov=10 / tick(150)
					# 	Sound.play_sound(self.sound)
			else:
				mov = self.disp_w
				while mov >= 0:
					self.surface.blit(self.img_anim, (mov, frame * frame_h), frame_list[frame])
					mov -= 20
					vars_2.pg.display.update()
					self.clock.tick(150)
					# if mov == 200:
					# 	Sound.play_sound(self.sound)
			frame += 1
			vars_2.pg.display.update()
			self.clock.tick(200)

	def anim_fade_out(self):
		'''It fades out from one screen to the other'''
		self.img_anim = self.img_anim.convert()
		self.img_anim_bg = self.img_anim_bg.convert()
		i = 0
		for event in vars_2.pg.event.get():
			if event.type == 12:
				f_quit()
		while i < 150:
			self.img_anim.set_alpha(i)
			self.surface.blit(self.img_anim, (0, 0))
			i += 10
			vars_2.pg.time.delay(60)
			vars_2.pg.display.update()
		i = 0
		while i < 150:
			self.img_anim_bg.set_alpha(i)
			self.surface.blit(self.img_anim_bg, (0, 0))
			i += 10
			vars_2.pg.time.delay(60)
			vars_2.pg.display.update()

	def anim_music_but(self):
		'''It executes the sound button animation in the scroll menu'''

		position = (self.disp_w * 0.56, self.disp_h * 0.49)
		scroll_music_but_rect = vars_2.img_scroll_but_sound.get_rect()
		frame_w, frame_h = scroll_music_but_rect.width, scroll_music_but_rect.height / self.num_frames
		frame_list = list([(0, frame_h * frame, frame_w, frame_h) for frame in range(self.num_frames)])
		inverse_frame_list = frame_list[::-1]
		if vars_2.music_on:
			self.surface.blit(vars_2.img_scroll_but_sound, position, frame_list[0])
			if self.switch_music:
				for i in range(self.num_frames):
					self.surface.blit(vars_2.img_scroll_but_sound, position, frame_list[i])
					vars_2.pg.display.update()
					self.clock.tick(20)
				self.switch_music = not self.switch_music
		else:
			self.surface.blit(vars_2.img_scroll_but_sound, position, frame_list[4])
			if self.switch_music:
				for i in range(self.num_frames):
					self.surface.blit(vars_2.img_scroll_but_sound, position, inverse_frame_list[i])
					vars_2.pg.display.update()
					self.clock.tick(20)
				self.switch_music = not self.switch_music

	def anim_sound_but(self):
		'''It executes the sound button animation in the scroll menu'''

		position = (self.disp_w * 0.57, self.disp_h * 0.59)
		scroll_sound_but_rect = vars_2.img_scroll_but_sound.get_rect()
		frame_w, frame_h = scroll_sound_but_rect.width, scroll_sound_but_rect.height / self.num_frames
		frame_list = list([(0, frame_h * frame, frame_w, frame_h) for frame in range(self.num_frames)])
		inverse_frame_list = frame_list[::-1]
		if vars_2.sound_on:
			self.surface.blit(vars_2.img_scroll_but_sound, position, frame_list[0])
			if self.switch_sound:
				for i in range(self.num_frames):
					self.surface.blit(vars_2.img_scroll_but_sound, position, frame_list[i])
					vars_2.pg.display.update()
					self.clock.tick(20)
				self.switch_sound = not self.switch_sound
		else:
			self.surface.blit(vars_2.img_scroll_but_sound, position, frame_list[4])
			if self.switch_sound:
				for i in range(self.num_frames):
					self.surface.blit(vars_2.img_scroll_but_sound, position, inverse_frame_list[i])
					vars_2.pg.display.update()
					self.clock.tick(20)
				self.switch_sound = not self.switch_sound

	def anim_pop(self):
		'''It displays the pop animation with every fail in-game'''

		pop_rect = self.img_anim.get_rect()
		frame_w, frame_h = pop_rect.width / self.num_frames, pop_rect.height
		frame_list = list([(frame_w*frame, 0, frame_w, frame_h) for frame in range(self.num_frames)])

		witch_rect = vars_2.img_ingame_witch.get_rect()
		witch_frame_w, witch_frame_h = witch_rect.width, int(witch_rect.height / 11)
		witch_frame_list = list([(0, witch_frame_h * witch_frame, witch_frame_w, witch_frame_h) for witch_frame in range(11)])
		witch_frame_list.reverse()

		self.frame = 0
		Sound.play_sound(snd_ingame_pop)
		if vars_2.tries == 10: pass
		elif vars_2.tries == 9:
			pos = (400, 380)
			while self.frame < self.num_frames:
				self.surface.blit(vars_2.img_ingame_witch_bg, (pos[0]-frame_w*0.5, pos[1]-frame_h*0.5), (pos[0], pos[1], frame_w, frame_h))
				self.surface.blit(vars_2.img_ingame_pop, (pos[0]-frame_w*0.5, pos[1]-frame_h*0.5), frame_list[self.frame])
				self.frame += 1

				vars_2.pg.display.update()
				vars_2.clock.tick(20)

		elif vars_2.tries == 8:
			pos = (290, 250)
			while self.frame < self.num_frames:
				self.surface.blit(vars_2.img_ingame_witch_bg, (pos[0] - frame_w * 0.5, pos[1] - frame_h * 0.5), (pos[0], pos[1], frame_w, frame_h))
				self.surface.blit(vars_2.img_ingame_pop, (pos[0] - frame_w * 0.5, pos[1] - frame_h * 0.5), frame_list[self.frame])
				self.frame += 1

				vars_2.pg.display.update()
				vars_2.clock.tick(20)

		elif vars_2.tries == 7:
			pos = (400, 110)
			while self.frame < self.num_frames:
				self.surface.blit(vars_2.img_ingame_witch_bg, (pos[0] - frame_w * 0.5, pos[1] - frame_h * 0.5), (pos[0], pos[1], frame_w, frame_h))
				self.surface.blit(vars_2.img_ingame_pop, (pos[0] - frame_w * 0.5, pos[1] - frame_h * 0.5), frame_list[self.frame])
				self.frame += 1

				vars_2.pg.display.update()
				vars_2.clock.tick(20)

		elif vars_2.tries == 6:
			pos = (350, 165)
			while self.frame < self.num_frames:
				self.surface.blit(vars_2.img_ingame_witch_bg, (pos[0] - frame_w * 0.5, pos[1] - frame_h * 0.5), (pos[0], pos[1], frame_w, frame_h))
				self.surface.blit(vars_2.img_ingame_pop, (pos[0] - frame_w * 0.5, pos[1] - frame_h * 0.5), frame_list[self.frame])
				self.frame += 1

				vars_2.pg.display.update()
				vars_2.clock.tick(20)

		elif vars_2.tries == 5:
			pos = (490, 165)
			while self.frame < self.num_frames:
				self.surface.blit(vars_2.img_ingame_witch_bg, (pos[0]-frame_w*0.5, pos[1]-frame_h*0.5), (pos[0], pos[1], frame_w, frame_h))
				self.surface.blit(vars_2.img_ingame_pop, (pos[0]-frame_w*0.5, pos[1]-frame_h*0.5), frame_list[self.frame])
				self.frame += 1

				vars_2.pg.display.update()
				vars_2.clock.tick(20)

		elif vars_2.tries == 4:
			pos = (500, 240)
			while self.frame < self.num_frames:
				self.surface.blit(vars_2.img_ingame_witch_bg, (pos[0] - frame_w * 0.5, pos[1] - frame_h * 0.5), (pos[0], pos[1], frame_w, frame_h))
				self.surface.blit(vars_2.img_ingame_pop, (pos[0] - frame_w * 0.5, pos[1] - frame_h * 0.5), frame_list[self.frame])
				self.frame += 1

				vars_2.pg.display.update()
				vars_2.clock.tick(20)
		elif vars_2.tries == 3:
			pos = (475, 235)
			while self.frame < self.num_frames:
				self.surface.blit(vars_2.img_ingame_witch_bg, (pos[0]-frame_w*0.5, pos[1]-frame_h*0.5), (pos[0], pos[1], frame_w, frame_h))
				self.surface.blit(vars_2.img_ingame_witch, (pos[0]-frame_w*0.5, pos[1]-frame_h*0.5),(pos[0]-frame_w*0.5-(vars_2.disp_w*0.5-witch_frame_h*0.5),
									witch_frame_list[vars_2.tries][1]+(pos[1]-frame_h*0.5-vars_2.disp_h*0.4-witch_frame_h*0.5), frame_w, frame_h))
				self.surface.blit(vars_2.img_ingame_pop, (pos[0]-frame_w*0.5, pos[1]-frame_h*0.5), frame_list[self.frame])
				self.frame += 1

				vars_2.pg.display.update()
				vars_2.clock.tick(20)

		elif vars_2.tries == 2:
			pos = (520, 235)
			while self.frame < self.num_frames:
				self.surface.blit(vars_2.img_ingame_witch_bg, (pos[0] - frame_w * 0.5, pos[1] - frame_h * 0.5), (pos[0], pos[1], frame_w, frame_h))
				self.surface.blit(vars_2.img_ingame_witch, (pos[0]-frame_w*0.5, pos[1]-frame_h*0.5),(pos[0]-frame_w*0.5-(vars_2.disp_w*0.5-witch_frame_h*0.5),
									witch_frame_list[vars_2.tries][1]+(pos[1]-frame_h*0.5-vars_2.disp_h*0.4-witch_frame_h*0.5), frame_w, frame_h))
				self.surface.blit(vars_2.img_ingame_pop, (pos[0] - frame_w * 0.5, pos[1] - frame_h * 0.5), frame_list[self.frame])
				self.frame += 1

				vars_2.pg.display.update()
				vars_2.clock.tick(20)

		elif vars_2.tries == 1:
			pos = (488, 315)
			while self.frame < self.num_frames:
				self.surface.blit(vars_2.img_ingame_witch_bg, (pos[0] - frame_w * 0.5, pos[1] - frame_h * 0.5), (pos[0], pos[1], frame_w, frame_h))
				self.surface.blit(vars_2.img_ingame_witch, (pos[0]-frame_w*0.5, pos[1]-frame_h*0.5),(pos[0]-frame_w*0.5-(vars_2.disp_w*0.5-witch_frame_h*0.5),
									witch_frame_list[vars_2.tries][1]+(pos[1]-frame_h*0.5-vars_2.disp_h*0.4-witch_frame_h*0.5), frame_w, frame_h))
				self.surface.blit(vars_2.img_ingame_pop, (pos[0] - frame_w * 0.5, pos[1] - frame_h * 0.5), frame_list[self.frame])
				self.frame += 1

				vars_2.pg.display.update()
				vars_2.clock.tick(20)

		elif vars_2.tries == 0:
			pos = (505, 315)
			while self.frame < self.num_frames:
				self.surface.blit(vars_2.img_ingame_witch_bg, (pos[0] - frame_w * 0.5, pos[1] - frame_h * 0.5), (pos[0], pos[1], frame_w, frame_h))
				self.surface.blit(vars_2.img_ingame_witch, (pos[0]-frame_w*0.5, pos[1]-frame_h*0.5),(pos[0]-frame_w*0.5-(vars_2.disp_w*0.5-witch_frame_h*0.5),
									witch_frame_list[vars_2.tries][1]+(pos[1]-frame_h*0.5-vars_2.disp_h*0.4-witch_frame_h*0.5), frame_w, frame_h))
				self.surface.blit(vars_2.img_ingame_pop, (pos[0] - frame_w * 0.5, pos[1] - frame_h * 0.5), frame_list[self.frame])
				self.frame += 1

				vars_2.pg.display.update()
				vars_2.clock.tick(20)

	def anim_scratch(self, letter):
		'''It executes the scratching over the letters in the game'''

		# Coords list of the char that equals the letter key_down
		pos_index_list = [vars_2.letter_pos[index] for index, char in enumerate(vars_2.char_list) if char == letter]

		# Removes the guessed char from 'removable_char_list'
		[vars_2.removable_char_list.remove(char) for char in vars_2.char_list if char == letter]
		vars_2.letters_guessed = list(set(vars_2.char_list) - set(vars_2.removable_char_list))

		underlines_rect = self.img_anim.get_rect()
		frame_w, frame_h = underlines_rect.width, underlines_rect.height / self.num_frames
		frame_list = list([(0, frame_h * frame, frame_w, frame_h) for frame in range(self.num_frames)])

		for pos in pos_index_list:                  # 'pos' are the coords of each letter
			self.frame = 0
			Sound.play_sound(snd_ingame_scratch)
			while self.frame < self.num_frames:

				# Instead of blitting the whole bg, it blits a crop of the size and position of each letter
				self.surface.blit(vars_2.img_ingame_witch_bg, pos, (pos[0], pos[1], frame_w, frame_h))

				# Blitting the letters independently
				text_object(self.surface, letter, pos=(pos[0]+16, pos[1]+25))

				# Blitting the scratch_animation itself, also independently
				self.surface.blit(vars_2.img_ingame_scratch, pos, frame_list[self.frame])
				self.frame += 1

				vars_2.pg.display.update()
				vars_2.clock.tick(15)

	def anim_or_not(self):
		'''It displays the 'or not...' message at the end of the game over screen'''

		or_not_rect = self.img_anim.get_rect()
		frame_w, frame_h = or_not_rect.width, int(or_not_rect.height/self.num_frames)
		frame_list = list([(0, frame_h*frame, frame_w, frame_h) for frame in range(self.num_frames)])

		while self.frame < self.num_frames:
			self.surface.blit(self.img_anim, (vars_2.disp_w*0.5-frame_w*0.5, vars_2.disp_h*0.5-frame_h*0.5), frame_list[self.frame])
			self.frame += 1

			vars_2.pg.display.update()
			vars_2.clock.tick(5)

# Animations #
anim_menu_title = Anim(vars_2.screen, img_anim=vars_2.img_menu_bg)
anim_ingame_boards = Anim(surface=vars_2.screen, img_anim=vars_2.img_ingame_bg_board, num_frames=6)
anim_scroll_music_but = Anim(vars_2.screen, img_anim=vars_2.img_scroll_but_sound, num_frames=5)
anim_scroll_sound_but = Anim(vars_2.screen, img_anim=vars_2.img_scroll_but_sound, num_frames=5)
anim_scratch = Anim(surface=vars_2.screen, img_anim=vars_2.img_ingame_scratch, num_frames=13)
