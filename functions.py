import pygame as pg
import variables as v

def update_components():
    v.comps.buttons["inmenu"]["resume"].fn = resume_game
    v.comps.buttons["inmenu"]["new"].fn = new_game
    v.comps.buttons["inmenu"]["music"].fn = toggle_music
    v.comps.buttons["inmenu"]["sound"].fn = toggle_sound
    v.comps.buttons["inmenu"]["main"].fn = goto_main_menu

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

def click(fn):
	def wrapper():
		v.media.sounds["btn_click"].play()
		return fn()
	return wrapper

@click
def resume_game():
    v.ingame_menu.opened = False

@click
def new_game():
	pass

@click
def toggle_music():
	'''It enables or disables the music'''

	if v.music_on:
		v.comps.animations["inmenu_toggle_music"].start_anim()
		v.music_on = False
		pg.mixer.music.set_volume(1)
	else:
		v.comps.animations["inmenu_toggle_music"].start_anim(mode="descend")
		v.music_on = True
		pg.mixer.music.set_volume(0)

@click
def toggle_sound():
	'''It enables or disables the sound'''

	if v.sound_on:
		v.comps.animations["inmenu_toggle_sound"].start_anim()
		v.sound_on = False
		for snd in v.media.sounds.values():
			snd.set_volume(0)
	else:
		v.comps.animations["inmenu_toggle_sound"].start_anim(mode="descend")
		v.sound_on = True
		for snd in v.media.sounds.values():
			snd.set_volume(1)

@click
def goto_main_menu():
    pass
