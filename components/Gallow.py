class Gallow:
    def __init__(self, surface, img_witch, img_scratch, tries):
        self.surface = surface
        self.disp_w, self.disp_h = self.surface.get_size()
        self.imgs = {
            "witch": img_witch,
            "scratch": img_scratch
        }
        self.tries = tries

    def display(self):
        '''It displays the gallow and the hanged witch'''

        witch_rect = self.imgs["witch"].get_rect()
        frame_w, frame_h = witch_rect.width, witch_rect.height / 11
        frame_list = list([(0, frame_h * frame, frame_w, frame_h) for frame in range(11)])
        frame_list.reverse()
        self.surface.blit(self.imgs["witch"], (self.disp_w*0.5-frame_w*0.5, self.disp_h*0.4-frame_h*0.5), frame_list[self.tries])
