import pygame as pg

class Media:
    def __init__(self) -> None:
        self.fonts = {}
        self.images = {}
        self.sounds = {}
        self.musics = {}

    def add_font(self, name, path, size, emphasis):
        self.fonts[name] = pg.font.Font(path, size)
        if emphasis == "bold":
            self.fonts["name"].set_bold(True)

    def add_image(self, name, image):
        self.images[name] = image

    def add_sound(self, name, sound):
        self.sounds[name] = sound

    def add_music(self, name, music):
        self.musics[name] = music