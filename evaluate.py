import chess


piece_value = {
    chess.PAWN: 100,
    chess.ROOK: 500,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.QUEEN: 900,
    chess.KING: 20000
}

pawnEvalWhite = [
    0,  0,  0,  0,  0,  0,  0,  0,
    5, 10, 10, -20, -20, 10, 10,  5,
    5, -5, -10,  0,  0, -10, -5,  5,
    0,  0,  0, 20, 20,  0,  0,  0,
    5,  5, 10, 25, 25, 10,  5,  5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0
]
pawnEvalBlack = list(reversed(pawnEvalWhite))

knightEval = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50
]

bishopEvalWhite = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20
]
bishopEvalBlack = list(reversed(bishopEvalWhite))

rookEvalWhite = [
    0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0
]
rookEvalBlack = list(reversed(rookEvalWhite))

queenEval = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -5, 0, 5, 5, 5, 5, 0, -5,
    0, 0, 5, 5, 5, 5, 0, -5,
    -10, 5, 5, 5, 5, 5, 0, -10,
    -10, 0, 5, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20
]

kingEvalWhite = [
    20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30
]
kingEvalBlack = list(reversed(kingEvalWhite))


def evaluate_piece(piece: chess.Piece, square: chess.Square) -> int:
    """
    Evaluates the value of a chess piece based on its type and position on the board.

    Args:
        piece (chess.Piece): The chess piece to evaluate.
        square (chess.Square): The square on the board where the piece is located.

    Returns:
        int: The value of the piece based on its type and position on the board.

    The function uses predefined piece value mappings for each type of piece (pawn, knight, bishop, rook, queen, king)
    and for each color (white, black). The mappings are lists of values for each square on the board.
    The function returns the value from the appropriate mapping for the given piece and square.
    """

    piece_type = piece.piece_type
    mapping = []
    if piece_type == chess.PAWN:
        mapping = pawnEvalWhite if piece.color == chess.WHITE else pawnEvalBlack
    if piece_type == chess.KNIGHT:
        mapping = knightEval
    if piece_type == chess.BISHOP:
        mapping = bishopEvalWhite if piece.color == chess.WHITE else bishopEvalBlack
    if piece_type == chess.ROOK:
        mapping = rookEvalWhite if piece.color == chess.WHITE else rookEvalBlack
    if piece_type == chess.QUEEN:
        mapping = queenEval
    if piece_type == chess.KING:
        mapping = kingEvalWhite if piece.color == chess.WHITE else kingEvalBlack

    return mapping[square]



def evaluate_board(board: chess.Board) -> float:
    """
    Evaluates the full board and determines which player is in a most favorable position.

    The function iterates over all squares on the board, evaluates the piece on each square (if any),
    and adds or subtracts the value from the total score depending on the piece's color.
    If the board is in a checkmate state, the function returns positive or negative infinity depending on the winning side.

    Args:
        board (chess.Board): The chess board to evaluate.

    Returns:
        float: The total score of the board. The sign indicates the side:
            (+) for white
            (-) for black
        The magnitude indicates how big of an advantage that player has.
    """
    total = 0
    if board.is_checkmate():
        return -float("inf") if board.turn == chess.BLACK else float("inf")

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if not piece:
            continue

        value = piece_value[piece.piece_type] + evaluate_piece(piece, square)
        total += value if piece.color == chess.WHITE else -value

    return total


def order_moves(board: chess.Board) -> list[chess.Move]:
    """
    Orders legal moves based on priority: captures, checks, other moves.

    Args:
      board: The chess board.

    Returns:
      A list of legal moves ordered by priority.
    """
    moves = list(board.legal_moves)
    captures = []
    checks = []
    for move in moves:
        board.push(move)
        if board.is_check():
            checks.append(move)
        elif board.is_capture(move):
            captures.append(move)
        board.pop()
    other_moves = [move for move in moves if move not in captures and move not in checks]
    return captures + checks + other_moves


def min_max(board: chess.Board, depth: int, alpha: float, beta: float) -> (float, chess.Move):
    """
    Implements the Minimax algorithm with Alpha-Beta pruning to find the best move for the current player.

    The function recursively explores the game tree up to a certain depth. At each node, it simulates a move and evaluates the board.
    The function uses the Alpha-Beta pruning technique to cut off branches in the game tree and speed up the search process.

    Args:
        board (chess.Board): The current state of the chess board.
        depth (int): The maximum depth of the game tree to explore.
        alpha (float): The best (highest) value found so far for the maximizing player (white).
        beta (float): The best (lowest) value found so far for the minimizing player (black).

    Returns:
        float: The evaluation score of the best move found.
        chess.Move: The best move found.
    """
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    ordered_moves = order_moves(board)
    if board.turn == chess.WHITE:
        best_move = None
        best_value = -float("inf")
        for move in ordered_moves:
            board.push(move)
            value, _ = min_max(board, depth - 1, alpha, beta)
            board.pop()
            best_value = max(best_value, value)  # Update best_value regardless
            alpha = max(alpha, value)
            if beta <= alpha:
                break
            best_move = move  # Update best_move whenever a better value is found
        return best_value, best_move
    else:
        best_move = None
        best_value = float("inf")
        for move in ordered_moves:
            board.push(move)
            value, _ = min_max(board, depth - 1, alpha, beta)
            board.pop()
            best_value = min(best_value, value)  # Update best_value regardless
            beta = min(beta, value)
            if beta <= alpha:
                break
            best_move = move  # Update best_move whenever a better value is found
        return best_value, best_move

def best_move(board: chess.Board, depth: int) -> chess.Move:
    ''' Returns the best move for the current player given the board state and search depth.'''
    _, best_move = min_max(board, depth, -float("inf"), float("inf"))
    return best_move