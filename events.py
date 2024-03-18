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
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_SPACE:
            vars.tries -= 1

        if any(pg.key.name(event.key) in sublist for sublist in vars.dif_rare):
            if pg.key.name(event.key) in vars.word:
                print("key:", pg.key.name(event.key))
                for letter in vars.letters_properties:
                    if letter["letter"] == pg.key.name(event.key):
                        letter["guessed"] = True
                        ng.update()
                # covers_instance.f_covers(pg.key.name(event.key))
                # if len(vars.removable_char_list) == 0:
                #     pg.mixer_music.stop()
                #     won()
            else:                                                            # if not in 'vars.char_list'
                vars.tries -= 1
                # pop_instance = Anim(vars.screen, vars.img_ingame_pop, num_frames=7)
                # pop_instance.anim_pop()
                # if vars.tries <= 0:
                #     playing = False
