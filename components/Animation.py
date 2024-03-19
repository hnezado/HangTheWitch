class Animation:
    def __init__(self, disp, image, num_frames, pos, anim_times=-1, delay=1, reset_frame=True) -> None:
        self.disp = disp
        self.image = image
        self.num_frames = num_frames    # Total number of frames in the image
        self.frame_rect = self.image.get_rect()
        self.frame_dim = {
            "w": self.frame_rect.width,
            "h": self.frame_rect.height / self.num_frames
        }
        self.pos = pos
        self.anim_times = anim_times    # Animation repetitions (-1: infinite)
        self.anim_counter = 0
        self.delay = delay              # Loops it takes to update to the next frame
        self.reset_frame = reset_frame  # Resets frame to initial frame when anim is finished
        self.frames = self.get_frames()
        self.frame = 0                  # Current frame to display
        self.rect = (pos[0], pos[1], self.frame_dim["w"], self.frame_dim["h"])
        self.next_frame_counter = 0
        self.anim_in_progress = False

    def display(self):
        self.update()
        self.disp["disp"].blit(self.image, self.pos, self.frames[self.frame])

    def get_frames(self) -> list:
        frames = []
        for i in range(self.num_frames):
            frame = [0, self.frame_dim["h"]*i, self.frame_dim["w"], self.frame_dim["h"]]
            frames.append(frame)
        print("total frames:", frames)
        return frames

    def start_anim(self, mode="ascend"):
        if mode == "ascend":
            self.frame = 0
        elif mode == "descend":
            self.frame = len(self.frames)-1
        self.next_frame_counter = 0
        self.anim_in_progress = mode

    def stop_anim(self):
        print("stopping animation")
        self.anim_in_progress = False
        self.next_frame_counter = 0

    def update(self):
        if self.anim_in_progress:
            self.next_frame_counter += 1
            print("counter:", self.next_frame_counter)
            if self.anim_in_progress == "ascend":
                if self.next_frame_counter >= self.delay:
                    if self.frame < len(self.frames)-1:
                        self.frame += 1
                        self.next_frame_counter = 0
                        print("frame (asc):", self.frame)
                    else:
                        if self.reset_frame:
                            self.frame = 0
                            print("resetting frame:", self.frame)
                        self.anim_counter += 1
                        if self.anim_counter >= self.anim_times:
                            self.stop_anim()
                
            elif self.anim_in_progress == "descend":
                if self.next_frame_counter >= self.delay:
                    if self.frame > 0:
                        self.frame -= 1
                        self.next_frame_counter = 0
                        print("frame (desc):", self.frame)
                    else:
                        if self.reset_frame:
                            self.frame = len(self.frames)-1
                            print("resetting frame:", self.frame)
                        if self.anim_counter >= self.anim_times:
                            self.stop_anim()



