import json
import asyncio
import variables as vars
import functions as fn
import engine as ng
from events import event_manager


def initialize():
    
    # Loads the config file
    with open('config.json') as f:
        vars.config = json.load(f)
    
    ng.init_vars()
    ng.update()

def main():
    while True:
        event_manager()
        show_popup()
        show_ingame_menu()
        show_diff()
        show_main_menu()
        show_game()
        

def show_popup():
    pass

def show_ingame_menu():
    pass

def show_diff():
    pass

def show_main_menu():
    pass

def show_game():
    """Shows the game window"""
    
    if vars.active_win == "game":
        if not vars.current_game:
            new_game()
        
        vars.disp["disp"].blit(vars.images["ingame_bg_board"], (0, 0))
        vars.disp["disp"].blit(vars.images["ingame_witch_bg"], (0, 0))
        fn.text_object(vars.disp["disp"], 'Remaining tries: ', txt_font=vars.fonts["ingame_tries"], pos=(vars.disp["w"]*0.47, vars.disp["h"]*0.07), fg_color=(150, 0, 0))
        fn.text_object(vars.disp["disp"], txt='{}'.format(vars.tries), txt_font=vars.fonts["ingame_tries"], pos=(vars.disp["w"]*0.62, vars.disp["h"]*0.07), fg_color=(150, 0, 0))
        vars.buttons["ingame_menu"].display()
        vars.gallow.display()
        vars.letters.display_letters()

        vars.pg.display.update()
        vars.clock.tick(30)

def new_game():
    vars.tries = 10
    vars.current_game = True


if __name__ == '__main__':
    initialize()
    asyncio.run(main())
