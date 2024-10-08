# Tic Tac Toe Game (GUI)

This repository contains a Tic Tac Toe game implemented with Python’s Tkinter library. Players can play against each other or compete against the computer. The game features a graphical interface with interactive buttons and includes basic AI functionality for the computer opponent.

## Project Overview

### Features
- **Player vs Player** or **Player vs Computer** modes.
- Graphical interface for ease of play.
- Randomized AI strategy with a best-move algorithm.
- Shows game results (win or tie) with a message prompt and auto-resets the game for replay.

## How to Play

1. **Clone the Repository**
   ```bash
   git clone https://github.com/prantikm07/Tic-Tac-Toe-GUI.git
   cd tic-tac-toe-gui
   ```

2. **Run the Game**
   ```bash
   python tictactoeui.py
   ```

3. **Follow the Prompts**
   - At the start, choose if you want to play against the computer or another player.
   - If playing against the computer, select your symbol (X or O).
   - Take turns clicking on the grid to place your symbol.
   - The game will automatically reset after a win or a tie.

## Game Rules

- Players take turns marking a 3x3 grid.
- The player with the symbol “X” always starts.
- The first player to line up three symbols in a row (horizontal, vertical, or diagonal) wins.
- If all squares are filled without a winner, the game ends in a tie.

## Requirements

- **Python 3.x**
- **Tkinter** (included with standard Python installation)

## Code Structure

- **TicTacToe Class**: Manages the game logic and handles GUI interactions.
  - `create_grid`: Initializes the game board.
  - `choose_game_mode`: Sets the game mode based on user choice.
  - `player_move`: Handles the player’s move.
  - `computer_move`: Determines the best move for the computer.
  - `find_best_move`: AI strategy to win or block the player from winning.
  - `is_winner`: Checks for a winning condition.
  - `reset_game`: Resets the game board.

## License

This project is open-source and available for modification and distribution.
