import pygame as pg
import variables as v
import functions as fn

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
        if v.ingame_menu.opened:
            if v.active_win in ["dif", "game"]:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        fn.close_menu()
                if event.type == pg.MOUSEBUTTONDOWN:
                    for btn in v.comps.buttons["inmenu"].values():
                        if pg.Rect(btn.inact_rect).collidepoint(event.pos):
                            btn.fn()
            else:
                fn.close_menu()
        else:
            if v.active_win == "intro":
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        v.active_win = "main_menu"
            elif v.active_win == "main_menu":
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                        fn.goto_element("dif")
                if event.type == pg.MOUSEBUTTONDOWN:
                    for btn in v.comps.buttons["main"].values():
                        if pg.Rect(btn.inact_rect).collidepoint(event.pos):
                            btn.fn()
            elif v.active_win == "dif":
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        fn.open_menu()
                    if event.key == pg.K_RIGHT:
                        fn.goto_element("game")
                if event.type == pg.MOUSEBUTTONDOWN:
                    if pg.Rect(v.comps.buttons["game"]["menu"].inact_rect).collidepoint(event.pos):
                        fn.open_menu()
                    for btn in v.dif.dif_btns:
                        if pg.Rect(btn.inact_rect).collidepoint(event.pos):
                            btn.fn(int(btn.text))
            elif v.active_win == "game":
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        fn.open_menu()
                    ###################################################
                    # DEBUG - Generates word by difficulty with num-pad numbers
                    kp = [pg.K_KP1, pg.K_KP2, pg.K_KP3, pg.K_KP4, pg.K_KP5, pg.K_KP6, pg.K_KP7, pg.K_KP8, pg.K_KP9, pg.K_KP0]
                    for i in range(1, 11):
                        if event.key == kp[i-1]:
                            fn.create_new_game(i)
                    ###################################################
                    if not v.game.is_victory and not v.game.is_gameover:
                        v.game.word.event_check_letter(pushed_letter=pg.key.name(event.key), success=v.game.success_guess, fail=v.game.failed_guess)
                if event.type == pg.MOUSEBUTTONDOWN:
                        # if pg.Rect(v.comps.buttons["game"]["menu"].inact_rect).collidepoint(event.pos):
                        #     fn.open_menu()
                        for btn in v.comps.buttons["game"].values():
                            if pg.Rect(btn.inact_rect).collidepoint(event.pos):
                                btn.fn()
