import pygame as pg
import variables as v
import functions as fn


# ONLY main.py must import this module
def event_manager() -> None:
    """Recovers the events and handles them individually"""
    for event in pg.event.get():
        event_handler(event)


def event_handler(event) -> None:
    """Handles any event"""
    if event.type == pg.QUIT:
        pg.quit()
        quit()
    if any([popup.opened for popup in v.popups.values()]):
        for popup in v.popups.values():
            if popup.opened:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        popup.accept_btn.fn()
                    if event.key == pg.K_ESCAPE:
                        popup.cancel_btn.fn()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if pg.Rect(popup.accept_btn.inact_rect).collidepoint(event.pos):
                        popup.accept_btn.fn()
                    if pg.Rect(popup.cancel_btn.inact_rect).collidepoint(event.pos):
                        popup.cancel_btn.fn()
    else:
        if v.ingame_menu.opened:
            if v.active_win in ["dif", "game"]:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        fn.resume_game()
                if event.type == pg.MOUSEBUTTONDOWN:
                    for btn in v.comps.buttons["inmenu"].values():
                        if pg.Rect(btn.inact_rect).collidepoint(event.pos):
                            btn.fn()
            else:
                fn.resume_game()
        else:
            if v.active_win == "intro":
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        v.active_win = "main_menu"
            elif v.active_win == "main_menu":
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        v.popups["quit_confirm"].opened = True
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
                            btn.fn(dif=int(btn.text))
            elif v.active_win == "game":
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        fn.open_menu()
                    if not v.game.is_victory and not v.game.is_gameover:
                        v.game.word.event_check_letter(pushed_letter=pg.key.name(event.key),
                                                       success=v.game.success_guess, fail=v.game.failed_guess)
                if event.type == pg.MOUSEBUTTONDOWN:
                    for btn in v.comps.buttons["game"].values():
                        if pg.Rect(btn.inact_rect).collidepoint(event.pos):
                            btn.fn()
