from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class Location(BaseModel):
    """Represents a 2D location somewhere on the board"""
    x: int = Field(..., examples=[0, 5, 10])
    y: int = Field(..., examples=[1, 6, 11])


class Customization(BaseModel):
    """Represents the chosen customization for a snake """
    color: str = Field(..., examples=["#00FF00", "#FF0000"])
    head: str = Field(..., examples=["alligator", "chicken", "cute-dragon"])
    tail: str = Field(..., examples=["curled", "duck", "default"])


class Snake(BaseModel):
    """Represents a snake on the board"""
    id: str = Field(..., examples=["fe512e52-599e-4b20-a0c8-b8a1d4d743a5"])
    name: str = Field(..., examples=["snake1"])
    latency: str = Field(..., examples=["10ms"])
    health: int = Field(..., description="Current health of the snake", ge=0, le=100, examples=[10, 50, 90])
    body: List[Location] = Field(..., description="locations of all body parts of the snake",
                                 examples=[[Location(x=0, y=1)], [Location(x=1, y=1)], [Location(x=2, y=1)]])
    head: Location = Field(..., description="location of the snake's head")
    length: int = Field(..., description="length of the snake", examples=[3])
    shout: Optional[str] = Field(..., description="shout a message to all other snakes in the game",
                                 examples=["Moving up !"])
    squad: Optional[str] = Field(..., description="squad name when battling with the squad mode", examples=["Team Red"])
    customizations: Customization = Field(...)


class Board(BaseModel):
    """Representation of the current state of the board."""
    height: int = Field(..., description="height of the board", examples=[11])
    width: int = Field(..., description="width of the board", examples=[11])
    snakes: List[Snake] = Field(..., description="list of snakes on the board")
    food: List[Location] = Field(..., description="list of food locations on the board")
    hazards: List[Location] = Field(..., description="list of hazard locations on the board")


class Game(BaseModel):
    """Global settings from the game"""
    id: str = Field(...)  # doesn't matter fow now
    ruleset: dict = Field(...)  # doesn't matter fow now
    map: str = Field(...)  # doesn't matter fow now
    timeout: int = Field(...)  # doesn't matter fow now
    source: str = Field(...)  # doesn't matter fow now


class GameStats(BaseModel):
    """Customize your snake see https://play.battlesnake.com/customizations for more details """
    apiversion: str = Field(default="1")
    author: str = Field(..., examples=["Princess Peach"])
    color: str = Field(..., examples=["#00FF00", "#FF0000"])
    head: str = Field(..., examples=["alligator", "chicken", "cute-dragon"])
    tail: str = Field(..., examples=["curled", "duck", "default"])


class GameState(BaseModel):
    """Current state of the game"""
    game: Game = Field(...)
    turn: int = Field(..., description="current turn number", examples=[0, 1, 2])
    board: Board = Field(...)
    you: Snake = Field(...)


class Move(Enum):
    """Enum for possible moves in the game"""
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"


class SelectedMove(BaseModel):
    """Return value of selected move by the snake"""
    move: Move = Field(..., examples=[Move.UP])
