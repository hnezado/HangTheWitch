import pygame as pg
import variables as vars
import functions as fn
from components.Game import Game
from components.Popup import Popup
from components.Button import Button
from components.Word import Word


def init_vars():
    vars.disp["w"] = vars.config["disp"]["dim"]["w"]
    vars.disp["h"] = vars.config["disp"]["dim"]["h"]
    vars.disp["disp"] = pg.display.set_mode(size=(vars.disp["w"], vars.disp["h"]))
    pg.display.set_caption(vars.config["full_name"])
    pg.display.set_icon(pg.image.load(vars.config["icon"]))
    
    generate_media()
    generate_components()

def generate_media():
    # Fonts
    vars.fonts["menu_title"] = pg.font.Font('data/fonts/feral.ttf', 120)
    vars.fonts["menu_but"] = pg.font.Font('data/fonts/feral.ttf', 30)
    vars.fonts["menu_but"].set_bold(True)
    vars.fonts["ingame_tries"] = pg.font.Font('data/fonts/Haunting Attraction.ttf', 40)
    vars.fonts["ingame_but"] = pg.font.Font('data/fonts/feral.ttf', 20)
    vars.fonts["ingame_but"].set_bold(True)
    vars.fonts["won"] = pg.font.Font('data/fonts/Haunting Attraction.ttf', 60)
    vars.fonts["gameover"] = pg.font.Font('data/fonts/Haunting Attraction.ttf', 75)
    vars.fonts["dif_txt"] = pg.font.Font('data/fonts/parchment.ttf', 70)
    vars.fonts["dif_but"] = pg.font.Font('data/fonts/parchment.ttf', 40)
    vars.fonts["scroll_menu_but"] = pg.font.Font('data/fonts/parchment.ttf', 40)
    vars.fonts["scroll_menu_but"].set_bold(True)
    vars.fonts["verify_but"] = pg.font.Font('data/fonts/feral.ttf', 18)
    vars.fonts["verify_but"].set_bold(True)
    vars.fonts["verify"] = pg.font.Font('data/fonts/feral.ttf', 27)
    vars.fonts["verify"].set_bold(True)
    vars.fonts["no_words"] = pg.font.Font('data/fonts/feral.ttf', 18)
    vars.fonts["no_words"].set_bold(True)
    
    # Images
    vars.images["menu_bg"] = pg.image.load('data/images/bg_main.png')
    vars.images["menu_space"] = pg.image.load('data/images/space.png')
    vars.images["ingame_bg_board"] = pg.image.load('data/images/boards_bg.png')
    vars.images["ingame_witch_bg"] = pg.image.load('data/images/witch_bg.png')
    vars.images["ingame_gallows"] = pg.image.load('data/images/gallows.png')
    vars.images["ingame_pop"] = pg.image.load('data/images/pop.png')
    vars.images["ingame_scratch"] = pg.image.load('data/images/scratch.png')
    vars.images["gameover_brush"] = pg.image.load('data/images/brush_traces.png')
    vars.images["gameover_or_not"] = pg.image.load('data/images/or_not.png')
    vars.images["scroll_dif"] = pg.image.load('data/images/scroll_wide.png')
    vars.images["scroll_bg_fade"] = pg.image.load('data/images/fade_bg.png')
    vars.images["scroll_bg_fade_full"] = pg.image.load('data/images/fade_bg_full.png')
    vars.images["scroll_menu"] = pg.image.load('data/images/scroll.png')
    vars.images["scroll_but_sound"] = pg.image.load('data/images/button_sound.png')
    vars.images["verify_question"] = pg.image.load('data/images/question_mark.png')
    
    # Sounds
    vars.sounds["but_click"] = pg.mixer.Sound('data/sounds/click.ogg')
    vars.sounds["menu_but_play"] = pg.mixer.Sound('data/sounds/rattle.ogg')
    vars.sounds["ingame_scratch"] = pg.mixer.Sound('data/sounds/scratch.ogg')
    vars.sounds["ingame_pop"] = pg.mixer.Sound('data/sounds/pop.ogg')
    vars.sounds["won"] = pg.mixer.Sound('data/sounds/witch_laugh.ogg')
    vars.sounds["gameover"] = pg.mixer.Sound('data/sounds/gameover.ogg')
    vars.sounds["scroll"] = pg.mixer.Sound('data/sounds/scroll.ogg')
    vars.music["menu_wind"] = 'data/sounds/wind.ogg'
    vars.music["ingame_music"] = 'data/sounds/game_music.ogg'
    
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

    # Main Menu


    # Difficulty Menu
    # Reset letters status and position
    # vars.letters_properties = Dif().parse_word(disp=vars.disp, word=vars.word, letter_dim=vars.config["word"]["letter"]["dim"], letter_gap=vars.config["word"]["letter"]["gap"])
    # vars.dif_menu["number_of_difficulties"] = vars.config["dif_menu"]["number_of_difficulties"]
    # vars.dif_menu["buttons"]
    
    # vars.letters = Letters(surface=vars.disp["disp"], text_object_fn=fn.text_object, letters_properties=vars.letters_properties)
    
    # Game
    vars.game = Game(
        disp=vars.disp,
        fonts=vars.fonts,
        images=vars.images,
        word_config_presets=vars.config["word"],
        subcomponents={"buttons": [vars.buttons["ingame_menu"]]}
        )
    
    vars.word = Word(9)
    
    # Popup
    vars.popup_verify = Popup()

def update():
    # vars.letters.letters_properties = vars.letters_properties
    pass

def new_game():
    vars.game.new_game("dif")
