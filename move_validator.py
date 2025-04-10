from random import choice

from schemas import GameState, Move


class NoSafeMovesException(Exception):
    """Custom error for when we can't find a safe move"""
    pass


class MoveValidator:
    """Class to validate safe moves for the Snake game."""

    def __init__(self, game_state: GameState):
        self.game_state = game_state
        self.safe_moves = {move: True for move in Move}

    def avoid_moving_backwards(self) -> None:
        """Validate moves to avoid moving against the Snake's neck."""
        my_head = self.game_state.you.head
        my_neck = self.game_state.you.body[1]
        if my_neck.x < my_head.x:
            self.safe_moves[Move.LEFT] = False
        elif my_neck.x > my_head.x:
            self.safe_moves[Move.RIGHT] = False
        elif my_neck.y < my_head.y:
            self.safe_moves[Move.DOWN] = False
        elif my_neck.y > my_head.y:
            self.safe_moves[Move.UP] = False

    def avoid_moving_out_of_bounds(self)->None:
        """Validate moves to avoid moving out of bounds"""
        board_width = self.game_state.board.width
        board_height = self.game_state.board.height
        my_head = self.game_state.you.head
        print(f"my_head:{my_head}, board_width:{board_width}, board_height:{board_height}")
        if my_head.x - 1 <= 0:
            self.safe_moves[Move.LEFT] = False
        elif my_head.x +1 >= board_width:
            self.safe_moves[Move.RIGHT] = False
        elif my_head.y -1 <= 0:
            self.safe_moves[Move.DOWN] = False
        elif my_head.y +1 >= board_height:
            self.safe_moves[Move.UP] = False

    def avoid_moving_into_body(self):
        # TODO: Step 2 - Prevent your Battlesnake from colliding with itself
        # my_body = self.game_state.you.body
        raise NotImplementedError("Avoid moving into body not implemented yet")

    def avoid_moving_into_snakes(self):
        # TODO: Step 3 - Prevent your Battlesnake from colliding with other Battlesnakes
        # opponents = self.game_state.board.snakes
        raise NotImplementedError("Avoid moving into snakes not implemented yet")

    def _get_safe_moves(self) -> list[Move]:
        """Loops through the moves to collect all safe moves."""
        return [move for move, safe in self.safe_moves.items() if safe]

    def get_move_towards_food(self):
        # TODO: Step 4 - Move towards food instead of random, to regain health and survive longer
        # food = self.game_state.board.food
        raise NotImplementedError("Get move towards food not implemented yet")

    def choose_random_safe_move(self) -> Move:
        """Try to return a safe move or raise an exception if none are found."""
        safe_moves = self._get_safe_moves()
        if not safe_moves:
            raise NoSafeMovesException("No safe moves available")
        return choice(safe_moves)
