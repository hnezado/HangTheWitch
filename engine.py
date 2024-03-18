import pygame as pg
import variables as vars
import functions as fn
from components.Button import Button
from components.Gallow import Gallow
from components.Letters import Letters


def init_vars():
    vars.disp["w"] = vars.config["disp"]["dim"]["w"]
    vars.disp["h"] = vars.config["disp"]["dim"]["h"]
    vars.disp["disp"] = pg.display.set_mode(size=(vars.disp["w"], vars.disp["h"]))
    pg.display.set_caption(vars.config["full_name"])
    pg.display.set_icon(pg.image.load(vars.config["icon"]))
    
    generate_media()
    generate_components()
    
    # Reset letters status and position
    vars.letters_properties = parse_word(
        disp=vars.disp, 
        word=vars.word, 
        letter_dim=vars.config["word"]["letter"]["dim"], 
        letter_gap=vars.config["word"]["letter"]["gap"]
        )

def generate_media():
    # Fonts
    vars.fonts["menu_title"] = pg.font.Font('data/feral.ttf', 120)
    vars.fonts["menu_but"] = pg.font.Font('data/feral.ttf', 30)
    vars.fonts["menu_but"].set_bold(True)
    vars.fonts["ingame_tries"] = pg.font.Font('data/Haunting Attraction.ttf', 40)
    vars.fonts["ingame_but"] = pg.font.Font('data/feral.ttf', 20)
    vars.fonts["ingame_but"].set_bold(True)
    vars.fonts["won"] = pg.font.Font('data/Haunting Attraction.ttf', 60)
    vars.fonts["gameover"] = pg.font.Font('data/Haunting Attraction.ttf', 75)
    vars.fonts["dif_txt"] = pg.font.Font('data/parchment.ttf', 70)
    vars.fonts["dif_but"] = pg.font.Font('data/parchment.ttf', 40)
    vars.fonts["scroll_menu_but"] = pg.font.Font('data/parchment.ttf', 40)
    vars.fonts["scroll_menu_but"].set_bold(True)
    vars.fonts["verify_but"] = pg.font.Font('data/feral.ttf', 18)
    vars.fonts["verify_but"].set_bold(True)
    vars.fonts["verify"] = pg.font.Font('data/feral.ttf', 27)
    vars.fonts["verify"].set_bold(True)
    vars.fonts["no_words"] = pg.font.Font('data/feral.ttf', 18)
    vars.fonts["no_words"].set_bold(True)
    
    # Images
    vars.images["menu_bg"] = pg.image.load('data/bg_main.png')
    vars.images["menu_space"] = pg.image.load('data/space.png')
    vars.images["ingame_bg_board"] = pg.image.load('data/boards_bg.png')
    vars.images["ingame_witch_bg"] = pg.image.load('data/witch_bg.png')
    vars.images["ingame_witch"] = pg.image.load('data/witches.png')
    vars.images["ingame_pop"] = pg.image.load('data/pop.png')
    vars.images["ingame_scratch"] = pg.image.load('data/underlines.png')
    vars.images["gameover_brush"] = pg.image.load('data/brush_traces.png')
    vars.images["gameover_or_not"] = pg.image.load('data/or_not.png')
    vars.images["scroll_dif"] = pg.image.load('data/scroll_wide.png')
    vars.images["scroll_bg_fade"] = pg.image.load('data/fade_bg.png')
    vars.images["scroll_bg_fade_full"] = pg.image.load('data/fade_bg_full.png')
    vars.images["scroll_menu"] = pg.image.load('data/scroll.png')
    vars.images["scroll_but_sound"] = pg.image.load('data/button_sound.png')
    vars.images["verify_question"] = pg.image.load('data/question_mark.png')
    
    # Sounds
    vars.sounds["but_click"] = pg.mixer.Sound('data/click.ogg')
    vars.sounds["menu_but_play"] = pg.mixer.Sound('data/rattle.ogg')
    vars.sounds["ingame_scratch"] = pg.mixer.Sound('data/scratch.ogg')
    vars.sounds["ingame_pop"] = pg.mixer.Sound('data/pop.ogg')
    vars.sounds["won"] = pg.mixer.Sound('data/witch_laugh.ogg')
    vars.sounds["gameover"] = pg.mixer.Sound('data/gameover.ogg')
    vars.sounds["scroll"] = pg.mixer.Sound('data/scroll.ogg')
    
    # Music
    vars.music["rm_menu_wind"] = 'data/wind.ogg'
    vars.music["rm_ingame_music"] = 'data/game_music.ogg'
    
def generate_components():    
    # Buttons    
    vars.buttons["menu_play"] = Button(vars.disp["disp"], 200, 50, vars.disp["w"]*0.5, vars.disp["h"]*0.7, (130, 96, 94), (179, 104, 100), 'Play', vars.fonts["menu_but"])
    vars.buttons["menu_quit"] = Button(vars.disp["disp"], 200, 50, vars.disp["w"]*0.5, vars.disp["h"]*0.8, (130, 96, 94), (179, 104, 100), 'Quit', vars.fonts["menu_but"])
    vars.buttons["ingame_menu"] = Button(vars.disp["disp"], 100, 25, vars.disp["w"]*0.9, vars.disp["h"]*0.05, (130, 96, 94), (179, 104, 100), 'Menu', vars.fonts["ingame_but"], act_margin=3)
    vars.buttons["gameover_play"] = Button(vars.disp["disp"], 200, 50, vars.disp["w"]*0.3, vars.disp["h"]*0.6, (130, 96, 94), (179, 104, 100), 'Play again', vars.fonts["menu_but"], act_margin=3)
    vars.buttons["gameover_menu"] = Button(vars.disp["disp"], 200, 50, vars.disp["w"]*0.7, vars.disp["h"]*0.6, (130, 96, 94), (179, 104, 100), 'Main menu', vars.fonts["menu_but"], act_margin=3)
    vars.buttons["scroll_resume"] = Button(vars.disp["disp"], 195, 30, vars.disp["w"]*0.5, vars.disp["h"]*0.3, (255, 255, 255), (255, 255, 255), 'Resume game', vars.fonts["scroll_menu_but"], but_transp=True)
    vars.buttons["scroll_new"] = Button(vars.disp["disp"], 150, 30, vars.disp["w"]*0.49, vars.disp["h"]*0.4, (255, 255, 255), (255, 255, 255), 'New game', vars.fonts["scroll_menu_but"], but_transp=True)
    vars.buttons["scroll_music"] = Button(vars.disp["disp"], 180, 30, vars.disp["w"]*0.52, vars.disp["h"]*0.5, (130, 96, 94), (179, 104, 100), 'Music', vars.fonts["scroll_menu_but"], text_centered=(370, vars.disp["h"]*0.5+15), but_transp=True)
    vars.buttons["scroll_sound"] = Button(vars.disp["disp"], 175, 30, vars.disp["w"]*0.52, vars.disp["h"]*0.6, (130, 96, 94), (179, 104, 100), 'Sound', vars.fonts["scroll_menu_but"], text_centered=(375, vars.disp["h"]*0.6+15), but_transp=True)
    vars.buttons["scroll_main"] = Button(vars.disp["disp"], 150, 30, vars.disp["w"]*0.5, vars.disp["h"]*0.7, (255, 255, 255), (255, 255, 255), 'Main menu', vars.fonts["scroll_menu_but"], but_transp=True)
    vars.buttons["verify_yes_main"] = Button(vars.disp["disp"], 80, 25, vars.disp["w"]*0.43, vars.disp["h"]*0.525, (130, 96, 94), (179, 104, 100), 'Yes', vars.fonts["verify_but"])
    vars.buttons["verify_no"] = Button(vars.disp["disp"], 80, 25, vars.disp["w"]*0.57, vars.disp["h"]*0.525, (130, 96, 94), (179, 104, 100), 'No', vars.fonts["verify_but"])
    vars.buttons["accept"] = Button(vars.disp["disp"], 80, 25, vars.disp["w"]*0.5, vars.disp["h"]*0.525, (130, 96, 94), (179, 104, 100), 'Accept', vars.fonts["verify_but"])

    vars.gallow = Gallow(surface=vars.disp["disp"], img_witch=vars.images["ingame_witch"], img_scratch=vars.images["ingame_scratch"], tries=vars.tries)
    vars.letters = Letters(surface=vars.disp["disp"], text_object_fn=fn.text_object, letters_properties=vars.letters_properties)

def update():
    vars.gallow.tries = vars.tries
    vars.letters.letters_properties = vars.letters_properties

def parse_word(disp, word, letter_dim, letter_gap) -> dict:
    """Parses the random word and gets its letters properties

    Returns:
        dict({
            "letter": String,
            "guessed": Boolean,
            "pos": List([Integer, Integer])
            })
    """
    init_pos = {
        "x": disp["w"] * 0.5 - ((((letter_dim["w"] + letter_gap) * len(word)) - letter_gap * 1.5) * 0.5),
        "y": disp["h"] * 0.7
        }
    letters_props = []
    for letter_index, letter in enumerate(word):
        pos = (init_pos["x"] + (letter_dim["w"] + letter_gap) * letter_index + letter_gap * 0.5, disp["h"] * 0.7)
        letter_props = {
            "letter": letter,
            "guessed": False,
            "pos": pos
        }
        letters_props.append(letter_props)
    
    return letters_props
