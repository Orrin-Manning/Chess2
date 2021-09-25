import chess
import numpy as np

# for file in range(8):
#     for rank in range(8):
#         knight = chess.Knight(np.array([3,3]), 'white')
#         try:
#             knight.move(np.array([file, rank]))
#         except chess.InvalidMove:
#             pass
# 
# for file in range(8):
#     for rank in range(8):
#         bishop = chess.Bishop(np.array([2,0]), 'white')
#         try:
#             bishop.move(np.array([file, rank]))
#         except chess.InvalidMove:
#             pass

board = chess.Board()
board.board[0][0] = chess.Knight(np.array([0,0]), 'white')
board.move([0,0], [1,2])
print(np.array2string(board.board))
