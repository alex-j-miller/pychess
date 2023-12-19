import pygame

from classes.piece import Piece

class Queen(Piece):
    def __init__(self, pos, color, board):
        super().__init__(pos, color, board)
        img_path = f'images/{color[0]}q.svg'
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))
        self.notation = 'Q'
    
    def get_possible_moves(self, board):
        output= []

        moves_n = []
        for y in range(self.y)[::-1]:
            moves_n.append(board.get_square_from_pos(
                (self.x, y)
            ))
        output.append(moves_n)

        moves_ne = []
        for i in range(1, 8):
            if self.x + i > 7 or self.y - i < 0:
                break
            moves_ne.append(board.get_square_from_pos(
                (self.x + i, self.y - i)
            ))
        output.append(moves_ne)

        moves_e = []
        for x in range(self.x + 1, 8):
            moves_e.append(board.get_square_from_pos(
                (x, self.y)
            ))
        output.append(moves_e)

        moves_se = []
        for i in range(1, 8):
            if self.x + i > 7 or self.y + i > 7:
                break
            moves_se.append(board.get_square_from_pos(
                (self.x + i, self.y + i)
            ))
        output.append(moves_se)

        moves_s = []
        for y in range(self.y + 1, 8):
            moves_s.append(board.get_square_from_pos(
                (self.x, y)
            ))
        output.append(moves_s)

        moves_sw = []
        for i in range(1, 8):
            if self.x - i < 0 or self.y + i > 7:
                break
            moves_sw.append(board.get_square_from_pos(
                (self.x - i, self.y + i)
            ))
        output.append(moves_sw)

        moves_w = []
        for x in range(self.x)[::-1]:
            moves_w.append(board.get_square_from_pos(
                (x, self.y)
            ))
        output.append(moves_w)

        moves_nw = []
        for i in range(1, 8):
            if self.x - i < 0 or self.y - i < 0:
                break
            moves_nw.append(board.get_square_from_pos(
                (self.x - i, self.y - i)
            ))
        output.append(moves_nw)
        
        return output