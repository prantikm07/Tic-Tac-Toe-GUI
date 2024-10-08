import tkinter as tk
import random
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.symbol_1 = "X"
        self.symbol_2 = "O"
        self.current_player = self.symbol_1
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_grid()
        self.player_vs_computer = False
        self.is_player_x = True

        # Game mode selection
        self.choose_game_mode()

    def create_grid(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text=" ", font=('normal', 40, 'bold'),
                                   width=5, height=2, command=lambda row=i, col=j: self.player_move(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def choose_game_mode(self):
        game_mode = messagebox.askquestion("Game Mode", "Do you want to play against the computer? (Yes for Computer, No for Player vs Player)")
        if game_mode == "yes":
            self.player_vs_computer = True
            symbol_choice = messagebox.askquestion("Symbol Choice", "Do you want to be X? (Yes for X, No for O)")
            if symbol_choice == "yes":
                self.symbol_1 = "X"
                self.symbol_2 = "O"
                self.is_player_x = True
            else:
                self.symbol_1 = "O"
                self.symbol_2 = "X"
                self.is_player_x = False
        self.current_player = self.symbol_1 if self.is_player_x else self.symbol_2

        # Player with 'X' always starts
        if not self.is_player_x and self.player_vs_computer:
            self.root.after(500, self.computer_move)

    def player_move(self, row, col):
        if self.buttons[row][col]["text"] == " " and self.current_player == self.symbol_1:
            self.buttons[row][col]["text"] = self.current_player
            self.board[row][col] = self.current_player
            if self.is_winner(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_full():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.switch_player()
                if self.player_vs_computer and self.current_player == self.symbol_2:
                    self.root.after(500, self.computer_move)  # Add delay for computer move

    def computer_move(self):
        row, col = self.find_best_move()
        self.buttons[row][col]["text"] = self.symbol_2
        self.board[row][col] = self.symbol_2
        if self.is_winner(self.symbol_2):
            messagebox.showinfo("Game Over", f"Computer ({self.symbol_2}) wins!")
            self.reset_game()
        elif self.is_full():
            messagebox.showinfo("Game Over", "It's a tie!")
            self.reset_game()
        else:
            self.switch_player()

    def find_best_move(self):
        # Step 1: Check if computer can win
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = self.symbol_2
                    if self.is_winner(self.symbol_2):
                        return i, j
                    else:
                        self.board[i][j] = " "

        # Step 2: Block player from winning
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = self.symbol_1
                    if self.is_winner(self.symbol_1):
                        self.board[i][j] = " "
                        return i, j
                    else:
                        self.board[i][j] = " "

        # Step 3: Take center if available
        if self.board[1][1] == " ":
            return 1, 1

        # Step 4: Take a corner if available
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        random.shuffle(corners)  # Randomize to add some unpredictability
        for corner in corners:
            if self.board[corner[0]][corner[1]] == " ":
                return corner

        # Step 5: Choose a random spot
        empty_spots = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == " "]
        return random.choice(empty_spots)

    def switch_player(self):
        if self.current_player == self.symbol_1:
            self.current_player = self.symbol_2
        else:
            self.current_player = self.symbol_1

    def is_winner(self, symbol):
        # Check rows, columns, and diagonals
        for row in self.board:
            if row.count(symbol) == 3:
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == symbol:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == symbol or self.board[0][2] == self.board[1][1] == self.board[2][0] == symbol:
            return True
        return False

    def is_full(self):
        for row in self.board:
            if " " in row:
                return False
        return True

    def reset_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = " "
        self.current_player = self.symbol_1 if self.is_player_x else self.symbol_2
        if not self.is_player_x and self.player_vs_computer:
            self.root.after(500, self.computer_move)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
