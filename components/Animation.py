class Animation:
    def __init__(self, disp, image, pos, anim_times=-1, delay=1, reset_frame=True) -> None:
        self.disp = disp
        self.image = image
        self.pos = pos
        self.anim_times = anim_times    # Animation repetitions (-1: infinite)
        self.anim_counter = 0
        self.delay = delay              # Loops it takes to update to the next frame
        self.reset_frame = reset_frame  # Resets frame to initial frame when anim is finished
        self.frame = 0                  # Current frame to display
        self.rect = (pos[0], pos[1], self.image.w, self.image.h)
        self.next_frame_counter = 0
        self.anim_in_progress = False

    def display(self):
        self.update()
        self.disp.scr.blit(self.image.img, self.pos, self.image.frames[self.frame])

    def start_anim(self, mode="ascend"):
        if mode == "ascend":
            self.frame = 0
        elif mode == "descend":
            self.frame = len(self.image.frames)-1
        self.next_frame_counter = 0
        self.anim_in_progress = mode

    def stop_anim(self):
        self.anim_in_progress = False
        self.next_frame_counter = 0

    def update(self):
        if self.anim_in_progress:
            self.next_frame_counter += 1
            if self.anim_in_progress == "ascend":
                if self.next_frame_counter >= self.delay:
                    if self.frame < len(self.image.frames)-1:
                        self.frame += 1
                        self.next_frame_counter = 0
                    else:
                        if self.reset_frame:
                            self.frame = 0
                        self.anim_counter += 1
                        if self.anim_counter >= self.anim_times:
                            self.stop_anim()
                
            elif self.anim_in_progress == "descend":
                if self.next_frame_counter >= self.delay:
                    if self.frame > 0:
                        self.frame -= 1
                        self.next_frame_counter = 0
                    else:
                        if self.reset_frame:
                            self.frame = len(self.image.frames)-1
                        if self.anim_counter >= self.anim_times:
                            self.stop_anim()



