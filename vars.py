import pygame as pg
import os
import random as r
from random_words import RandomWords


pg.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
disp_w, disp_h = 800, 600
screen = pg.display.set_mode(size=(disp_w, disp_h))
pg.display.set_caption('hang_the_witch')
pg.display.set_icon(pg.image.load('data/icon_hang.png'))
clock = pg.time.Clock()
music_on, sound_on = True, True

# Fonts #
font_menu_title = pg.font.Font('data/feral.ttf', 120)
font_menu_but = pg.font.Font('data/feral.ttf', 30)
font_menu_but.set_bold(True)
font_ingame_tries = pg.font.Font('data/Haunting Attraction.ttf', 40)
font_ingame_but = pg.font.Font('data/feral.ttf', 20)
font_ingame_but.set_bold(True)
font_won = pg.font.Font('data/Haunting Attraction.ttf', 60)
font_gameover = pg.font.Font('data/Haunting Attraction.ttf', 75)
font_dif_txt = pg.font.Font('data/parchment.ttf', 70)
font_dif_but = pg.font.Font('data/parchment.ttf', 40)
font_scroll_menu_but = pg.font.Font('data/parchment.ttf', 40)
font_scroll_menu_but.set_bold(True)
font_verify_but = pg.font.Font('data/feral.ttf', 18)
font_verify_but.set_bold(True)
font_verify = pg.font.Font('data/feral.ttf', 27)
font_verify.set_bold(True)
font_no_words = pg.font.Font('data/feral.ttf', 18)
font_no_words.set_bold(True)

# Images #
img_menu_bg = pg.image.load('data/bg_main.png')
img_menu_space = pg.image.load('data/space.png')
img_ingame_bg_board = pg.image.load('data/boards_bg.png')
img_ingame_witch_bg = pg.image.load('data/witch_bg.png')
img_ingame_witch = pg.image.load('data/witchs.png')
img_ingame_pop = pg.image.load('data/pop.png')
img_ingame_scratch = pg.image.load('data/underlines.png')
img_gameover_brush = pg.image.load('data/brush_traces.png')
img_gameover_ornot = pg.image.load('data/or_not.png')
img_scroll_dif = pg.image.load('data/scroll_wide.png')
img_scroll_bg_fade = pg.image.load('data/fade_bg.png')
img_scroll_bg_fade_full = pg.image.load('data/fade_bg_full.png')
img_scroll_menu = pg.image.load('data/scroll.png')
img_scroll_but_sound = pg.image.load('data/button_sound.png')
img_verify_question = pg.image.load('data/question_mark.png')

# Raw sounds #
rs_but_click = pg.mixer.Sound('data/click.ogg')
rs_menu_but_play = pg.mixer.Sound('data/rattle.ogg')
rs_ingame_scratch = pg.mixer.Sound('data/scratch.ogg')
rs_ingame_pop = pg.mixer.Sound('data/pop.ogg')
rs_won = pg.mixer.Sound('data/witch_laugh.ogg')
rs_gameover = pg.mixer.Sound('data/gameover.ogg')
rs_scroll = pg.mixer.Sound('data/scroll.ogg')
raw_sounds = [rs_but_click, rs_menu_but_play, rs_ingame_scratch, rs_ingame_pop, rs_won, rs_gameover, rs_scroll]

# Raw music / bg #
rm_menu_wind = 'data/wind.ogg'
rm_ingame_music = 'data/game_music.ogg'

# General #
new_game = True
dif_but_list = []
dif_num = [pg.K_1, pg.K_2, pg.K_3, pg.K_4, pg.K_5, pg.K_6, pg.K_7, pg.K_8, pg.K_9, pg.K_0]
diff_num_choice = 0
dif_len1, dif_len2 = False, False
dif_rare = [['e', 't', 'a', 'o'], ['i', 'n', 's', 'h', 'r', 'd', 'l'], ['c', 'u', 'm', 'w', 'f'], ['g', 'y', 'p', 'b', 'v', 'k'], ['j', 'x', 'q', 'z']]
dif1, dif2, dif3, dif4, dif5, dif6, dif7, dif8, dif9, dif10 = [], [], [], [], [], [], [], [], [], []
dif_all = [dif1, dif2, dif3, dif4, dif5, dif6, dif7, dif8, dif9, dif10]
random_word = ''
tries = 0
char_list = []
removable_char_list = []
letter_pos = []
letters_guessed = []

# Words # (Until 16 characters)
rw = RandomWords()
words = ''
