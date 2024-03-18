import pygame as pg

def f_quit():
	pg.quit()
	quit()

def text_object(surface, txt, txt_font=None, pos=(0, 0), fg_color=(0, 0, 0)):
	'''Renders the font with a text, text font, text color and displays it in the given position'''

	if txt_font == None:
		font = pg.font.Font(txt_font, 45)
	else:
		font = txt_font
	text_surface = font.render(txt, True, fg_color)
	surface.blit(text_surface, text_surface.get_rect(center=pos))

def toggle_music(music_on, force_off=False):
	'''It enables or disables the music'''

	if music_on:
		if not force_off:
			pg.mixer.music.set_volume(0)
	else:
		pg.mixer.music.set_volume(1)
		if force_off:
			pg.mixer.music.set_volume(0)

def toggle_sound(sound_on, sounds):
	'''It enables or disables the sound'''

	if sound_on:
		for rs_sound in sounds:
			rs_sound.set_volume(0)
	else:
		for rs_sound in sounds:
			rs_sound.set_volume(1)