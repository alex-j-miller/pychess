import pygame

class Square:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.abs_x = x * width
        self.abs_y = y * height
        self.abs_pos = (self.abs_x, self.abs_y)
        self.pos = (self.x, self.y)

        self.color = 'light' if (x + y) % 2 == 0 else 'dark'
        self.draw_color = (223, 213, 211) if self.color == 'light' else (117, 150, 110)
        self.highlight_color = (255, 100, 100) if self.color == 'light' else (200, 100, 75)

        self.occupying_piece = None
        self.coord = self.get_coord()
        self.highlight = False
        self.rect = pygame.Rect(
            self.abs_x, 
            self.abs_y, 
            self.width, 
            self.height
        )
    
    # Gets the formal notation of the tile
    def get_coord(self):
        return 'abcdefgh'[self.x] + str(self.y + 1)

    def draw(self, display):
        # Determines the color of the tile
        if self.highlight:
            pygame.draw.rect(display, self.highlight_color, self.rect)
        else:
            pygame.draw.rect(display, self.draw_color, self.rect)
        
        # Draws the piece on the tile
        if self.occupying_piece != None:
            centering_rect = self.occupying_piece.img.get_rect()
            centering_rect.center = self.rect.center
            display.blit(self.occupying_piece.img, centering_rect.topleft)
        