from components.Text import Text

class Letter:
    def __init__(self, disp: object, txt: str) -> None:
        self.disp = disp
        self.txt = txt
        self.guessed = False
        self.text_surf = Text(disp=self.disp, text=self.txt, centered=True)

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
