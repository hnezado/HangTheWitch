import math
from random_words import RandomWords
from components.Text import Text

class Word:
    def __init__(self, difficulty) -> None:
        self.rw = RandomWords()
        self.difficulty = difficulty
        self.letters_rarity = [
            ['e', 't', 'a', 'i', 'n', 'o'],
            ['s', 'h', 'r', 'd', 'l'],
            ['u', 'c', 'm', 'f', 'w'],
            ['y', 'g', 'p', 'b', 'v'],
            ['k', 'q', 'j', 'x', 'z']
        ]

    def generate_word(self) -> None:
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

    @staticmethod
    def parse_word(disp: object, word: str) -> dict:
        """Extracts properties of the individual letters from a random word.

            Returns:
                dict: A dictionary containing properties of each letter, including:
                    - "letter": The letter itself (string).
                    - "guessed": A boolean indicating whether the letter has been guessed.
                    - "pos": A list of two integers representing the position of the letter.
        """
        letters_props = []
        for letter_index, letter in enumerate(word):
            letter_props = {
                "letter": letter,
                "guessed": False,
            }
            letters_props.append(letter_props)
        return letters_props

    @staticmethod
    def generate_letter_texts_objs(disp: object, letters_properties: list, word_config_presets: dict) -> list:
        letter_dim, letter_gap = word_config_presets["letter"].values()
        init_pos = {
            "x": disp.w * 0.5 - ((((letter_dim["w"] + letter_gap) * len(word)) - letter_gap * 1.5) * 0.5),
            "y": disp.h * 0.78
            }
        pos = (init_pos["x"] + (letter_dim["w"] + letter_gap) * letter_index + letter_gap * 0.5, disp.h * 0.5)
        # pos = (init_pos["x"] + (letter_dim["w"] + letter_gap) * letter_index + letter_gap * 0.5, init_pos["y"])
        letter_text_objects = []
        for letter_props in letters_properties:
            letter_text_objects.append(Text(disp=disp, text=letter_props["letter"], pos=pos))
        return letter_text_objects

    #     if letter in v.removable_char_list:
    #         anim_scratch.anim_scratch(letter)
    #     else:
    #         for index, char1 in enumerate(v.char_list):
    #             if len(v.removable_char_list) > 0:
                    
    #                 # If 'char1' is not guessed blit the cover
    #                 if char1 in v.removable_char_list:
    #                     self.surface.blit(v.img_ingame_scratch, v.letter_pos[index], (0, 0, 32, 50))
                        
    #                 # If 'char1' is guessed blit the underline
    #                 else:
    #                     self.surface.blit(v.img_ingame_scratch, v.letter_pos[index], (0, 600, 32, 50))
                        
    #             # If all the letters are guessed (empty removable_char_list), blit underlines
    #             else:
    #                 self.surface.blit(v.img_ingame_scratch, v.letter_pos[index], (0, 600, 32, 50))
