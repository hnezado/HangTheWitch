import pygame as pg
import variables as vars
import functions as fn
from variables import media
from components.Game import Game
from components.IngameMenu import IngameMenu
from components.Popup import Popup
from components.Button import Button
from components.Animation import Animation

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
    media.add_font(name="menu_title", path="data/fonts/feral.ttf", size=120)
    media.add_font(name="menu_btn", path="data/fonts/feral.ttf", size=30, emphasis="bold")
    media.add_font(name="ingame_tries", path="data/fonts/Haunting Attraction.ttf", size=40)
    media.add_font(name="ingame_btn", path="data/fonts/feral.ttf", size=20, emphasis="bold")
    media.add_font(name="ingame_menu_btn", path="data/fonts/parchment.ttf", size=40, emphasis="bold")
    media.add_font(name="won", path="data/fonts/Haunting Attraction.ttf", size=60)
    media.add_font(name="gameover", path="data/fonts/Haunting Attraction.ttf", size=75)
    media.add_font(name="dif_txt", path="data/fonts/parchment.ttf", size=70)
    media.add_font(name="dif_btn", path="data/fonts/parchment.ttf", size=40)
    media.add_font(name="verify_txt", path="data/fonts/feral.ttf", size=27, emphasis="bold")
    media.add_font(name="verify_btn", path="data/fonts/feral.ttf", size=18, emphasis="bold")

    # Images
    media.add_image(name="menu_bg", path="data/images/bg_main.png")
    media.add_image(name="menu_space", path="data/images/space.png")
    media.add_image(name="ingame_bg_board", path="data/images/boards_bg.png")
    media.add_image(name="ingame_witch_bg", path="data/images/witch_bg.png")
    media.add_image(name="ingame_gallows", path="data/images/gallows.png")
    media.add_image(name="ingame_pop", path="data/images/pop.png")
    media.add_image(name="ingame_scratch", path="data/images/scratch.png")
    media.add_image(name="gameover_brush", path="data/images/brush_traces.png")
    media.add_image(name="gameover_or_not", path="data/images/or_not.png")
    media.add_image(name="scroll_dif", path="data/images/scroll_wide.png")
    media.add_image(name="scroll_bg_fade", path="data/images/fade_bg.png")
    media.add_image(name="scroll_bg_fade_full", path="data/images/fade_bg_full.png")
    media.add_image(name="scroll_menu", path="data/images/scroll.png")
    media.add_image(name="scroll_but_sound", path="data/images/button_sound.png")
    media.add_image(name="verify_question", path="data/images/question_mark.png")
    
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
    vars.buttons["ingame_menu"] = Button(vars.disp["disp"], 100, 25, vars.disp["w"]*0.9, vars.disp["h"]*0.05, (130, 96, 94), (179, 104, 100), 'Menu', media.fonts["ingame_btn"], act_margin=3)
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

    # Animations
    vars.animations["scroll_music_toggle"] = Animation(disp=vars.disp, image=vars.images["scroll_but_sound"], num_frames=5, pos=(vars.disp["w"]*0.56, vars.disp["h"]*0.49), anim_times=1, reset_frame=False)
    vars.animations["scroll_sound_toggle"] = Animation(disp=vars.disp, image=vars.images["scroll_but_sound"], num_frames=5, pos=(vars.disp["w"]*0.57, vars.disp["h"]*0.59), anim_times=1, reset_frame=False)
    
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
        media=vars.media,
        images=vars.images,
        buttons= [vars.buttons["ingame_menu"]],
        word_config_presets=vars.config["word"],
        )
        
    # Ingame Menu
    vars.ingame_menu = IngameMenu(
        disp=vars.disp,
        fonts=vars.fonts,
        images=vars.images,
        buttons=vars.buttons,
        animations=vars.animations
    )
    
    # Popup
    vars.popup_verify = Popup()

def update():
    # vars.letters.letters_properties = vars.letters_properties
    pass

def new_game():
    vars.game.new_game("dif")
