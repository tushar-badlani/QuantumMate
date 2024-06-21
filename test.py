import chess
from evaluate import best_move, min_max

board = chess.Board(
    "r1bqk2r/p1p2ppp/2nbpn2/1p4N1/Q1BPP3/2N5/PP3PPP/R1B1K2R b KQkq - 1 8"
)
print(board)
print(min_max(board, 4, -float("inf"), float("inf")))