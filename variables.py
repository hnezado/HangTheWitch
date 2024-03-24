import os
import pygame as pg
from components.Media import Media
from components.Components import Components

# General
pg.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
clock = pg.time.Clock()
ticks = 30
config = None
disp = None
active_win = ""
music_on, sound_on = True, True

# Main Elements
main_menu = None
dif = None
game = None
ingame_menu = None
popups = {}

# Media
media = Media()

# Components
comps = Components()
animations = {}
buttons = {}
