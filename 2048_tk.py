"""
2048 Game (GUI) using tkinter
Default board size = 4x4
Board stays centered on any screen size
"""

import random
import tkinter as tk
from tkinter import messagebox

# ---------- Functional game logic ----------

def new_board(size=4):
    return [[0 for _ in range(size)] for _ in range(size)]

def add_random_tile(board):
    empty = [(r, c) for r in range(len(board)) for c in range(len(board)) if board[r][c] == 0]
    if not empty:
        return board
    r, c = random.choice(empty)
    board[r][c] = random.choice([2, 4])
    return board

def compress(row):
    new_row = [num for num in row if num != 0]
    new_row += [0] * (len(row) - len(new_row))
    return new_row

def merge(row):
    score = 0
    for i in range(len(row) - 1):
        if row[i] != 0 and row[i] == row[i + 1]:
            row[i] *= 2
            score += row[i]
            row[i + 1] = 0
    return row, score

def move_left(board):
    new_board, score = [], 0
    for row in board:
        row = compress(row)
        row, add_score = merge(row)
        row = compress(row)
        new_board.append(row)
        score += add_score
    return new_board, score

def reverse(board):
    return [row[::-1] for row in board]

def transpose(board):
    return [list(row) for row in zip(*board)]

def move_right(board):
    board = reverse(board)
    board, score = move_left(board)
    return reverse(board), score

def move_up(board):
    board = transpose(board)
    board, score = move_left(board)
    return transpose(board), score

def move_down(board):
    board = transpose(board)
    board, score = move_right(board)
    return transpose(board), score

def check_game_over(board):
    for row in board:
        if 0 in row:
            return False
    for r in range(len(board)):
        for c in range(len(board) - 1):
            if board[r][c] == board[r][c + 1] or board[c][r] == board[c + 1][r]:
                return False
    return True

# ---------- GUI Implementation ----------

class Game2048:
    def __init__(self, root):
        self.root = root
        self.root.title("2048 Game")
        self.root.configure(bg="#faf8ef")

        # Center window on screen
        window_width, window_height = 500, 600
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_pos = int((screen_width / 2) - (window_width / 2))
        y_pos = int((screen_height / 2) - (window_height / 2))
        root.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

        self.size = 4
        self.score = 0
        self.board = new_board(self.size)

        # Always start with one 2 and one 4
        empty = [(r, c) for r in range(self.size) for c in range(self.size)]
        (r1, c1), (r2, c2) = random.sample(empty, 2)
        self.board[r1][c1] = 2
        self.board[r2][c2] = 4

        self.cells = []
        self.bg_color = "#bbada0"
        self.cell_colors = {
            0: "#cdc1b4", 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
            16: "#f59563", 32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72",
            256: "#edcc61", 512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"
        }

        # Create main frame centered
        self.main_frame = tk.Frame(self.root, bg=self.bg_color, bd=10)
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.create_gui()
        self.update_gui()
        self.root.bind("<Key>", self.key_handler)

    def create_gui(self):
        for r in range(self.size):
            row = []
            for c in range(self.size):
                label = tk.Label(self.main_frame, text="", width=4, height=2,
                                 font=("Helvetica", 24, "bold"),
                                 bg=self.cell_colors[0], fg="#776e65")
                label.grid(row=r, column=c, padx=5, pady=5)
                row.append(label)
            self.cells.append(row)

        # Score label
        self.score_label = tk.Label(self.root, text=f"Score: {self.score}",
                                    font=("Helvetica", 16, "bold"), bg="#faf8ef", fg="#776e65")
        self.score_label.pack(pady=10)

        # Restart button
        restart_btn = tk.Button(self.root, text="Restart", font=("Helvetica", 14),
                                command=self.restart_game, bg="#8f7a66", fg="white")
        restart_btn.pack()

    def update_gui(self):
        for r in range(self.size):
            for c in range(self.size):
                value = self.board[r][c]
                color = self.cell_colors.get(value, "#3c3a32")
                text = str(value) if value != 0 else ""
                self.cells[r][c].config(text=text, bg=color)
        self.score_label.config(text=f"Score: {self.score}")
        self.root.update_idletasks()

    def key_handler(self, event):
        key = event.keysym
        temp_board = [row[:] for row in self.board]
        add_score = 0

        if key == "Left":
            self.board, add_score = move_left(self.board)
        elif key == "Right":
            self.board, add_score = move_right(self.board)
        elif key == "Up":
            self.board, add_score = move_up(self.board)
        elif key == "Down":
            self.board, add_score = move_down(self.board)
        else:
            return

        if self.board != temp_board:
            self.score += add_score
            add_random_tile(self.board)
            self.update_gui()

            if any(2048 in row for row in self.board):
                messagebox.showinfo("2048", "You reached 2048! You win!")
            elif check_game_over(self.board):
                messagebox.showinfo("Game Over", "No more moves left!")

    def restart_game(self):
        self.score = 0
        self.board = new_board(self.size)
        # Restart with one 2 and one 4
        empty = [(r, c) for r in range(self.size) for c in range(self.size)]
        (r1, c1), (r2, c2) = random.sample(empty, 2)
        self.board[r1][c1] = 2
        self.board[r2][c2] = 4
        self.update_gui()


if __name__ == "__main__":
    root = tk.Tk()
    Game2048(root)
    root.mainloop()
