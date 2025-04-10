import logging
import os

import uvicorn
from fastapi import FastAPI

from move_validator import MoveValidator, NoSafeMovesException
from schemas import GameState, GameStats, Move, SelectedMove

app = FastAPI()


@app.get("/")
def on_info() -> GameStats:
    """Customize your snake see https://play.battlesnake.com/customizations for more details """
    return GameStats(
        apiversion="1",
        author="Demo_Guy",
        color="#FF69B4",
        head="antelope",
        tail="beach-puffin",
    )


@app.post("/start")
def on_start(game_state: GameState) -> str:
    """Called in beginning of the game"""
    print("GAME START")
    return "ok"


@app.post("/move")
def on_move(game_state: GameState) -> SelectedMove:
    """Called on each turn of the game, here you can decide where to move your snake"""
    move_selector = MoveValidator(game_state)
    move_selector.avoid_moving_backwards()
    move_selector.avoid_moving_out_of_bounds()
    try:
        return SelectedMove(move=move_selector.choose_random_safe_move())
    except NoSafeMovesException:
        print("panic just go left")
        return SelectedMove(move=Move.LEFT)


@app.post("/end")
def on_end(game_state: GameState) -> str:
    """Called when a game ends"""
    print("GAME OVER\n")
    return "ok"


if __name__ == "__main__":
    logging.getLogger("uvicorn").setLevel(logging.ERROR)
    port = int(os.environ.get("PORT", "8080"))
    print(f"\nRunning Battlesnake at http://0.0.0.0:{port}/docs")
    uvicorn.run(app, host="0.0.0.0", port=port)
