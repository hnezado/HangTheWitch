import os
import pygame as pg

# General
pg.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
clock = pg.time.Clock()
ticks = 30
config = {}
disp = {}

media = None

# Media
fonts = {}
images = {}
sounds = {}
music = {}

# Components
buttons = {}
animations = {}
game = None
ingame_menu = None
popup_verify = None

# Other
active_win = "game"
popup = ""
bg_faded = False
music_on, sound_on = True, True
