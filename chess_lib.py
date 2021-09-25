import logging
import numpy as np

logging.basicConfig(filename='_chess.log', encoding='utf-8', level=logging.DEBUG)

class Board:
    def __init__(self):
        self._board = np.zeros([8, 8], dtype=Piece)

    @property
    def board(self):
        return self._board

    def move(self, position, destination):
        # Position and destination must not be the same
        if np.all(position==destination):
            raise InvalidMove("destination must be different from current position")
        # Destination must not contain piece of same color
        pos_piece = self.query_piece(position)
        dest_piece = self.query_piece(destination)
        if isinstance(dest_piece, Piece):
            if pos_piece.color == dest_piece.color:
                raise InvalidMove("Target square already occupied by piece of same color")
        # Move piece's location on board
        self.board[destination[0]][destination[1]] = self.board[position[0]][position[1]]
        # Free initial square
        self.board[position[0]][position[1]] = 0

    # Return piece at specified location on board
    def query_piece(self, location):
        piece = self.board[location[0]][location[1]]
        return piece

class Piece:
    def __init__(self, piece_type, position, color):
        self._piece_type = piece_type
        self._position = position
        self._color = color

    @property
    def piece_type(self):
        return self._piece_type

    @property
    def position(self):
        return self._position
    @position.setter
    def position(self, position):
        self._position = position

    @property
    def color(self):
        return self._color

    def move(self, board, destination):
        pos_s = np.array2string(self.position)
        dest_s = np.array2string(destination)
        if not self.valid_piece_move(destination):
            raise InvalidMove('Invalid ' + self.piece_type + '\'s move:' + pos_s + 'to' + dest_s)
        print(self.piece_type + pos_s + ' moved to ' + dest_s)
        self.position = destination

class Bishop(Piece):
    def __init__(self, position, color):
        Piece.__init__(self, 'Bishop', position, color)

    def valid_piece_move(self, destination):
        # check if on diagonal
        diff = destination - self.position
        diff = np.absolute(diff)
        if not (diff[0] == diff[1]):
            return False
        # TODO check for interposing pieces
        return True

class Knight(Piece):
    def __init__(self, position, color):
        Piece.__init__(self, 'Knight', position, color)

    def valid_piece_move(self, destination):
        # Compare current position with destination
        diff = destination - self.position
        diff = np.absolute(diff)
        # Check valid knight's move
        if not (all(diff==np.array([1,2])) or all(diff==np.array([2,1]))):
            return False
        return True

class InvalidMove(Exception):
    pass

class NoPieceFound(Exception):
    pass
