import pygame

from classes.piece import Piece

class Rook(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = f'images/{color[0]}r.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))
        self.notation = 'R'
    
    def get_possible_moves(self, board):
        output= []

        moves_n = []
        for y in range(self.y)[::-1]:
            moves_n.append(board.get_square_from_pos(
                (self.x, y)
            ))
        output.append(moves_n)

        moves_e = []
        for x in range(self.x + 1, 8):
            moves_e.append(board.get_square_from_pos(
                (x, self.y)
            ))
        output.append(moves_e)

        moves_s = []
        for y in range(self.y + 1, 8):
            moves_s.append(board.get_square_from_pos(
                (self.x, y)
            ))
        output.append(moves_s)

        moves_w = []
        for x in range(self.x)[::-1]:
            moves_w.append(board.get_square_from_pos(
                (x, self.y)
            ))
        output.append(moves_w)

        return output