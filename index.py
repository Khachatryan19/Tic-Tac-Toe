import tkinter as tk
import random
from tkinter import messagebox


class TicTacToe:
    def __init__(self, master):
        self.state = 0
        self.initial_cases = [
            [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']],
            [[' ', ' ', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']],
            [[' ', ' ', ' '], [' ', ' ', ' '], ['X', ' ', ' ']],
            [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', 'X']],
        ]
        self.master = master
        self.master.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(master, text="", font=("Arial", 20), width=5, height=2,
                                               command=lambda i=i, j=j: self.on_button_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

        self.status_label = tk.Label(master, text="Turn: Player X", font=("Arial", 12))
        self.status_label.grid(row=3, columnspan=3)

    def on_button_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_game()
            else:
                self.generate_opponent_step()
                if self.check_winner():
                    messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                    self.reset_game()
                elif self.is_board_full():
                    messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                    self.reset_game()
                self.current_player = "X"
                self.status_label.config(text=f"Turn: Player {self.current_player}")
        else:
            messagebox.showerror("Tic Tac Toe", "Invalid move. Please try again.")

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def reset_game(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
        self.current_player = "X"
        self.status_label.config(text="Turn: Player X")

    def generate_opponent_step(self):
        self.current_player = 'O'
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        close_line = self.close_line()
        print(close_line)
        if close_line is not None:
            row, col = close_line
        else:
            while (self.board[row][col] != " "):
                row = random.randint(0, 2)
                col = random.randint(0, 2)

        self.board[row][col] = self.current_player
        self.buttons[row][col].config(text=self.current_player)

    def close_line(self):
        if (self.state == 1):
            self.state = self.state - 1
            return 1, 2

        for case in self.initial_cases:
            if self.board == case:
                self.state = self.state + 1
                return 1, 1

        if self.board == [[' ', ' ', ' '], [' ', 'X', ' '], [' ', ' ', ' ']]:
            return 0, 0

        for row_index, row in enumerate(self.board):
            if (row.count('O') == 2) and row.count(' ') == 1:
                col_index = row.index(' ')
                return row_index, col_index

        for row_index, row in enumerate(self.board):
            if (row.count('X') == 2) and row.count(' ') == 1:
                col_index = row.index(' ')
                return row_index, col_index

        vertical_board = [[row[col] for row in self.board] for col in range(len(self.board[0]))]

        print(self.board)
        print('vertical ------> ')
        print(vertical_board)

        for row_index, row in enumerate(vertical_board):
            if (row.count('O') == 2) and row.count(' ') == 1:
                col_index = row.index(' ')
                return col_index, row_index

        for row_index, row in enumerate(vertical_board):
            if (row.count('X') == 2) and row.count(' ') == 1:
                col_index = row.index(' ')
                return col_index, row_index

        diagonal_board = [
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[0][2], self.board[1][1], self.board[2][0]]
        ]
        for row_index, row in enumerate(diagonal_board):
            if (row.count('O') == 2) and row.count(' ') == 1:
                col_index = row.index(' ')
                if row_index == 0:
                    return col_index, col_index
                else:
                    return col_index, 2 - col_index

        for row_index, row in enumerate(diagonal_board):
            if (row.count('X') == 2) and row.count(' ') == 1:
                col_index = row.index(' ')
                if row_index == 0:
                    return col_index, col_index
                else:
                    return col_index, 2 - col_index

        return None

def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()


if __name__ == "__main__":
    main()
