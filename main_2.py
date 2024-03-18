from functions_2 import *

obstacle_objects = []


def initialization():
	'''It initializes the main program with the sound (no wind sound interruption between screens and it sorts the words)'''

	vars_2.words = vars_2.rw.random_words(count=100)
	f_sorting()
	if vars_2.music_on:
		Sound.play_music(snd_menu_wind)
	else:
		en_dis_music(vars_2.music_on, force_off=True)

	intro()


def intro():
	'''It initiates the Intro screen'''

	global scr

	vars_2.pg.mouse.set_visible(False)
	intro_m = True
	frame = 0
	while intro_m:
		scr = 'intro'
		for event in vars_2.pg.event.get():
			actions(event)

		anim_menu_space = Anim(surface=vars_2.screen, img_anim=vars_2.img_menu_space, num_frames=11, frame=frame)
		anim_menu_space.anim_space()
		frame += 1
		if frame == 11:
			frame = 0

		vars_2.pg.display.update()
		vars_2.clock.tick(12)


def menu():
	'''It initiates the Main Menu screen'''

	global scr

	vars_2.pg.mouse.set_visible(True)
	anim_menu_title.title_done = False
	main_m = True
	while main_m:
		scr = 'menu'
		for event in vars_2.pg.event.get():
			actions(event)

		anim_menu_title.anim_title()
		anim_menu_title.title_done = True
		but_menu_play.drawing()
		but_menu_quit.drawing()

		vars_2.pg.display.update()
		vars_2.clock.tick(30)


def diff_menu():            # Reduced the number of difficulties to half because the lack of words in the firsts levels
	'''It initiates the Difficulty Choice Scroll Menu'''

	global scr, diff_m, diff_but

	# Difficulty choice #
	diff_m = True
	while diff_m:
		scr = 'diff'
		for event in vars_2.pg.event.get():
			actions(event)

		vars_2.screen.blit(vars_2.img_ingame_bg_board, (0, 0))
		but_ingame_menu.drawing()

		# Difficulty Menu #
		diff_but = Diff()
		diff_but.diff_blit()

		vars_2.pg.display.update()
		vars_2.clock.tick(30)


def game():
	'''It starts the game instance'''

	global scr, covers_instance, playing

	while True:
		vars_2.pg.mouse.set_visible(True)
		if vars_2.music_on:
			Sound.play_music(snd_ingame_music)
		else:
			Sound.play_music(snd_ingame_music)
			en_dis_music(vars_2.music_on, force_off=True)

		# Main game loop #
		playing = True
		ingame = True
		while ingame:
			if vars_2.new_game:
				vars_2.words = vars_2.rw.random_words(count=100)
				f_sorting()
				diff_menu()
				vars_2.tries = 10
				# print(vars.random_word)
				# print(len(vars.random_word))
				# print(vars.words)
				vars_2.new_game = False
			scr = 'game'

			if playing:
				for event in vars_2.pg.event.get():
					actions(event)

			vars_2.screen.blit(vars_2.img_ingame_bg_board, (0, 0))
			vars_2.screen.blit(vars_2.img_ingame_witch_bg, (0, 0))
			text_object(vars_2.screen, 'Remaining tries: ', txt_font=vars_2.font_ingame_tries, pos=(vars_2.disp_w*0.47, vars_2.disp_h*0.07), fg_color=(150, 0, 0))
			text_object(vars_2.screen, txt='{}'.format(vars_2.tries), txt_font=vars_2.font_ingame_tries, pos=(vars_2.disp_w*0.62, vars_2.disp_h*0.07), fg_color=(150, 0, 0))
			but_ingame_menu.drawing()

			# Displaying the witch and the gallow
			witch_instance = Hang()
			witch_instance.f_witch()

			# Displaying letters #
			letters_instance = Hang(letter_num=len(vars_2.random_word))
			letters_instance.f_letters()

			# Displaying covers # # These instances need to be created after the f_randomize is called (word generated)
			covers_instance = Hang(letter_num=len(vars_2.random_word))
			covers_instance.f_covers()

			vars_2.pg.display.update()
			vars_2.clock.tick(30)

			if not playing:
				vars_2.pg.mixer_music.fadeout(300)
				game_over()
				playing = True


def won():
	'''Displays the congratulations on screen'''

	global scr

	vars_2.screen.blit(vars_2.img_scroll_bg_fade, (0, 0))
	Sound.play_sound(snd_won)
	count = 0
	while True:
		scr = 'won'
		for event in vars_2.pg.event.get():
			actions(event)

		if count >= 0:
			text_object(vars_2.screen, 'The Witch will live one more day', txt_font=vars_2.font_won, pos=(vars_2.disp_w * 0.5, vars_2.disp_h * 0.2), fg_color=(150, 50, 50))
			text_object(vars_2.screen, 'CONGRATULATIONS !', txt_font=vars_2.font_won, pos=(vars_2.disp_w * 0.5, vars_2.disp_h * 0.35), fg_color=(150, 50, 50))
			count += 1
		if count == 10:
			or_not_instance = Anim(vars_2.screen, vars_2.img_gameover_ornot, num_frames=6)
			or_not_instance.anim_or_not()

		but_gameover_play.drawing()
		but_gameover_menu.drawing()

		vars_2.pg.display.update()
		vars_2.clock.tick(5)


def game_over():
	'''Displays the game over on screen'''

	global scr

	vars_2.screen.blit(vars_2.img_scroll_bg_fade, (0, 0))
	Sound.play_sound(snd_gameover)
	opacity = 0
	vars_2.pg.time.delay(1000)
	while True:
		scr = 'gameover'
		for event in vars_2.pg.event.get():
			actions(event)

		if opacity <= 40:
			vars_2.screen.blit(vars_2.img_gameover_brush, (225, vars_2.disp_h * 0.24))
			opacity += 1
		text_object(vars_2.screen, 'The Witch Died', txt_font=vars_2.font_gameover, pos=(vars_2.disp_w * 0.5, vars_2.disp_h * 0.34), fg_color=(255, 0, 0))
		text_object(vars_2.screen, 'GAME OVER', txt_font=vars_2.font_gameover, pos=(vars_2.disp_w * 0.5, vars_2.disp_h * 0.48), fg_color=(255, 0, 0))
		but_gameover_play.drawing()
		but_gameover_menu.drawing()

		vars_2.pg.display.update()
		vars_2.clock.tick(30)


def scroll_menu():
	'''It pops up an option menu in-game'''

	global scroll_popup, scr, music_on, sound_on

	scroll_popup = True
	bg_faded = True
	while scroll_popup:
		scr = 'scroll_menu'
		for event in vars_2.pg.event.get():
			actions(event)

		# Fades out the background while menu is popping up
		if bg_faded:
			vars_2.screen.blit(vars_2.img_scroll_bg_fade, (0, 0))
			bg_faded = False

		scroll_rect = vars_2.img_scroll_menu.get_rect()
		vars_2.screen.blit(vars_2.img_scroll_menu, (vars_2.disp_w * 0.5 - scroll_rect.width * 0.5, vars_2.disp_h * 0.5 - scroll_rect.height * 0.5))
		but_scroll_resume.drawing()
		but_scroll_new.drawing()
		but_scroll_music.drawing()
		but_scroll_sound.drawing()
		but_scroll_main.drawing()
		anim_scroll_music_but.anim_music_but()
		anim_scroll_sound_but.anim_sound_but()

		vars_2.pg.display.update()
		vars_2.clock.tick(30)


def verify():
	'''It pops up a verify window on screen (Are you sure?)'''

	global scr, verify_popup

	verify_popup = True
	while verify_popup:
		scr = 'verify'
		for event in vars_2.pg.event.get():
			actions(event)

		vars_2.pg.draw.rect(vars_2.screen, (130, 96, 94), (vars_2.disp_w*0.5-110, vars_2.disp_h*0.5-50, 220, 100))
		vars_2.pg.draw.rect(vars_2.screen, (192, 138, 117), (vars_2.disp_w*0.5-105, vars_2.disp_h*0.5-45, 210, 90))
		text_object(vars_2.screen, 'Are you sure  ', vars_2.font_verify, (vars_2.disp_w*0.5, vars_2.disp_h*0.46))
		vars_2.screen.blit(vars_2.img_verify_question, (vars_2.disp_w*0.59, vars_2.disp_h*0.44))    # blit self_made question_mark due to the lack of it in the font
		but_verify_yes_main.drawing()
		but_verify_no.drawing()

		vars_2.pg.display.update()
		vars_2.clock.tick(30)


def no_words():
	'''It pops up a notification window on screen (Difficulty not available)'''

	global scr, no_words_popup

	no_words_popup = True
	while no_words_popup:
		scr = 'no_words'
		for event in vars_2.pg.event.get():
			actions(event)

		vars_2.pg.draw.rect(vars_2.screen, (130, 96, 94), (vars_2.disp_w*0.5-110, vars_2.disp_h*0.5-50, 220, 100))
		vars_2.pg.draw.rect(vars_2.screen, (192, 138, 117), (vars_2.disp_w*0.5-105, vars_2.disp_h*0.5-45, 210, 90))
		text_object(vars_2.screen, 'Difficulty not available', vars_2.font_no_words, (vars_2.disp_w*0.5, vars_2.disp_h*0.46))
		but_accept.drawing()

		vars_2.pg.display.update()
		vars_2.clock.tick(30)


def actions(event):
	'''It contains all the button commands (on-click or on-key)'''

	global scroll_popup, scr, sounds, diff_m, verify_popup, verify_yes, playing, no_words_popup

	verify_yes = False

	if event.type == vars_2.pg.QUIT:
		f_quit()

	if scr == 'intro':
		if event.type == vars_2.pg.KEYDOWN:
			if event.key == vars_2.pg.K_ESCAPE:
				f_quit()
			if event.key == vars_2.pg.K_SPACE:
				menu()

	if scr == 'menu':
		if event.type == vars_2.pg.MOUSEBUTTONDOWN and event.button == 1:
			if vars_2.pg.Rect(but_menu_play.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_menu_but_play)

				# Animation pregame #
				anim_ingame_boards.anim_boards()
				vars_2.pg.time.delay(800)
				game()
			if vars_2.pg.Rect(but_menu_quit.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_but_click)
				verify()
				if verify_yes:
					f_quit()
		if event.type == vars_2.pg.KEYDOWN:
			if event.key == vars_2.pg.K_ESCAPE:
				verify()
				if verify_yes:
					f_quit()

	if scr == 'diff':
		if event.type == vars_2.pg.MOUSEBUTTONDOWN and event.button == 1:
			if vars_2.pg.Rect(but_ingame_menu.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_scroll)
				scroll_menu()
			for button in vars_2.dif_but_list:
				if vars_2.pg.Rect(button.inact_rectangle).collidepoint(event.pos):
					vars_2.diff_num_choice = (vars_2.dif_but_list.index(button))+1
					Sound.play_sound(snd_but_click)
					try:
						diff_but.f_randomize()
						diff_m = False          # It breaks the difficulty menu loop
					except IndexError:
						no_words()
		if event.type == vars_2.pg.KEYDOWN:
			if event.key == vars_2.pg.K_ESCAPE:
				Sound.play_sound(snd_scroll)
				scroll_menu()
			if event.key in vars_2.dif_num:
				vars_2.diff_num_choice = vars_2.dif_num.index(event.key)+1
				Sound.play_sound(snd_but_click)
				try:
					diff_but.f_randomize()
					diff_m = False              # It breaks the difficulty menu loop
				except IndexError:
					no_words()

	if scr == 'game':
		if event.type == vars_2.pg.MOUSEBUTTONDOWN and event.button == 1:
			if vars_2.pg.Rect(but_ingame_menu.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_scroll)
				scroll_menu()
		if event.type == vars_2.pg.KEYDOWN:
			if event.key == vars_2.pg.K_ESCAPE:
				Sound.play_sound(snd_scroll)
				scroll_menu()
			if any(vars_2.pg.key.name(event.key) in sublist for sublist in vars_2.dif_rare):
				if vars_2.pg.key.name(event.key) in vars_2.char_list:
					covers_instance.f_covers(vars_2.pg.key.name(event.key))
					if len(vars_2.removable_char_list) == 0:
						vars_2.pg.mixer_music.stop()
						won()
				else:                                                            # if not in 'vars.char_list'
					vars_2.tries -= 1
					pop_instance = Anim(vars_2.screen, vars_2.img_ingame_pop, num_frames=7)
					pop_instance.anim_pop()
					if vars_2.tries <= 0:
						playing = False

	if scr == 'won':
		if event.type == vars_2.pg.MOUSEBUTTONDOWN and event.button == 1:
			if vars_2.pg.Rect(but_gameover_play.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_but_click)
				anim_fade_to_new_game = Anim(vars_2.screen, vars_2.img_scroll_bg_fade_full, vars_2.img_ingame_bg_board)
				anim_fade_to_new_game.anim_fade_out()
				vars_2.new_game = True
				game()
			if vars_2.pg.Rect(but_gameover_menu.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_but_click)
				anim_fade_to_menu = Anim(vars_2.screen, vars_2.img_scroll_bg_fade_full, vars_2.img_menu_bg)
				anim_fade_to_menu.anim_fade_out()
				Sound.play_music(snd_menu_wind)
				vars_2.new_game = True
				menu()

	if scr == 'gameover':
		if event.type == vars_2.pg.MOUSEBUTTONDOWN and event.button == 1:
			if vars_2.pg.Rect(but_gameover_play.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_but_click)
				anim_fade_to_new_game = Anim(vars_2.screen, vars_2.img_scroll_bg_fade_full, vars_2.img_ingame_bg_board)
				anim_fade_to_new_game.anim_fade_out()
				vars_2.new_game = True
				game()
			if vars_2.pg.Rect(but_gameover_menu.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_but_click)
				anim_fade_to_menu = Anim(vars_2.screen, vars_2.img_scroll_bg_fade_full, vars_2.img_menu_bg)
				anim_fade_to_menu.anim_fade_out()
				Sound.play_music(snd_menu_wind)
				vars_2.new_game = True
				menu()

	if scr == 'scroll_menu':
		if event.type == vars_2.pg.MOUSEBUTTONDOWN and event.button == 1:
			if vars_2.pg.Rect(but_scroll_resume.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_but_click)
				Sound.play_sound(snd_scroll)
				scroll_popup = False
			if vars_2.pg.Rect(but_scroll_new.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_but_click)
				verify()
				if verify_yes:
					anim_fade_to_new_game = Anim(vars_2.screen, vars_2.img_scroll_bg_fade_full, vars_2.img_ingame_bg_board)
					anim_fade_to_new_game.anim_fade_out()
					vars_2.new_game = True
					game()
			if vars_2.pg.Rect(but_scroll_music.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_but_click)
				en_dis_music(vars_2.music_on)                         # It enables / disables the music
				anim_scroll_music_but.switch_music = True
				anim_scroll_music_but.anim_music_but()              # It executes the music button animation
				vars_2.music_on = not vars_2.music_on                   # It switches the music_on value
			if vars_2.pg.Rect(but_scroll_sound.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_but_click)
				en_dis_sound(vars_2.sound_on)                         # It enables / disables the sound
				anim_scroll_sound_but.switch_sound = True
				anim_scroll_sound_but.anim_sound_but()              # It executes the sound button animation
				vars_2.sound_on = not vars_2.sound_on                   # It switches the sound_on value
			if vars_2.pg.Rect(but_scroll_main.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_but_click)
				verify()
				if verify_yes:
					anim_fade_to_menu = Anim(vars_2.screen, vars_2.img_scroll_bg_fade_full, vars_2.img_menu_bg)
					anim_fade_to_menu.anim_fade_out()
					Sound.play_music(snd_menu_wind)
					vars_2.new_game = True
					menu()
		if event.type == vars_2.pg.KEYDOWN and event.key == vars_2.pg.K_ESCAPE:
			Sound.play_sound(snd_scroll)
			scroll_popup = False

	if scr == 'verify':
		if event.type == vars_2.pg.MOUSEBUTTONDOWN and event.button == 1:
			if vars_2.pg.Rect(but_verify_yes_main.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_but_click)
				verify_yes = True
				verify_popup = False

			if vars_2.pg.Rect(but_verify_no.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_but_click)
				verify_popup = False
		if event.type == vars_2.pg.KEYDOWN:
			if event.key == vars_2.pg.K_ESCAPE:
				verify_popup = False

	if scr == 'no_words':
		if event.type == vars_2.pg.MOUSEBUTTONDOWN and event.button == 1:
			if vars_2.pg.Rect(but_accept.inact_rectangle).collidepoint(event.pos):
				Sound.play_sound(snd_but_click)
				no_words_popup = False
		if event.type == vars_2.pg.KEYDOWN:
			if event.key == vars_2.pg.K_ESCAPE:
				no_words_popup = False


if __name__ == '__main__':
	'''It runs the script'''

	initialization()

# siguiente proyecto, como el mini-juego de miner (one, metallica)
