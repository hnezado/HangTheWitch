from pygame import Surface, Rect, draw, SRCALPHA, mouse

class Button:
    def __init__(self, surface, width, height, x, y, i_color, a_color, text, font, enabled=True, i_font_color=(0, 0, 0),
                a_font_color=(255, 0, 0), act_margin=6, btn_transp=False, text_centered=None, fn=lambda: None):
        self.surface = surface
        self.width = width
        self.height = height
        self.x = x - self.width * 0.5  # Center of the button (width)
        self.y = y
        self.i_color = i_color
        self.a_color = a_color
        self.text = text
        self.font = font
        self.enabled = enabled
        self.i_font_color = i_font_color
        self.a_font_color = a_font_color
        self.act_margin = act_margin
        self.inact_rect = self.x, self.y, self.width, self.height
        
        # Sets default active zone margin with the option to modify it:
        self.act_rect = self.x+self.act_margin, self.y+self.act_margin, self.width-self.act_margin*2, self.height-self.act_margin*2
        self.btn_transp = btn_transp
        self.text_centered = text_centered
        self.fn = fn

    # TODO Esto hay que cambiarlo, por probablemente objetos Text()
    def text_object(self, txt, txt_font, fg_color, x, y):
        '''It renders the font with a text, text font, and text color centering it on the button by default'''

        text_surface = txt_font.render(txt, True, fg_color)
        if self.text_centered == None:
            return text_surface, text_surface.get_rect(center=(x + (self.width * 0.5), y + (self.height * 0.5) - 3))
        else:
            return text_surface, text_surface.get_rect(center=self.text_centered)

    def display(self):
        '''It draws the button with the text (text itself, text font and text color), button size and position given in the arguments'''

        if self.enabled:
            if self.btn_transp:
                surf = Surface((self.width, self.height), SRCALPHA)
                surf.fill((255, 255, 255, 0))
                self.surface.blit(surf, (self.x, self.y))
                text_surface, text_rectangle = self.text_object(self.text, self.font, self.i_font_color, self.x, self.y)
                if Rect(self.inact_rect).collidepoint(mouse.get_pos()):
                    text_surface, text_rectangle = self.text_object(self.text, self.font, self.a_font_color, self.x, self.y)
                self.surface.blit(text_surface, text_rectangle)
            else:
                draw.rect(self.surface, self.i_color, self.inact_rect)
                text_surface, text_rectangle = self.text_object(self.text, self.font, self.i_font_color, self.x, self.y)
                if Rect(self.inact_rect).collidepoint(mouse.get_pos()):
                    draw.rect(self.surface, self.a_color, self.act_rect)
                    text_surface, text_rectangle = self.text_object(self.text, self.font, self.a_font_color, self.x, self.y)
                self.surface.blit(text_surface, text_rectangle)
        else:
            draw.rect(self.surface, (150, 150, 150), self.inact_rect)
            text_surface, text_rectangle = self.text_object(self.text, self.font, (80, 80, 80), self.x, self.y)
            self.surface.blit(text_surface, text_rectangle)
