import pygame as pg
import variables as v
from components.Word import Word

def update_components():
    v.comps.buttons["main"]["play"].fn = play
    v.comps.buttons["main"]["quit"].fn = open_popup_quit
    v.comps.buttons["game"]["menu"].fn = open_menu
    v.comps.buttons["game"]["gameover_play"].fn = play
    v.comps.buttons["game"]["gameover_menu"].fn = goto_main_menu
    v.comps.buttons["inmenu"]["resume"].fn = resume_game
    v.comps.buttons["inmenu"]["new"].fn = new_game
    v.comps.buttons["inmenu"]["music"].fn = toggle_music
    v.comps.buttons["inmenu"]["sound"].fn = toggle_sound
    v.comps.buttons["inmenu"]["main"].fn = goto_main_menu
    for btn in v.dif.dif_btns:
        btn.fn = create_new_game

def start_intro():
    # v.active_win = "intro"
    v.active_win = "dif"
    print("starting screen:", v.active_win)
    pg.mixer.music.load(v.media.musics["menu_wind"])
    if v.music_on:
        pg.mixer.music.play(loops=-1, fade_ms=2000)

def goto_element(elem):
    if v.active_win != elem:
        v.active_win = elem
        print("going to:", elem)
        v.ingame_menu.opened = False
        if elem == "main_menu":
            pg.mixer.music.fadeout(2000)
            pg.mixer.music.load(v.media.musics["menu_wind"])
            if v.music_on:
                pg.mixer.music.play(loops=-1, fade_ms=2000)

        elif elem == "dif":
            pg.mixer.music.fadeout(2000)
            pg.mixer.music.load(v.media.musics["ingame_music"])
            if v.music_on:
                pg.mixer.music.play(loops=-1, fade_ms=2000)
        elif elem == "game":
            pass

def click(fn):
	def wrapper(*args, **kwargs):
		v.media.sounds["btn_click"].play()
		return fn(*args, **kwargs)
	return wrapper

@click
def play():
    print("play function")
    goto_element("dif")

@click
def open_popup_quit():
    v.popups["quit_confirm"].opened = True

@click
def quit():
    pg.time.delay(500)
    pg.quit()
    quit()

@click
def open_menu():
    v.ingame_menu.opened = True

@click
def close_menu():
    v.ingame_menu.opened = False

@click
def resume_game():
    v.ingame_menu.opened = False

@click
def new_game():
    goto_element("dif")
	# create_new_game(5)

@click
def toggle_music():
	'''It enables or disables the music'''

	if v.music_on:
		v.comps.animations["inmenu_toggle_music"].start_anim()
		v.music_on = False
		pg.mixer.music.set_volume(0)
	else:
		v.comps.animations["inmenu_toggle_music"].start_anim(mode="descend")
		v.music_on = True
		pg.mixer.music.set_volume(1)

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
    goto_element("main_menu")

@click
def create_new_game(dif):
	v.game.is_victory = False
	v.game.is_gameover = False
	v.game.tries = 10
	v.game.word = Word(
		disp=v.disp,
		scratch=v.media.images["ingame_scratch"],
		scratch_snd=v.media.sounds["ingame_scratch"],
		letter_conf=v.config["letter"],
		difficulty=dif
	)
	print("word:", v.game.word.word)
	goto_element("game")