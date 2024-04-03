import pygame as pg
import threading
import variables as v
from components.Word import Word


### General ###
def update_components():
    v.comps.buttons["main"]["play"].fn = play
    v.comps.buttons["main"]["quit"].fn = open_popup_quit
    for btn in v.dif.dif_btns:
        btn.fn = create_new_game
    v.comps.buttons["game"]["menu"].fn = open_menu
    v.comps.buttons["game"]["gameover_play"].fn = play
    v.comps.buttons["game"]["gameover_menu"].fn = goto_main_menu
    v.comps.buttons["inmenu"]["resume"].fn = resume_game
    v.comps.buttons["inmenu"]["new"].fn = open_popup_new_game
    v.comps.buttons["inmenu"]["music"].fn = toggle_music
    v.comps.buttons["inmenu"]["sound"].fn = toggle_sound
    v.comps.buttons["inmenu"]["main"].fn = open_popup_main_menu
    v.popups["quit_confirm"].accept_btn.fn = quit
    v.popups["new_game_confirm"].accept_btn.fn = new_game
    v.popups["menu_confirm"].accept_btn.fn = goto_main_menu
    for popup in v.popups.values():
        popup.cancel_btn.fn = close_popup


def start_intro():
    v.active_win = "intro"
    pg.mixer.music.load(v.media.musics["menu_wind"])
    if v.music_on:
        pg.mixer.music.play(loops=-1, fade_ms=1000)


def fade_out_music():
    pg.mixer.music.fadeout(2000)


def play_ingame_music():
    pg.mixer.music.load(v.media.musics["ingame_music"])
    if v.music_on:
        pg.mixer.music.play(loops=-1, fade_ms=1000)


def play_menu_wind():
    pg.mixer.music.load(v.media.musics["menu_wind"])
    if v.music_on:
        pg.mixer.music.play(loops=-1, fade_ms=1000)


def goto_element(elem):
    if v.active_win != elem:
        v.active_win = elem
        for popup in v.popups.values():
            popup.close()
        v.ingame_menu.opened = False
        if elem == "main_menu":
            fade_out_music_task = threading.Thread(target=fade_out_music)
            fade_out_music_task.daemon = True
            fade_out_music_task.start()
            fade_in_music_task = threading.Thread(target=play_menu_wind)
            fade_in_music_task.daemon = True
            fade_in_music_task.start()

        elif elem == "dif":
            fade_out_music_task = threading.Thread(target=fade_out_music)
            fade_out_music_task.daemon = True
            fade_out_music_task.start()
            fade_in_music_task = threading.Thread(target=play_ingame_music)
            fade_in_music_task.daemon = True
            fade_in_music_task.start()
            v.media.sounds["scroll"].play()
        elif elem == "game":
            pass


def click(fn):
    def clicker(*args, **kwargs):
        v.media.sounds["btn_click"].play()
        return fn(*args, **kwargs)

    return clicker


### Main Menu ###
@click
def play():
    v.comps.transitions["slide"].start(fn=goto_element, to="dif")


@click
def quit():
    pg.time.delay(500)
    pg.quit()
    quit()


### Difficulty Menu ###
@click
def create_new_game(**kwargs):
    v.game.is_victory = False
    v.game.is_gameover = False
    v.game.tries = 10
    v.game.word = Word(
        disp=v.disp,
        scratch=v.media.images["ingame_scratch"],
        scratch_snd=v.media.sounds["ingame_scratch"],
        letter_conf=v.config["letter"],
        difficulty=kwargs["dif"]
    )
    goto_element("game")


### Game ###
@click
def open_menu():
    v.ingame_menu.buttons["inmenu"]["new"].enabled = v.active_win != "dif"
    v.ingame_menu.open()


@click
def close_menu():
    v.ingame_menu.open()


### Ingame Menu ###
@click
def resume_game():
    v.ingame_menu.close()


@click
def new_game():
    goto_element("dif")


@click
def toggle_music():
    """It enables or disables the music"""

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
    """It enables or disables the sound"""

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
    v.main_menu.reset_anim()
    v.comps.transitions["fade"].start(fn=goto_element, to="main_menu")


### Popups ###
@click
def open_popup_quit():
    v.popups["quit_confirm"].opened = True


@click
def open_popup_new_game():
    v.popups["new_game_confirm"].opened = True


@click
def open_popup_main_menu():
    v.popups["menu_confirm"].opened = True


@click
def close_popup():
    for popup in v.popups.values():
        popup.close()
