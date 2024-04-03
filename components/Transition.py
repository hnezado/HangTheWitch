class Transition:
    def __init__(self, disp, images, type, speed=10):
        self.disp = disp
        self.image = images["fade_full"]
        self.opacity = 0
        self.type = type        # Transition type ("fade", "slide")
        self.mode = None        # Transition mode ("in" or "out")
        self.speed = speed
        self.transition_in_progress = False
        self.fn = None
        self.target = None
        self.full_display = False
        self.fn_ready = False

    def update(self):
        """Updates the transition attributes while is in progress"""
        if self.type == "fade":
            if self.mode == "in":
                self.opacity += self.speed
                if self.opacity < 255:
                    self.image.img.set_alpha(self.opacity)
                else:
                    self.opacity = 255
                    self.image.img.set_alpha(self.opacity)
                    if self.full_display:
                        self.full_display = False
                        self.fn_ready = True
                        self.mode = "out"
                    self.full_display = True
            elif self.mode == "out":
                self.opacity -= self.speed
                if self.opacity >= 0:
                    self.image.img.set_alpha(self.opacity)
                else:
                    self.opacity = 0
                    self.image.img.set_alpha(self.opacity)
                    self.transition_in_progress = False

    def start(self, **kwargs):
        """Starts the transition"""
        try:
            self.fn = kwargs["fn"]
            self.target = kwargs["to"]
        except KeyError:
            raise "Transition function and/or target not provided"

        self.transition_in_progress = True
        if self.type == "fade":
            self.mode = "in"

    def display(self):
        if self.transition_in_progress:
            self.update()
            self.disp.scr.blit(self.image.img, (0, 0))
            if self.fn_ready:
                print("fn()")
                self.fn_ready = False
                self.fn(self.target)
