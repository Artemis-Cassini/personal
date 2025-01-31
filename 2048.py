from tkinter import *
import random

class Play_2048(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        
        # Initialize game variables
        self.game_board = [[0] * 4 for _ in range(4)]
        self.name_random_tiles = [2, 2, 2, 2, 2, 2, 4]
        self.score = 0
        self.high_score = 0

        # UI Variables
        self.game_score = StringVar(self, "0")
        self.highest_score = StringVar(self, "0")

        # Button frame
        self.button_frame = Frame(self)
        self.button_frame.pack(side="top")
        Button(self.button_frame, text="New Game", font=("times new roman", 15), command=self.new_game).grid(row=0, column=0)
        Label(self.button_frame, text="Score:", font=("times new roman", 15)).grid(row=0, column=1)
        Label(self.button_frame, textvariable=self.game_score, font=("times new roman", 15)).grid(row=0, column=2)
        Label(self.button_frame, text="Record:", font=("times new roman", 15)).grid(row=0, column=3)
        Label(self.button_frame, textvariable=self.highest_score, font=("times new roman", 15)).grid(row=0, column=4)

        # Game board canvas
        self.canvas = Canvas(self, width=410, height=410, borderwidth=5, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand=False)

        # Bind key events
        self.bind_all('<Key>', self.moves)

        # Start a new game
        self.new_game()

    def new_game(self):
        """Initialize a new game."""
        self.score = 0
        self.game_score.set("0")
        self.game_board = [[0] * 4 for _ in range(4)]
        self.add_random_tile()
        self.add_random_tile()
        self.show_board()

    def add_random_tile(self):
        """Add a new tile to the game board."""
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.game_board[i][j] == 0]
        if empty_cells:
            x, y = random.choice(empty_cells)
            self.game_board[x][y] = random.choice(self.name_random_tiles)

    def show_board(self):
        """Update the visual representation of the board."""
        self.canvas.delete("all")
        cell_width = 105
        cell_height = 105
        bg_colors = {
            0: "#cdc1b4", 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
            16: "#f59563", 32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72",
            256: "#edcc61", 512: "#f2b179", 1024: "#edc850", 2048: "#edc22e"
        }
        text_colors = {
            2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2",
            32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2", 256: "#f9f6f2",
            512: "#f9f6f2", 1024: "#f9f6f2", 2048: "#f9f6f2"
        }
        for i in range(4):
            for j in range(4):
                value = self.game_board[i][j]
                x1, y1 = j * cell_width, i * cell_height
                x2, y2 = x1 + cell_width - 5, y1 + cell_height - 5
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=bg_colors[value], outline="")
                if value:
                    self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(value),
                                             font=("Arial", 36), fill=text_colors.get(value, "black"))

    def moves(self, event):
        """Handle keypresses to move tiles."""
        if event.keysym in ['Up', 'Down', 'Left', 'Right']:
            self.shift(event.keysym)
            self.add_random_tile()
            self.show_board()
            if self.is_game_over():
                self.game_over()

    def shift(self, direction):
        """Shift tiles in the given direction."""
        def merge(row):
            """Helper to merge a single row or column."""
            non_zero = [num for num in row if num != 0]
            merged = []
            skip = False
            for i in range(len(non_zero)):
                if skip:
                    skip = False
                    continue
                if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
                    merged.append(non_zero[i] * 2)
                    self.score += non_zero[i] * 2
                    skip = True
                else:
                    merged.append(non_zero[i])
            return merged + [0] * (4 - len(merged))

        rotated = self.rotate_board(direction)
        for i in range(4):
            rotated[i] = merge(rotated[i])
        self.game_board = self.rotate_board(direction, reverse=True, board=rotated)

    def rotate_board(self, direction, reverse=False, board=None):
        """Rotate the board to align with the intended shift direction."""
        if board is None:
            board = self.game_board
        if direction == 'Up':
            return [list(row) for row in zip(*board[::-1])] if not reverse else [list(row) for row in zip(*board)][::-1]
        if direction == 'Down':
            return [list(row) for row in zip(*board)][::-1] if not reverse else [list(row) for row in zip(*board[::-1])]
        if direction == 'Left':
            return board if not reverse else [row[::-1] for row in board]
        if direction == 'Right':
            return [row[::-1] for row in board] if not reverse else board

    def is_game_over(self):
        """Check if the game is over."""
        for i in range(4):
            for j in range(4):
                if self.game_board[i][j] == 0:
                    return False
                if j < 3 and self.game_board[i][j] == self.game_board[i][j + 1]:
                    return False
                if i < 3 and self.game_board[i][j] == self.game_board[i + 1][j]:
                    return False
        return True

    def game_over(self):
        """Display game over message."""
        self.canvas.create_text(205, 205, text="GAME OVER", font=("Arial", 48), fill="red")

if __name__ == "__main__":
    app = Play_2048()
    app.mainloop()