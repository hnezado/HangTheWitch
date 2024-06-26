import math
from pygame import Surface
from pygame.mixer import Sound
from typing import Callable
from random_words import RandomWords
from components.Letter import Letter
from components.Animation import Animation


class Word:
    def __init__(self, disp, scratch: Surface, scratch_snd: Sound, letter_conf: dict, difficulty: int) -> None:
        self.disp = disp
        self.scratch = scratch
        self.scratch_snd = scratch_snd
        self.letter_conf = letter_conf
        self.rw = RandomWords()
        self.difficulty = difficulty
        self.letters_rarity = [
            ['e', 't', 'a', 'i', 'n', 'o'],
            ['s', 'h', 'r', 'd', 'l'],
            ['u', 'c', 'm', 'f', 'w'],
            ['y', 'g', 'p', 'b', 'v'],
            ['k', 'q', 'j', 'x', 'z']
        ]
        self.word = self.generate_word()
        self.letters = []
        self.letters_txt = []
        self.covers = []
        self.parse_word()
        self.calculate_letter_pos()
        self.generate_covers()

    def generate_word(self) -> str:
        """Generates a random word that meets predefined criteria for word difficulty.
            This function continuously creates a random word and checks its length and letter rarity against specified
            conditions, iterating until all conditions are satisfied.
            Returns:
                str: A randomly generated word that conforms to the preset word difficulty criteria.
        """
        while True:
            min_letter = 3
            max_letter = min_letter + math.ceil(self.difficulty*1.5)
            if self.difficulty > 8:     # dif (9, 10)
                word = self.rw.random_word(min_letter_count=min_letter)
            elif self.difficulty > 2:   # dif (7, 8)
                word = self.rw.random_word(min_letter_count=min_letter)
            elif self.difficulty > 2:   # dif (5, 6)
                word = self.rw.random_word(min_letter_count=min_letter)
            elif self.difficulty > 2:   # dif (3, 4)
                word = self.rw.random_word(min_letter_count=min_letter)
            else:                       # dif (1, 2)
                word = self.rw.random_word(min_letter_count=min_letter)
            
            len_ok = len(word) <= max_letter
            
            if len_ok:
                letter_dif_count = {4: 0, 3: 0, 2: 0, 1: 0, 0: 0}
                for index, rarity_gr in reversed(list(enumerate(self.letters_rarity))):
                    for letter in word:
                        if letter in rarity_gr:
                            letter_dif_count[index] += 1
                
                selected_group = None
                for group_num, weight in letter_dif_count.items():
                    if weight >= len(word) / 3:
                        selected_group = group_num
                if not selected_group:
                    selected_group = max(letter_dif_count, key=letter_dif_count.get)
                dif = (selected_group + 1) * 2
                if self.difficulty in (dif-1, dif):
                    break
        return word

    def parse_word(self) -> None:
        """Extracts properties of the individual letters from a random word.
            Returns:
                dict: A dictionary containing properties of each letter, including:
                    - "letter": The letter itself (string).
                    - "guessed": A boolean indicating whether the letter has been guessed.
        """
        for letter_str in self.word:
            letter = Letter(disp=self.disp, txt=letter_str)
            self.letters.append(letter)
            self.letters_txt.append(letter.txt)

    def calculate_letter_pos(self) -> None:
        """Calculates every letter position"""
        letter_w = self.letter_conf["dim"]["w"]
        gap = self.letter_conf["gap"]
        word_w = (letter_w + gap) * (len(self.letters) - 1)
        initial_pos = (self.disp.w * 0.5 - word_w * 0.5, self.disp.h * 0.78)
        for letter_index, letter in enumerate(self.letters):
            pos = (initial_pos[0] + (letter_w + gap) * letter_index, initial_pos[1])
            letter.text_surf.pos = pos
            
    def generate_covers(self):
        """Generates every covers Surface (image) which covers every letter"""
        for letter in self.letters:
            if not letter.guessed:
                letter_pos = letter.text_surf.pos
                img_dim = self.scratch.w, self.scratch.h
                scratch_pos = (letter_pos[0] - img_dim[0] * 0.5, letter_pos[1] - img_dim[1] * 0.5)
                self.covers.append(Animation(
                    disp=self.disp,
                    image=self.scratch,
                    pos=scratch_pos,
                    delay=2,
                    reset_frame=False)
                )

    def display(self):
        """Displays all the word letters with its covers"""
        for letter in self.letters:
            letter.text_surf.display()
        for cover in self.covers:
            cover.display()

    def event_check_letter(self, pushed_letter: str, success: Callable[[], None], fail: Callable[[], None]) -> None:
        """Checks if the pushed letter is in the generated word"""
        if any(pushed_letter in sublist for sublist in self.letters_rarity):
            if pushed_letter in self.letters_txt:
                for ind, letter in enumerate(self.letters):
                    if pushed_letter == letter.txt:
                        if not letter.guessed:
                            success(ind)
            else:
                fail()
