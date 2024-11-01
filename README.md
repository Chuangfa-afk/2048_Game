# 2048 Game

A Python implementation of the classic game **2048**! This project allows you to play the game in the terminal using simple controls for moving tiles up, down, left, and right to combine numbers and reach the goal of **2048**.

## How to Play

- **Objective**: Combine tiles with the same number to create larger numbers, aiming to reach **2048**.
- **Controls**:
  - **W**: Move Up
  - **S**: Move Down
  - **A**: Move Left
  - **D**: Move Right

After each move, a new tile (with a value of 2) is added to a random empty position on the board.

## Game Rules

1. Tiles with the same number merge when they collide in the direction of your move.
2. The game ends when:
   - You reach a tile with the value **2048** (Victory! 🎉).
   - There are no more moves left and no empty spaces on the board (Defeat 😞).

## Code Structure

- `main.py`: The main entry point for running the game.
- `functions.py`: Contains the core `game2048` class that handles game logic, including board setup, moves, merging, and game status checks.

### Running the Game

python main.py

## Example

Here's an example of what the board might look like after some moves:

+----+----+----+----+ | | 2 | | | +----+----+----+----+ | | | | | +----+----+----+----+ | | 4 | 2 | | +----+----+----+----+ | | | | | +----+----+----+----+

## Enjoy the game~!!!

