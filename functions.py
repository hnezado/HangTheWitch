import pygame as pg
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
    v.active_win = "dif"
    print("starting screen:", v.active_win)
    pg.mixer.music.load(v.media.musics["menu_wind"])
    if v.music_on:
        pg.mixer.music.play(loops=-1, fade_ms=2000)


def goto_element(elem):
    if v.active_win != elem:
        v.active_win = elem
        print("going to:", elem)
        for popup in v.popups.values():
            popup.close()
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
    def clicker(*args, **kwargs):
        v.media.sounds["btn_click"].play()
        return fn(*args, **kwargs)

    return clicker


### Main Menu ###
@click
def play(*args, **kwargs):
    goto_element("dif")


@click
def quit():
    pg.time.delay(500)
    pg.quit()
    quit()


### Difficulty Menu ###
@click
def create_new_game(*args, **kwargs):
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
    print("word:", v.game.word.word)
    goto_element("game")


### Game ###
@click
def open_menu(*args, **kwargs):
    v.ingame_menu.buttons["inmenu"]["new"].enabled = v.active_win != "dif"
    v.ingame_menu.opened = True


@click
def close_menu():
    v.ingame_menu.opened = False


### Ingame Menu ###
@click
def resume_game(*args, **kwargs):
    v.ingame_menu.opened = False


@click
def new_game(*args, **kwargs):
    print("exec new_game fn")
    goto_element("dif")


# create_new_game(5)

@click
def toggle_music(*args, **kwargs):
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
def toggle_sound(*args, **kwargs):
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
def goto_main_menu(*args, **kwargs):
    goto_element("main_menu")


### Popups ###
@click
def open_popup_quit(*args, **kwargs):
    v.popups["quit_confirm"].opened = True


@click
def open_popup_new_game(*args, **kwargs):
    v.popups["new_game_confirm"].opened = True


@click
def open_popup_main_menu(*args, **kwargs):
    v.popups["menu_confirm"].opened = True


@click
def close_popup(*args, **kwargs):
    for popup in v.popups.values():
        popup.close()
