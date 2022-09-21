from funct import *

obstacle_objects = []


def initialization():
	'''It initializes the main program with the sound (no wind sound interruption between screens and it sorts the words)'''

	vars.words = vars.rw.random_words(count=100)
	f_sorting()
	if vars.music_on:
		Sound.play_music(snd_menu_wind)
	else:
		en_dis_music(vars.music_on, force_off=True)

	intro()


def intro():
	'''It initiates the Intro screen'''

	global scr

	vars.pg.mouse.set_visible(False)
	intro_m = True
	frame = 0
	while intro_m:
		scr = 'intro'
		for event in vars.pg.event.get():
			actions(event)

		anim_menu_space = Anim(surface=vars.screen, img_anim=vars.img_menu_space, num_frames=11, frame=frame)
		anim_menu_space.anim_space()
		frame += 1
		if frame == 11:
			frame = 0

		vars.pg.display.update()
		vars.clock.tick(12)


def menu():
	'''It initiates the Main Menu screen'''

	global scr

	vars.pg.mouse.set_visible(True)
	anim_menu_title.title_done = False
	main_m = True
	while main_m:
		scr = 'menu'
		for event in vars.pg.event.get():
			actions(event)

		anim_menu_title.anim_title()
		anim_menu_title.title_done = True
		but_menu_play.drawing()
		but_menu_quit.drawing()

		vars.pg.display.update()
		vars.clock.tick(30)


def diff_menu():            # Reduced the number of difficulties to half because the lack of words in the firsts levels
	'''It initiates the Difficulty Choice Scroll Menu'''

	global scr, diff_m, diff_but

	# Difficulty choice #
	diff_m = True
	while diff_m:
		scr = 'diff'
		for event in vars.pg.event.get():
			actions(event)

		vars.screen.blit(vars.img_ingame_bg_board, (0, 0))
		but_ingame_menu.drawing()

		# Difficulty Menu #
		diff_but = Diff()
		diff_but.diff_blit()

		vars.pg.display.update()
		vars.clock.tick(30)


def game():
	'''It starts the game instance'''

	global scr, covers_instance, playing

	while True:
		vars.pg.mouse.set_visible(True)
		if vars.music_on:
			Sound.play_music(snd_ingame_music)
		else:
			Sound.play_music(snd_ingame_music)
			en_dis_music(vars.music_on, force_off=True)

		# Main game loop #
		playing = True
		ingame = True
		while ingame:
			if vars.new_game:
				vars.words = vars.rw.random_words(count=100)
				f_sorting()
				diff_menu()
				vars.tries = 10
				# print(vars.random_word)
				# print(len(vars.random_word))
				# print(vars.words)
				vars.new_game = False
			scr = 'game'

			if playing:
				for event in vars.pg.event.get():
					actions(event)

			vars.screen.blit(vars.img_ingame_bg_board, (0, 0))
			vars.screen.blit(vars.img_ingame_witch_bg, (0, 0))
			text_object(vars.screen, 'Remaining tries: ', txt_font=vars.font_ingame_tries, pos=(vars.disp_w*0.47, vars.disp_h*0.07), fg_color=(150, 0, 0))
			text_object(vars.screen, txt='{}'.format(vars.tries), txt_font=vars.font_ingame_tries, pos=(vars.disp_w*0.62, vars.disp_h*0.07), fg_color=(150, 0, 0))
			but_ingame_menu.drawing()

			# Displaying the witch and the gallow
			witch_instance = Hang()
			witch_instance.f_witch()

			# Displaying letters #
			letters_instance = Hang(letter_num=len(vars.random_word))
			letters_instance.f_letters()

			# Displaying covers # # These instances need to be created after the f_randomize is called (word generated)
			covers_instance = Hang(letter_num=len(vars.random_word))
			covers_instance.f_covers()

			vars.pg.display.update()
			vars.clock.tick(30)

			if not playing:
				vars.pg.mixer_music.fadeout(300)
				game_over()
				playing = True


def won():
	'''Displays the congratulations on screen'''

	global scr

	vars.screen.blit(vars.img_scroll_bg_fade, (0, 0))
	Sound.play_sound(snd_won)
	count = 0
	while True:
		scr = 'won'
		for event in vars.pg.event.get():
			actions(event)

		if count >= 0:
			text_object(vars.screen, 'The Witch will live one more day', txt_font=vars.font_won, pos=(vars.disp_w * 0.5, vars.disp_h * 0.2), fg_color=(150, 50, 50))
			text_object(vars.screen, 'CONGRATULATIONS !', txt_font=vars.font_won, pos=(vars.disp_w * 0.5, vars.disp_h * 0.35), fg_color=(150, 50, 50))
			count += 1
		if count == 10:
			or_not_instance = Anim(vars.screen, vars.img_gameover_ornot, num_frames=6)
			or_not_instance.anim_or_not()

		but_gameover_play.drawing()
		but_gameover_menu.drawing()

		vars.pg.display.update()
		vars.clock.tick(5)


def game_over():
	'''Displays the game over on screen'''

	global scr

	vars.screen.blit(vars.img_scroll_bg_fade, (0, 0))
	Sound.play_sound(snd_gameover)
	opacity = 0
	vars.pg.time.delay(1000)
	while True:
		scr = 'gameover'
		for event in vars.pg.event.get():
			actions(event)

		if opacity <= 40:
			vars.screen.blit(vars.img_gameover_brush, (225, vars.disp_h * 0.24))
			opacity += 1
		text_object(vars.screen, 'The Witch Died', txt_font=vars.font_gameover, pos=(vars.disp_w * 0.5, vars.disp_h * 0.34), fg_color=(255, 0, 0))
		text_object(vars.screen, 'GAME OVER', txt_font=vars.font_gameover, pos=(vars.disp_w * 0.5, vars.disp_h * 0.48), fg_color=(255, 0, 0))
		but_gameover_play.drawing()
		but_gameover_menu.drawing()

		vars.pg.display.update()
		vars.clock.tick(30)


def scroll_menu():
	'''It pops up an option menu in-game'''

	global scroll_popup, scr, music_on, sound_on

	scroll_popup = True
	bg_faded = True
	while scroll_popup:
		scr = 'scroll_menu'
		for event in vars.pg.event.get():
			actions(event)

		# Fades out the background while menu is popping up
		if bg_faded:
			vars.screen.blit(vars.img_scroll_bg_fade, (0, 0))
			bg_faded = False

		scroll_rect = vars.img_scroll_menu.get_rect()
		vars.screen.blit(vars.img_scroll_menu, (vars.disp_w * 0.5 - scroll_rect.width * 0.5, vars.disp_h * 0.5 - scroll_rect.height * 0.5))
		but_scroll_resume.drawing()
		but_scroll_new.drawing()
		but_scroll_music.drawing()
		but_scroll_sound.drawing()
		but_scroll_main.drawing()
		anim_scroll_music_but.anim_music_but()
		anim_scroll_sound_but.anim_sound_but()

		vars.pg.display.update()
		vars.clock.tick(30)


def verify():
	'''It pops up a verify window on screen (Are you sure?)'''

	global scr, verify_popup

	verify_popup = True
	while verify_popup:
		scr = 'verify'
		for event in vars.pg.event.get():
			actions(event)

		vars.pg.draw.rect(vars.screen, (130, 96, 94), (vars.disp_w*0.5-110, vars.disp_h*0.5-50, 220, 100))
		vars.pg.draw.rect(vars.screen, (192, 138, 117), (vars.disp_w*0.5-105, vars.disp_h*0.5-45, 210, 90))
		text_object(vars.screen, 'Are you sure  ', vars.font_verify, (vars.disp_w*0.5, vars.disp_h*0.46))
		vars.screen.blit(vars.img_verify_question, (vars.disp_w*0.59, vars.disp_h*0.44))    # blit self_made question_mark due to the lack of it in the font
		but_verify_yes_main.drawing()
		but_verify_no.drawing()

		vars.pg.display.update()
		vars.clock.tick(30)


def no_words():
	'''It pops up a notification window on screen (Difficulty not available)'''

	global scr, no_words_popup

	no_words_popup = True
	while no_words_popup:
		scr = 'no_words'
		for event in vars.pg.event.get():
			actions(event)

		vars.pg.draw.rect(vars.screen, (130, 96, 94), (vars.disp_w*0.5-110, vars.disp_h*0.5-50, 220, 100))
		vars.pg.draw.rect(vars.screen, (192, 138, 117), (vars.disp_w*0.5-105, vars.disp_h*0.5-45, 210, 90))
		text_object(vars.screen, 'Difficulty not available', vars.font_no_words, (vars.disp_w*0.5, vars.disp_h*0.46))
		but_accept.drawing()

		vars.pg.display.update()
		vars.clock.tick(30)


def actions(event):
	'''It contains all the button commands (on-click or on-key)'''

	global scroll_popup, scr, sounds, diff_m, verify_popup, verify_yes, playing, no_words_popup

	verify_yes = False

	if event.type == vars.pg.QUIT:
		f_quit()

	if scr == 'intro':
		if event.type == vars.pg.KEYDOWN:
			if event.key == vars.pg.K_ESCAPE:
				f_quit()
			if event.key == vars.pg.K_SPACE:
				menu()

	if scr == 'menu':
		if event.type == vars.pg.MOUSEBUTTONDOWN and event.button == 1:
			if vars.pg.Rect(but_menu_play.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_menu_but_play)

				# Animation pregame #
				anim_ingame_boards.anim_boards()
				vars.pg.time.delay(800)
				game()
			if vars.pg.Rect(but_menu_quit.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_but_click)
				verify()
				if verify_yes:
					f_quit()
		if event.type == vars.pg.KEYDOWN:
			if event.key == vars.pg.K_ESCAPE:
				verify()
				if verify_yes:
					f_quit()

	if scr == 'diff':
		if event.type == vars.pg.MOUSEBUTTONDOWN and event.button == 1:
			if vars.pg.Rect(but_ingame_menu.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_scroll)
				scroll_menu()
			for button in vars.dif_but_list:
				if vars.pg.Rect(button.inact_rectangle).collidepoint(event.pos):
					vars.diff_num_choice = (vars.dif_but_list.index(button))+1
					Sound.play_sound(snd_but_click)
					try:
						diff_but.f_randomize()
						diff_m = False          # It breaks the difficulty menu loop
					except IndexError:
						no_words()
		if event.type == vars.pg.KEYDOWN:
			if event.key == vars.pg.K_ESCAPE:
				Sound.play_sound(snd_scroll)
				scroll_menu()
			if event.key in vars.dif_num:
				vars.diff_num_choice = vars.dif_num.index(event.key)+1
				Sound.play_sound(snd_but_click)
				try:
					diff_but.f_randomize()
					diff_m = False              # It breaks the difficulty menu loop
				except IndexError:
					no_words()

	if scr == 'game':
		if event.type == vars.pg.MOUSEBUTTONDOWN and event.button == 1:
			if vars.pg.Rect(but_ingame_menu.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_scroll)
				scroll_menu()
		if event.type == vars.pg.KEYDOWN:
			if event.key == vars.pg.K_ESCAPE:
				Sound.play_sound(snd_scroll)
				scroll_menu()
			if any(vars.pg.key.name(event.key) in sublist for sublist in vars.dif_rare):
				if vars.pg.key.name(event.key) in vars.char_list:
					covers_instance.f_covers(vars.pg.key.name(event.key))
					if len(vars.removable_char_list) == 0:
						vars.pg.mixer_music.stop()
						won()
				else:                                                            # if not in 'vars.char_list'
					vars.tries -= 1
					pop_instance = Anim(vars.screen, vars.img_ingame_pop, num_frames=7)
					pop_instance.anim_pop()
					if vars.tries <= 0:
						playing = False

	if scr == 'won':
		if event.type == vars.pg.MOUSEBUTTONDOWN and event.button == 1:
			if vars.pg.Rect(but_gameover_play.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_but_click)
				anim_fade_to_new_game = Anim(vars.screen, vars.img_scroll_bg_fade_full, vars.img_ingame_bg_board)
				anim_fade_to_new_game.anim_fade_out()
				vars.new_game = True
				game()
			if vars.pg.Rect(but_gameover_menu.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_but_click)
				anim_fade_to_menu = Anim(vars.screen, vars.img_scroll_bg_fade_full, vars.img_menu_bg)
				anim_fade_to_menu.anim_fade_out()
				Sound.play_music(snd_menu_wind)
				vars.new_game = True
				menu()

	if scr == 'gameover':
		if event.type == vars.pg.MOUSEBUTTONDOWN and event.button == 1:
			if vars.pg.Rect(but_gameover_play.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_but_click)
				anim_fade_to_new_game = Anim(vars.screen, vars.img_scroll_bg_fade_full, vars.img_ingame_bg_board)
				anim_fade_to_new_game.anim_fade_out()
				vars.new_game = True
				game()
			if vars.pg.Rect(but_gameover_menu.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_but_click)
				anim_fade_to_menu = Anim(vars.screen, vars.img_scroll_bg_fade_full, vars.img_menu_bg)
				anim_fade_to_menu.anim_fade_out()
				Sound.play_music(snd_menu_wind)
				vars.new_game = True
				menu()

	if scr == 'scroll_menu':
		if event.type == vars.pg.MOUSEBUTTONDOWN and event.button == 1:
			if vars.pg.Rect(but_scroll_resume.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_but_click)
				Sound.play_sound(snd_scroll)
				scroll_popup = False
			if vars.pg.Rect(but_scroll_new.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_but_click)
				verify()
				if verify_yes:
					anim_fade_to_new_game = Anim(vars.screen, vars.img_scroll_bg_fade_full, vars.img_ingame_bg_board)
					anim_fade_to_new_game.anim_fade_out()
					vars.new_game = True
					game()
			if vars.pg.Rect(but_scroll_music.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_but_click)
				en_dis_music(vars.music_on)                         # It enables / disables the music
				anim_scroll_music_but.switch_music = True
				anim_scroll_music_but.anim_music_but()              # It executes the music button animation
				vars.music_on = not vars.music_on                   # It switches the music_on value
			if vars.pg.Rect(but_scroll_sound.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_but_click)
				en_dis_sound(vars.sound_on)                         # It enables / disables the sound
				anim_scroll_sound_but.switch_sound = True
				anim_scroll_sound_but.anim_sound_but()              # It executes the sound button animation
				vars.sound_on = not vars.sound_on                   # It switches the sound_on value
			if vars.pg.Rect(but_scroll_main.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_but_click)
				verify()
				if verify_yes:
					anim_fade_to_menu = Anim(vars.screen, vars.img_scroll_bg_fade_full, vars.img_menu_bg)
					anim_fade_to_menu.anim_fade_out()
					Sound.play_music(snd_menu_wind)
					vars.new_game = True
					menu()
		if event.type == vars.pg.KEYDOWN and event.key == vars.pg.K_ESCAPE:
			Sound.play_sound(snd_scroll)
			scroll_popup = False

	if scr == 'verify':
		if event.type == vars.pg.MOUSEBUTTONDOWN and event.button == 1:
			if vars.pg.Rect(but_verify_yes_main.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_but_click)
				verify_yes = True
				verify_popup = False

			if vars.pg.Rect(but_verify_no.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_but_click)
				verify_popup = False
		if event.type == vars.pg.KEYDOWN:
			if event.key == vars.pg.K_ESCAPE:
				verify_popup = False

	if scr == 'no_words':
		if event.type == vars.pg.MOUSEBUTTONDOWN and event.button == 1:
			if vars.pg.Rect(but_accept.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_but_click)
				no_words_popup = False
		if event.type == vars.pg.KEYDOWN:
			if event.key == vars.pg.K_ESCAPE:
				no_words_popup = False


if __name__ == '__main__':
	'''It runs the script'''

	initialization()

# siguiente proyecto, como el mini-juego de miner (one, metallica)
