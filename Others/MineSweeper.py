import time
import random
import keyboard

random.seed(time.time())


def getInput(*Allowed, message="Plese, Enter:", banned=" "):
    if Allowed[0].lower() not in [
        "numbers",
        "num",
        "numb",
        "number",
        "integer",
        "digit",
        "integers",
        "digits",
    ]:
        chars = [c for c in Allowed if c not in banned]
        forprint = set([c.upper() for c in chars])
        output = input(f"{message} {forprint}:")
        while output not in chars:
            output = input(f"Plese, any of {forprint}:")
    else:
        output = input(f"{message} (e.g. 0, 1, 2, …):")
        while True:
            try:
                output = int(output)
                break
            except ValueError:
                output = input(f"Plese, any number:")
    return output


class MineSweeper:
    score = 0
    LIMIT, MINE_COUNT, HIDDEN, MINE, MARKED = 5, 3, -1, -2, -3
    cursor = []
    mines = []
    marked = []
    grid = [[]]

    def __init__(self, size=5, mines=0):

        self.LIMIT = size
        self.MINE_COUNT = mines if mines != 0 else size // 2
        self.score = 0

        self.setup()
        self.printer()
        self.pressor = keyboard.on_press(self.pressed)

    def setup(self):
        self.grid.clear()
        self.mines.clear()
        self.marked.clear()

        self.grid = [
            [self.HIDDEN for i in range(self.LIMIT)] for j in range(self.LIMIT)
        ]
        self.cursor = [self.LIMIT // 2, self.LIMIT // 2]
        for _ in range(self.MINE_COUNT):
            x, y = random.randrange(self.LIMIT), random.randrange(self.LIMIT)
            while [x, y] in self.mines or [x, y] == self.cursor:
                x, y = random.randrange(self.LIMIT), random.randrange(self.LIMIT)
            self.grid[x][y] = self.MINE
            self.mines.append([x, y])

    def pressed(self, event):
        if event.name == "left":
            self.cursor[1] = (self.cursor[1] - 1) % self.LIMIT
            self.printer()
        elif event.name == "right":
            self.cursor[1] = (self.cursor[1] + 1) % self.LIMIT
            self.printer()
        elif event.name == "up":
            self.cursor[0] = (self.cursor[0] - 1) % self.LIMIT
            self.printer()
        elif event.name == "down":
            self.cursor[0] = (self.cursor[0] + 1) % self.LIMIT
            self.printer()
        elif event.name == "c":
            self.check()
        elif event.name == "x":
            self.mark()

        time.sleep(0.15)

    def mark(self):
        x, y = self.cursor
        if self.cursor not in self.marked:
            self.grid[x][y] = self.MARKED
            self.marked.append([x, y])
        else:
            self.grid[x][y] = self.HIDDEN
            self.marked.remove([x, y])
        self.printer()
        if sum([i in self.marked for i in self.mines]) == self.MINE_COUNT:
            self.scorer()

    def check(self):
        x, y = self.cursor
        if self.cursor in self.mines:
            print("Sorry.")
            self.scorer()
        elif self.grid[x][y] == self.HIDDEN:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    try:
                        if (
                            self.grid[x + i][y + j] > self.MINE
                            and x + i >= 0
                            and y + j >= 0
                        ):
                            self.dilute(x + i, y + j)
                    except IndexError:
                        pass
        self.printer()

    def dilute(self, x, y):
        try:
            self.grid[x][y] = len(
                [
                    k
                    for k in (
                        [
                            self.grid[i][j]
                            for i in range(
                                (x - 1 if x > 0 else x),
                                (x + 2 if x + 2 < self.LIMIT else self.LIMIT),
                            )
                            for j in range(
                                (y - 1 if y > 0 else y),
                                (y + 2 if y + 2 < self.LIMIT else self.LIMIT),
                            )
                        ]
                    )
                    if k <= self.MINE
                ]
            )
        except IndexError:
            pass

    def printer(self):
        x, y = self.cursor
        print("-" * (self.LIMIT * 4 + 1))
        for i in range(self.LIMIT):
            for j in range(self.LIMIT):
                val = self.grid[i][j]
                # Start
                if i == x and j == y:
                    print("|", end="[")
                else:
                    print("|", end=" ")
                # Mid
                if val == 0:
                    print(" ", end="")
                elif val == self.MARKED:
                    print("X", end="")
                elif val < 0:
                    print("#", end="")
                else:
                    print(f"{val}", end="")
                # End
                if i == x and j == y:
                    print("", end="]")
                else:
                    print("", end=" ")

            print("|")
            print("-" * (self.LIMIT * 4 + 1))
        x = True
        for c in self.grid:
            if self.HIDDEN in c:
                x = False
        if x:
            self.scorer()

    def scorer(self):
        self.score += sum([-500 if i not in self.mines else 1000 for i in self.marked])
        print("Score:", self.score)
        keyboard.press_and_release('esc')
        reset = getInput(
            "Y", "y", "N", "n", message="Do you want to play again?", banned=", "
        )
        if reset.lower()[0] == "y":
            edit = getInput(
                "Y",
                "y",
                "N",
                "n",
                message="Do you want to Modify the game? i.e. mines, or grid.",
                banned=", ",
            )
            size = self.LIMIT
            mines = self.MINE_COUNT
            if edit.lower()[0] == "y":
                size = getInput("Numbers", message="Grid Size")
                mines = getInput("num", message="Mines")
            keyboard.unhook(self.pressor)
            self.__init__(size, mines)


def main():
    board = MineSweeper()
    keyboard.wait("esc")


if __name__ == "__main__":
    main()
