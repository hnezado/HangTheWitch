import pygame as pg
import variables as vars
import functions as fn
import engine as ng

# ONLY main.py must import this module

def event_manager():
    """Recovers the events and handles them individually"""
    for event in pg.event.get():
        event_handler(event)
        ng.update()


def event_handler(event):
    """Handles any event"""
    
    if event.type == pg.QUIT:
        fn.f_quit()
    
    # TESTING
    # if event.type == pg.KEYDOWN:
    #     if event.key == pg.K_ESCAPE:
    #         vars.popup = "ingame_menu"
            
    #     if event.key == pg.K_SPACE:
    #         vars.game.tries -= 1
        
        

    #     if any(pg.key.name(event.key) in sublist for sublist in vars.word.letters_rarity):
    #         if pg.key.name(event.key) in vars.game.word:
    #             print("key:", pg.key.name(event.key))
    #             for letter in vars.letters_properties:
    #                 if letter["letter"] == pg.key.name(event.key):
    #                     letter["guessed"] = True
    #                     ng.update()
    #             # covers_instance.f_covers(pg.key.name(event.key))
    #             # if len(vars.removable_char_list) == 0:
    #             #     pg.mixer_music.stop()
    #             #     won()
    #         else:                                                            # if not in 'vars.char_list'
    #             vars.game.tries -= 1
    #             # pop_instance = Anim(vars.screen, vars.img_ingame_pop, num_frames=7)
    #             # pop_instance.anim_pop()
    #             # if vars.tries <= 0:
    #             #     playing = False
    
    if vars.popup:
        pass
    else:
        if vars.active_win == "game":
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    vars.ingame_menu.opened = not vars.ingame_menu.opened
                
                # DEBUG - Generates word by difficulty with num-pad numbers
                kp = [pg.K_KP1, pg.K_KP2, pg.K_KP3, pg.K_KP4, pg.K_KP5, pg.K_KP6, pg.K_KP7, pg.K_KP8, pg.K_KP9, pg.K_KP0]
                for i in range(1, 11):
                    if event.key == kp[i-1]:
                        vars.game.new_game(i)
                
            if vars.ingame_menu.opened:
                if event.type == pg.MOUSEBUTTONDOWN:
                    if pg.Rect(vars.animations["scroll_music_toggle"].rect).collidepoint(event.pos):
                        if vars.music_on:
                            print("toggle_music", vars.music_on)
                            vars.animations["scroll_music_toggle"].start_anim()
                            vars.music_on = False
                        else:
                            print("toggle_sound", vars.sound_on)
                            vars.animations["scroll_music_toggle"].start_anim(mode="descend")
                            vars.music_on = True
                    elif pg.Rect(vars.animations["scroll_sound_toggle"].rect).collidepoint(event.pos):
                        if vars.sound_on:
                            vars.animations["scroll_sound_toggle"].start_anim()
                            vars.sound_on = False
                        else:
                            vars.animations["scroll_sound_toggle"].start_anim(mode="descend")
                            vars.sound_on = True
            else:
                if event.type == pg.MOUSEBUTTONDOWN:
                    if pg.Rect(vars.buttons["ingame_menu"].inact_rectangle).collidepoint(event.pos):
                        vars.ingame_menu.opened = True

