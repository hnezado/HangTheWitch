import math
from random_words import RandomWords
from components.Letter import Letter

class Word:
    def __init__(self, disp, letter_conf, difficulty) -> None:
        self.disp = disp
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
        self.word = "estoesunapalabramuylarga"
        # self.word = "prueba"
        # self.word = self.generate_word()
        self.letters = []
        self.parse_word()
        self.calculate_letter_pos()

    def generate_word(self):
        """Generates a random word that meets predefined criteria for word difficulty.
    
            This function continuously creates a random word and checks its length and letter rarity against specified conditions, iterating until all conditions are satisfied.
            
            Returns:
                str: A randomly generated word that conforms to the preset word difficulty criteria.
        """
        
        while True:
            min_letter = 3
            max_letter = min_letter + math.ceil(self.difficulty*1.5)
            word = ""
            if self.difficulty > 8: # dif (9, 10)
                word = self.rw.random_word(min_letter_count=min_letter)
            elif self.difficulty > 2: # dif (7, 8)
                word = self.rw.random_word(min_letter_count=min_letter)
            elif self.difficulty > 2: # dif (5, 6)
                word = self.rw.random_word(min_letter_count=min_letter)
            elif self.difficulty > 2: # dif (3, 4)
                word = self.rw.random_word(min_letter_count=min_letter)
            else: # dif (1, 2)
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
                    if (weight >= len(word)/3):
                        selected_group = group_num
                if not selected_group:
                    selected_group = max(letter_dif_count, key=letter_dif_count.get)
                dif = (selected_group + 1) * 2
                if self.difficulty in (dif-1, dif):
                    break
        return word

    def parse_word(self):
        """Extracts properties of the individual letters from a random word.

            Returns:
                dict: A dictionary containing properties of each letter, including:
                    - "letter": The letter itself (string).
                    - "guessed": A boolean indicating whether the letter has been guessed.
        """
        for letter_str in self.word:
            letter = Letter(disp=self.disp, txt=letter_str)
            # self.word_width += letter.text_surf.rect.w + self.letter_conf["gap"]
            self.letters.append(letter)

    def calculate_letter_pos(self):
        letter_w = self.letter_conf["dim"]["w"]
        gap = self.letter_conf["gap"]
        # word_w = sum([l.text_surf.w for l in self.letters])
        word_w = sum([letter_w for _ in self.letters])
        print("word_w:", word_w)
        initial_pos = (self.disp.w * 0.5 - word_w * 0.5, self.disp.h * 0.78)
        print("initial_pos:", initial_pos)
        for letter_index, letter in enumerate(self.letters):
            # pos = (initial_pos[0] + letter_w * letter_index, initial_pos[1])
            pos = (initial_pos[0] + (letter_w * letter_index), initial_pos[1])
            # pos = (0, 0)
            letter.text_surf.rect.center = pos
            # letter.text_surf.get_rect_centered()

    def display(self):
        for letter in self.letters:
            # print(f'ancho de {letter.txt}: {letter.text_surf.w}')
            letter.text_surf.display()
