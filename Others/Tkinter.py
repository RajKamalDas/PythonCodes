import tkinter as tk
import random

class MineSweeper:
    HIDDEN = -1
    MINE = -2
    MARKED = -3

    def __init__(self, size=8, mines=10):
        self.size = size
        self.mines = mines
        self.grid = [[self.HIDDEN for _ in range(size)] for _ in range(size)]
        self.buttons = {}
        self.root = tk.Tk()
        self.root.title("Minesweeper")

        # --- Top label
        self.status = tk.Label(self.root, text="Welcome to Minesweeper!", font=("Arial", 14))
        self.status.pack(pady=10)

        # --- Frame for the grid (adds padding & neat box look)
        self.frame = tk.Frame(self.root, bd=3, relief="ridge", padx=10, pady=10)
        self.frame.pack(padx=20, pady=20)

        self.place_mines()
        self.calculate_numbers()
        self.make_board()

    def place_mines(self):
        placed = 0
        while placed < self.mines:
            x, y = random.randrange(self.size), random.randrange(self.size)
            if self.grid[x][y] != self.MINE:
                self.grid[x][y] = self.MINE
                placed += 1

    def calculate_numbers(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.grid[x][y] == self.MINE:
                    continue
                count = 0
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < self.size and 0 <= ny < self.size:
                            if self.grid[nx][ny] == self.MINE:
                                count += 1
                self.grid[x][y] = count

    def make_board(self):
        for x in range(self.size):
            for y in range(self.size):
                b = tk.Button(
                    self.frame,
                    width=3, height=1,
                    command=lambda x=x, y=y: self.reveal(x, y)
                )
                b.bind("<Button-3>", lambda e, x=x, y=y: self.mark(x, y))
                b.grid(row=x, column=y, padx=1, pady=1)
                self.buttons[(x, y)] = b

    def reveal(self, x, y):
        if self.grid[x][y] == self.MINE:
            self.buttons[(x, y)].config(text="💣", bg="red")
            self.status.config(text="💥 Game Over!")
            self.game_over(False)
        elif self.grid[x][y] == 0:
            self.buttons[(x, y)].config(text="", state="disabled", relief="sunken")
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.size and 0 <= ny < self.size:
                        if self.buttons[(nx, ny)]["state"] == "normal":
                            self.reveal(nx, ny)
        else:
            self.buttons[(x, y)].config(
                text=str(self.grid[x][y]),
                state="disabled",
                relief="sunken"
            )

    def mark(self, x, y):
        b = self.buttons[(x, y)]
        if b["text"] == "🚩":
            b.config(text="")
        else:
            b.config(text="🚩")

    def game_over(self, won):
        for (x, y), b in self.buttons.items():
            if self.grid[x][y] == self.MINE:
                b.config(text="💣")
        msg = "🎉 You Win!" if won else "💀 You Lose!"
        self.status.config(text=msg)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    MineSweeper(size=8, mines=10).run()
