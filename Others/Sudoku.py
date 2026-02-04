import requests
import tkinter


class SudokuBoard:
    SIZE = 9
    board = [[]]
    URL = "https://sudoku-api.vercel.app/api/dosuku?query={newboard(limit:1){grids{value}}}"

    def __init__(self):
        try:
            response = requests.get(
                "https://sudoku-api.vercel.app/api/dosuku?query={newboard(limit:1){grids{value}}}"
            )
            if response.status_code == 200:
                data = response.json()
                self.board = data["newboard"]["grids"][0]["value"]
        except Exception as e:
            print(e)
            del self

    def col(self, ColumnIndex):
        column = [i[ColumnIndex] for i in self.board]
        return set(column)

    def box(self, BoxIndex):
        if not 0 < BoxIndex <= 9:
            return -1
        else:
            indices = (1, 4, 7)
            mod = indices[(BoxIndex - 1) % 3]
            box = []
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    box.append(self.board[mod + i][mod + j])
            return set(box)

    def weightRow(self, RowIndex):
        return len(set(self.board[RowIndex]))

    def weightCol(self, ColumnIndex):
        return len(self.col(ColumnIndex))

    def weightBox(self, BoxIndex):
        if not 0 < BoxIndex <= 9:
            return -1
        else:
            return len(self.box(BoxIndex))

    def print(self):
        print("-" * (self.SIZE * 4 + 1))
        for i in range(self.SIZE):
            for j in self.board[i]:
                if j != 0:
                    print(f"|{j: 2d}", end=" ")
                else:
                    print("|  ", end=" ")
            print("|", end="\n|")
            if i == self.SIZE - 1:
                print("\b-" + "-" * self.SIZE * 4)
            elif i % 3 == 2:
                print(("=" * 11 + "|") * 3)
            else:
                print(("-" * 11 + "|") * 3)


class SudokuChecker(SudokuBoard):
    def __init__(self, ToCheck: type[SudokuBoard]):
        self.SIZE = 9
        self.board = ToCheck.board

    def isFull(self):
        empty = sum([i.count(0) for i in self.board])
        return empty == 0

    def couldHave(self, cord):
        x, y = cord
        allNum = set(range(1, 10))
        canBe = set(self.board[x]) | set(self.col(y))
        canBe = allNum - (canBe | set(self.box(x // 3 + y // 3 + 1)))
        return canBe

    def emptyPlaces(self):
        places = [
            (i, j)
            for i in range(self.SIZE)
            for j in range(self.SIZE)
            if self.board[i][j] == 0
        ]
        return places

    def check(self):
        for i in range(self.SIZE):
            if self.weightBox(i) != 9:
                return False
        for i in range(self.SIZE):
            if self.weightRow(i) != 9:
                return False
        for i in range(self.SIZE):
            if self.weightCol(i) != 9:
                return False
        return True

class SudokuUI(SudokuChecker):
    def __init__(self, ToCheck):
        super().__init__(ToCheck)

    def run(self):
        pass


# class SudokuSolver(SudokuChecker, SudokuBoard):
#     def __init__(self, ToSolve: type[SudokuBoard]):
#         self.board = ToSolve.board
#         self.SIZE = ToSolve.SIZE

#     def solve(self):
#         if self.isFull():
#             print("It's Full. Sorry.")
#         while not self.isFull():
#             for i, j in self.emptyPlaces():
#                 if len(self.couldHave((i, j))) == 1:
#                     print(f"{i}, {j} => {self.couldHave((i,j))}")
#                     self.board[i][j] = self.couldHave((i, j)).pop()
#                     self.print()
#         print(self.check())
#         self.print()


if __name__ == "__main__":
    x = SudokuUI(SudokuBoard())

