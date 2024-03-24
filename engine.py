import pygame as pg
import variables as v
from variables import media, comps
from components.MainMenu import MainMenu
from components.Dif import Dif
from components.Game import Game
from components.IngameMenu import IngameMenu
from components.Popup import Popup
from components.Text import Text
from components.Animation import Animation
from components.Button import Button
from functions import update_components, start_intro


class Disp:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.scr = None
    
    def __str__(self) -> str:
        return f'Object({self.__dict__})'

def init_vars():
    v.disp = Disp(w=v.config["disp"]["dim"]["w"], h=v.config["disp"]["dim"]["h"])
    v.disp.scr = pg.display.set_mode(size=(v.disp.w, v.disp.h))
    pg.display.set_caption(v.config["full_name"])
    pg.display.set_icon(pg.image.load(v.config["icon"]))
    
    generate_main_elements()
    generate_media()
    generate_components()
    update_main_elements()
    update_components()
    
    start_intro()

def generate_main_elements():
    v.main_menu = MainMenu(disp=v.disp)
    v.dif = Dif(disp=v.disp)
    v.game = Game(disp=v.disp)
    v.ingame_menu = IngameMenu(disp=v.disp)
    # v.pop # Este requiere varias declaraciones

def generate_media():
    # Fonts
    media.add_font(name="menu_title", path="data/fonts/feral.ttf", size=120)
    media.add_font(name="menu_btn", path="data/fonts/feral.ttf", size=30, emphasis="bold")
    media.add_font(name="ingame_tries", path="data/fonts/Haunting Attraction.ttf", size=40)
    media.add_font(name="ingame_btn", path="data/fonts/feral.ttf", size=20, emphasis="bold")
    media.add_font(name="ingame_menu_btn", path="data/fonts/parchment.ttf", size=40, emphasis="bold")
    media.add_font(name="victory", path="data/fonts/Haunting Attraction.ttf", size=60)
    media.add_font(name="gameover", path="data/fonts/Haunting Attraction.ttf", size=75)
    media.add_font(name="dif_txt", path="data/fonts/parchment.ttf", size=70)
    media.add_font(name="dif_btn", path="data/fonts/parchment.ttf", size=40)
    media.add_font(name="popup_txt", path="data/fonts/feral.ttf", size=27, emphasis="bold")
    media.add_font(name="popup_btn", path="data/fonts/feral.ttf", size=18, emphasis="bold")

    # Images
    media.add_image(name="intro_space", path="data/images/intro_space.png", num_frames=11)
    media.add_image(name="fade", path="data/images/fade.png")
    media.add_image(name="fade_full", path="data/images/fade_full.png")
    media.add_image(name="question", path="data/images/question.png")
    media.add_image(name="menu_bg", path="data/images/menu_bg.png")
    media.add_image(name="dif_scroll", path="data/images/dif_scroll.png")
    media.add_image(name="ingame_bg", path="data/images/ingame_bg.png", num_frames=6)
    media.add_image(name="ingame_gallow_bg", path="data/images/ingame_gallow_bg.png")
    media.add_image(name="ingame_gallow", path="data/images/ingame_gallow.png", num_frames=11)
    media.add_image(name="ingame_pop", path="data/images/ingame_pop.png", num_frames=7, dir_frames="right")
    media.add_image(name="ingame_scratch", path="data/images/ingame_scratch.png", num_frames=13)
    media.add_image(name="inmenu_scroll", path="data/images/inmenu_scroll.png")
    media.add_image(name="inmenu_toggle", path="data/images/inmenu_toggle.png", num_frames=5)
    media.add_image(name="gameover_brush", path="data/images/gameover_brush.png")
    media.add_image(name="gameover_ornot", path="data/images/gameover_ornot.png", num_frames=6)
    
    # Sounds & Music
    media.add_sound(name="btn_click", path="data/sounds/click.ogg")
    media.add_sound(name="menu_btn_play", path="data/sounds/rattle.ogg")
    media.add_sound(name="ingame_scratch", path="data/sounds/scratch.ogg")
    media.add_sound(name="ingame_pop", path="data/sounds/pop.ogg")
    media.add_sound(name="victory", path="data/sounds/witch_laugh.ogg")
    media.add_sound(name="gameover", path="data/sounds/gameover.ogg")
    media.add_sound(name="scroll", path="data/sounds/scroll.ogg")
    media.add_music(name="menu_wind", path="data/sounds/wind.ogg")
    media.add_music(name="ingame_music", path="data/sounds/game_music.ogg")

def generate_components():
    
    # Text Surfaces
    comps.texts["game"]["tries_remaining"] = Text(disp=v.disp, text="Remaining tries: ", font=media.fonts["ingame_tries"], pos=(v.disp.w * 0.35, v.disp.h * 0.05), fg_color=(150, 0, 0))
    comps.texts["game"]["tries"] = Text(disp=v.disp, text="NaN")
    comps.texts["popup"]["txt"] = Text(disp=v.disp.scr, text='Are you sure  ', font=media.fonts["popup_txt"], pos=(v.disp.w * 0.5, v.disp.h * 0.46))
    
    # Animations
    comps.animations["inmenu_toggle_music"] = Animation(disp=v.disp, image=media.images["inmenu_toggle"], pos=(v.disp.w*0.56, v.disp.h*0.49), anim_times=1, reset_frame=False)
    comps.animations["inmenu_toggle_sound"] = Animation(disp=v.disp, image=media.images["inmenu_toggle"], pos=(v.disp.w*0.57, v.disp.h*0.59), anim_times=1, reset_frame=False)
    
    # Buttons
    comps.buttons["main"]["play"] = Button(v.disp.scr, 200, 50, v.disp.w*0.5, v.disp.h*0.7, (130, 96, 94), (179, 104, 100), 'Play', media.fonts["menu_btn"])
    comps.buttons["main"]["quit"] = Button(v.disp.scr, 200, 50, v.disp.w*0.5, v.disp.h*0.8, (130, 96, 94), (179, 104, 100), 'Quit', media.fonts["menu_btn"])
    comps.buttons["game"]["menu"] = Button(v.disp.scr, 100, 25, v.disp.w*0.9, v.disp.h*0.05, (130, 96, 94), (179, 104, 100), 'Menu', media.fonts["ingame_btn"], act_margin=3)
    comps.buttons["game"]["gameover_play"] = Button(v.disp.scr, 200, 50, v.disp.w*0.3, v.disp.h*0.6, (130, 96, 94), (179, 104, 100), 'Play again', media.fonts["menu_btn"], act_margin=3)
    comps.buttons["game"]["gameover_menu"] = Button(v.disp.scr, 200, 50, v.disp.w*0.7, v.disp.h*0.6, (130, 96, 94), (179, 104, 100), 'Main menu', media.fonts["menu_btn"], act_margin=3)
    comps.buttons["inmenu"]["resume"] = Button(v.disp.scr, 195, 30, v.disp.w*0.5, v.disp.h*0.3, (255, 255, 255), (255, 255, 255), 'Resume game', media.fonts["ingame_menu_btn"], btn_transp=True)
    comps.buttons["inmenu"]["new"] = Button(v.disp.scr, 150, 30, v.disp.w*0.49, v.disp.h*0.4, (255, 255, 255), (255, 255, 255), 'New game', media.fonts["ingame_menu_btn"], btn_transp=True)
    comps.buttons["inmenu"]["music"] = Button(v.disp.scr, 180, 30, v.disp.w*0.52, v.disp.h*0.5, (130, 96, 94), (179, 104, 100), 'Music', media.fonts["ingame_menu_btn"], text_centered=(370, v.disp.h*0.5+15), btn_transp=True)
    comps.buttons["inmenu"]["sound"] = Button(v.disp.scr, 175, 30, v.disp.w*0.52, v.disp.h*0.6, (130, 96, 94), (179, 104, 100), 'Sound', media.fonts["ingame_menu_btn"], text_centered=(375, v.disp.h*0.6+15), btn_transp=True)
    comps.buttons["inmenu"]["main"] = Button(v.disp.scr, 150, 30, v.disp.w*0.5, v.disp.h*0.7, (255, 255, 255), (255, 255, 255), 'Main menu', media.fonts["ingame_menu_btn"], btn_transp=True)
    comps.buttons["popup"]["accept"] = Button(v.disp.scr, 150, 30, v.disp.w*0.5, v.disp.h*0.7, (255, 255, 255), (255, 255, 255), 'Accept', media.fonts["popup_btn"], btn_transp=True)
    comps.buttons["popup"]["cancel"] = Button(v.disp.scr, 150, 30, v.disp.w*0.5, v.disp.h*0.7, (255, 255, 255), (255, 255, 255), 'Cancel', media.fonts["popup_btn"], btn_transp=True)

def update_main_elements():    

    # Main Menu
    v.main_menu.update(
        images=media.images,
        buttons=comps.buttons
    )
    
    # Difficulty Menu
    v.dif.update(
        fonts=media.fonts,
        images=media.images,
        buttons=comps.buttons
    )

    # Game
    v.game.update(
        fonts=media.fonts,
        images=media.images,
        sounds=media.sounds,
        texts=comps.texts,
        buttons=comps.buttons
        )

    # Ingame Menu
    v.ingame_menu.update(
        images=media.images,
        texts=comps.texts,
        animations=comps.animations,
        buttons=comps.buttons
    )
