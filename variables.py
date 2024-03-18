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
gallow = None
letters = None

# Constants
dif_rare = [['e', 't', 'a', 'o'], ['i', 'n', 's', 'h', 'r', 'd', 'l'], ['c', 'u', 'm', 'w', 'f'], ['g', 'y', 'p', 'b', 'v', 'k'], ['j', 'x', 'q', 'z']]

# Other
music_on, sound_on = True, True
active_win = "game"
current_game = False
word = "pruebas"
letters_properties = []
tries = 0
