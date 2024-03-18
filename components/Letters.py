class Letters:
    def __init__(self, surface, text_object_fn, letters_properties) -> None:
        self.surface = surface
        self.text_object = text_object_fn
        self.letters_properties = letters_properties
    
    def display_letters(self):
        '''Displays the letters behind the covers'''
            
        for letter_props in self.letters_properties:
            if letter_props["guessed"]:
                self.text_object(surface=self.surface, txt=letter_props["letter"], pos=letter_props["pos"])

    # def display_covers(self, letter=None):
    #     '''It blits the covers over the letters in-game'''

    #     if letter in vars.removable_char_list:
    #         anim_scratch.anim_scratch(letter)
    #     else:
    #         for index, char1 in enumerate(vars.char_list):
    #             if len(vars.removable_char_list) > 0:
                    
    #                 # If 'char1' is not guessed blit the cover
    #                 if char1 in vars.removable_char_list:
    #                     self.surface.blit(vars.img_ingame_scratch, vars.letter_pos[index], (0, 0, 32, 50))
                        
    #                 # If 'char1' is guessed blit the underline
    #                 else:
    #                     self.surface.blit(vars.img_ingame_scratch, vars.letter_pos[index], (0, 600, 32, 50))
                        
    #             # If all the letters are guessed (empty removable_char_list), blit underlines
    #             else:
    #                 self.surface.blit(vars.img_ingame_scratch, vars.letter_pos[index], (0, 600, 32, 50))