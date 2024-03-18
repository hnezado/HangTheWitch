import pygame as pg
import os
import random as r
from random_words import RandomWords


# General #
new_game = True
dif_but_list = []
dif_num = [pg.K_1, pg.K_2, pg.K_3, pg.K_4, pg.K_5, pg.K_6, pg.K_7, pg.K_8, pg.K_9, pg.K_0]
diff_num_choice = 0
dif_len1, dif_len2 = False, False
dif_rare = [['e', 't', 'a', 'o'], ['i', 'n', 's', 'h', 'r', 'd', 'l'], ['c', 'u', 'm', 'w', 'f'], ['g', 'y', 'p', 'b', 'v', 'k'], ['j', 'x', 'q', 'z']]
dif1, dif2, dif3, dif4, dif5, dif6, dif7, dif8, dif9, dif10 = [], [], [], [], [], [], [], [], [], []
dif_all = [dif1, dif2, dif3, dif4, dif5, dif6, dif7, dif8, dif9, dif10]
# random_word = ''
# tries = 0
char_list = []
removable_char_list = []
letter_pos = []
letters_guessed = []

# Words # (Until 16 characters)
# rw = RandomWords()
words = []
