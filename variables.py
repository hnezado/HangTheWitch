import os
import pygame as pg

# General
pg.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
clock = pg.time.Clock()
config = {}
disp = {}

# Media
fonts = {}
images = {}
sounds = {}
music = {}

# Components
buttons = {}
game = None
popup_verify = None

# Other
active_win = "game"
popup = ""
bg_faded = False
music_on, sound_on = True, True
