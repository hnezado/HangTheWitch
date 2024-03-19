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
        show_main_menu()
        show_game()
        show_menu()
        show_popup()
        
        vars.pg.display.update()
        vars.clock.tick(30)
        
def show_main_menu():
    pass

def show_game():
    """Shows the game window"""
    
    if vars.active_win == "game":
        if vars.word:
            vars.game.display()
        else: # Show difficulties menu when there is no word selected
            vars.disp["disp"].blit(vars.images["ingame_bg_board"], (0, 0))
            vars.buttons["ingame_menu"].display()
            vars.disp["disp"].blit(vars.images["scroll_dif"], (0, 0))

def show_menu():
    pass

def show_popup():
    if vars.popup == "confirmation":
        pass
    elif vars.popup == "ingame_menu":
        pass

if __name__ == '__main__':
    initialize()
    asyncio.run(main())
