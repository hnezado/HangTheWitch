from components.Image import Image


class Transition:
    def __init__(self, disp, image, type, sound=None, speed=10):
        self.disp = disp
        self.image = image
        self.sound = sound
        self.type = type  # Transition type ("fade", "slide")
        self.mode = None  # Transition mode ("in" or "out")
        self.speed = speed

        # Delay to ensure updating screen before calling wrapped function
        self.fn_counter = 0
        self.fn = None
        self.target = None
        self.fn_ready = False

        # Delay to ensure a smooth element change in the background
        # (goto_element is called while transition is still displaying)
        self.end_counter = 0
        self.transition_in_progress = False

        # Fade
        self.opacity = 0

        # Slide
        self.crops = self.generate_crops() if self.type == "slide" else []
        self.crops_pos = None
        self.current_crop = 0

        self.reset()

    def reset(self):
        self.fn_counter = 0
        self.opacity = 0
        self.crops_pos = self.generate_crops_pos() if self.type == "slide" else []
        self.current_crop = 0
        self.end_counter = 0

    def generate_crops(self):
        crops = []
        for _ in range(len(self.image.frames)):
            img = Image(path=self.image.path, number_of_frames=6)
            crops.append(img)
        return crops

    def generate_crops_pos(self):
        crops_pos = []
        for ind, crop in enumerate(self.crops):
            if ind % 2 == 0:
                pos = [- crop.w, crop.h * ind]
            else:
                pos = [crop.w, crop.h * ind]
            crops_pos.append(pos)
        return crops_pos

    def update(self):
        """Updates the transition attributes while is in progress"""
        if self.end_counter == 0:
            if self.type == "fade":
                if self.mode == "in":
                    self.opacity += self.speed
                    if self.opacity < 255:
                        self.image.img.set_alpha(self.opacity)
                    else:
                        self.opacity = 255
                        self.image.img.set_alpha(self.opacity)
                        self.call_fn()
                elif self.mode == "out":
                    self.opacity -= self.speed
                    if self.opacity >= 0:
                        self.image.img.set_alpha(self.opacity)
                    else:
                        self.opacity = 0
                        self.image.img.set_alpha(self.opacity)
                        self.end_counter += 1
            elif self.type == "slide":
                if self.mode == "in":
                    if self.current_crop % 2 == 0:
                        self.displace(towards="right")
                    else:
                        self.displace(towards="left")
        else:
            if self.end_counter > 0:
                self.reset()
                self.transition_in_progress = False

    def call_fn(self) -> None:
        """Checks if the function must be called in the next loop"""
        self.fn_counter += 1
        if self.type == "fade":
            if self.fn_counter > 1:
                self.mode = "out"
                self.fn_ready = True
        elif self.type == "slide":
            if self.fn_counter > 1:
                self.fn_ready = True
                self.end_counter += 1

    def displace(self, towards):
        if towards == "right":
            if self.crops_pos[self.current_crop][0] == 0:
                self.next_current_crop()
            else:
                self.crops_pos[self.current_crop][0] += self.speed
                if self.crops_pos[self.current_crop][0] > 0:
                    self.crops_pos[self.current_crop][0] = 0
        elif towards == "left":
            if self.crops_pos[self.current_crop][0] == 0:
                self.next_current_crop()
            else:
                self.crops_pos[self.current_crop][0] -= self.speed
                if self.crops_pos[self.current_crop][0] < 0:
                    self.crops_pos[self.current_crop][0] = 0

    def next_current_crop(self):
        self.current_crop += 1
        if self.current_crop > len(self.crops) - 1:
            self.current_crop = 0
            self.call_fn()

    def start(self, **kwargs):
        """Starts the transition"""
        try:
            self.fn = kwargs["fn"]
            self.target = kwargs["to"]
        except KeyError:
            raise "Transition function and/or target not provided"

        self.transition_in_progress = True
        self.mode = "in"

        if self.type == "slide":
            self.sound.play()

    def display(self):
        if self.transition_in_progress:
            self.update()
            if self.type == "fade":
                self.disp.scr.blit(self.image.img, (0, 0))
            elif self.type == "slide":
                for ind, crop in enumerate(self.crops):
                    self.disp.scr.blit(
                        crop.img,
                        self.crops_pos[ind],
                        self.image.frames[ind]
                    )
            if self.fn_ready:
                self.fn_ready = False
                self.fn(self.target)
