import pygame as pg

class Image:
    def __init__(self, path, number_of_frames=1, frames_direction="down") -> None:
        self.img = pg.image.load(path)
        self.num_frames = number_of_frames
        self.frames_direction = frames_direction
        self.w, self.h = self.get_single_frame_dim() # Refers to frame dimensions
        self.frames = self.get_frames_rects()

    def get_single_frame_dim(self) -> list:
        img_rect = self.img.get_rect()
        if self.frames_direction in ["down", "up"]:
            frame_w = img_rect.w
            frame_h = img_rect.h / self.num_frames
        elif self.frames_direction in ["right", "left"]:
            frame_w = img_rect.w / self.num_frames
            frame_h = img_rect.h
        return frame_w, frame_h

    def get_frames_rects(self) -> list:
        if self.frames_direction in ["down", "up"]:
            frames_rects = [
                (0, self.h * frame, self.w, self.h) for frame in range(self.num_frames)
            ]
        elif self.frames_direction in ["right", "left"]:
            frames_rects = [
                (self.w * frame, 0, self.w, self.h) for frame in range(self.num_frames)
            ]
        if self.frames_direction in ["up", "left"]:
            frames_rects = reversed(frames_rects)
        return frames_rects
