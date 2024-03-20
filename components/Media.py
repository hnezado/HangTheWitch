import pygame as pg
from components.Image import Image

class Media:
    def __init__(self) -> None:
        self.fonts = {}
        self.images = {}
        self.sounds = {}
        self.musics = {}

    def add_font(self, name, path, size, emphasis=None):
        self.fonts[name] = pg.font.Font(path, size)
        if emphasis == "bold":
            self.fonts[name].set_bold(True)

    def add_image(self, name, path, num_frames=1, dir_frames="down"):
        self.images[name] = Image(path=path, number_of_frames=num_frames, frames_direction=dir_frames)

    def add_sound(self, name, path):
        self.sounds[name] = pg.mixer.Sound(path)

    def add_music(self, name, path):
        self.musics[name] = path
