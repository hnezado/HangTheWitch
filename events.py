import pygame as pg
import variables as v
# import functions as fn
import engine as ng

# ONLY main.py must import this module

def event_manager():
    """Recovers the events and handles them individually"""
    for event in pg.event.get():
        event_handler(event)

def event_handler(event):
    """Handles any event"""
    
    if event.type == pg.QUIT:
        # fn.f_quit()
        pg.quit()
        quit()


    if any([popup.opened for popup in v.popups.values()]):
        pass
    else:
        if v.active_win == "game":
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    v.ingame_menu.opened = not v.ingame_menu.opened
                
                # DEBUG - Generates word by difficulty with num-pad numbers
                kp = [pg.K_KP1, pg.K_KP2, pg.K_KP3, pg.K_KP4, pg.K_KP5, pg.K_KP6, pg.K_KP7, pg.K_KP8, pg.K_KP9, pg.K_KP0]
                for i in range(1, 11):
                    if event.key == kp[i-1]:
                        v.game.new_game(i)
                
            if v.ingame_menu.opened:
                if event.type == pg.MOUSEBUTTONDOWN:
                    for btn in v.comps.buttons["inmenu"].values():
                        if pg.Rect(btn.inact_rect).collidepoint(event.pos):
                            btn.fn()
            else:
                if event.type == pg.MOUSEBUTTONDOWN:
                    if pg.Rect(v.comps.buttons["game"]["menu"].inact_rect).collidepoint(event.pos):
                        v.ingame_menu.opened = True
                if event.type == pg.KEYDOWN:
                    if any(pg.key.name(event.key) in sublist for sublist in v.game.word.letters_rarity):
                        for ind, letter in enumerate(v.game.word.letters):
                            if pg.key.name(event.key) == letter.txt:
                                if not letter.guessed:
                                    letter.guessed = True
                                    v.game.word.covers[ind].start_anim()
                                    
