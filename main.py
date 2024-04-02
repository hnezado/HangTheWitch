import json
import asyncio
import variables as v
import engine as ng
from events import event_manager


def initialize():
    
    # Loads the config file
    with open('config.json') as f:
        v.config = json.load(f)
        
    ng.init_vars()


def main():
    while True:
        event_manager()
        show_main_menu()
        show_dif()
        show_game()
        show_ingame_menu()
        show_popup()
        
        v.pg.display.update()
        v.clock.tick(v.ticks)


def show_main_menu():
    if v.active_win == "main_menu":
        v.main_menu.display()


def show_dif():
    if v.active_win == "dif":
        v.dif.display()


def show_game():
    """Shows the game window"""
    
    if v.active_win == "game":
        v.game.display()


def show_ingame_menu():
    v.ingame_menu.display()


def show_popup():
    for popup in v.popups.values():
        popup.display()


if __name__ == '__main__':
    initialize()
    asyncio.run(main())
