# 0 = blank
# 1 = red
# 2 = yellow

# Defines Board object
class Board:
    # Instantiates & defines variables turn & grid.
    # Points on grid are defined (y,x). y is the row, x is the column.
    def __init__(self):
        self.grid = [[0 for x in range(7)] for y in range(6)]
        self.turn = 1 # red's turn (yellow is 2)
        # print(self.grid)

    # places a token on Board grid at a given x position, the color of the current turn
    def placeToken(self, pos, grid=None):
        grid = grid if grid is not None else self.grid
        # find y posititon of token
        x = pos-1 # for the sake of preserving OUR sanity
        y = -1
        passed = False
        for row in grid:
            y+=1
            if row[x] == 0:
                passed = True
                break

        # Returns no change if selected row is full
        if not passed:
            print("All columns are filled! Please play a different move ;-;")
            return grid

        # adds token to return grid
        newGrid = grid
        newGrid[y][x] = self.turn
        return newGrid

    # updates Board grid & turn color
    def updateGrid(self, grid):
        # updates Board grid
        self.grid = grid
        self.turn = 3-(self.turn) # Flips turns: 1 = 2, 2 = 1.
        return self

    # displays Board grid
    def display(self):
        print("\n 1  2  3  4  5  6  7")  # column headers

        for row in self.grid[::-1]:  # top to bottom
            line = "|"
            for cell in row:  # left to right
                if cell == 1:
                    line += "🔴|"
                elif cell == 2:
                    line += "🟡|"
                else:
                    line += "🔘|"
            print(line)
        print()  # extra newline for spacing

    # returns True if the entire board is full (no legal moves remain)
    def is_full(self, grid=None):
        g = grid if grid is not None else self.grid
        # top row is index 5 because grid[0] is the bottom row
        return all(g[5][c] != 0 for c in range(7))

    # returns True if win detected at specified position on specified grid, False if not
    def checkWin(self, pos, grid=None):
        grid = grid if grid is not None else self.grid
        # find y of token & token color
        x = pos-1 # :]
        y=-1
        for i in range(6):
            currCheck = grid[i][x]
            if currCheck == 0:
                break
            y+=1
        if y == -1:
            print("No token in this row!")
            return False
        turn = grid[y][x] # independent of self.turn

        # Check vertical win
        cCol = 0
        for row in grid:
            if row[x] == turn:
                cCol += 1
                if cCol >= 4:
                    return True
            else:
                cCol = 0

        # Check horizantal win
        rowCount = 0
        for i in grid[y]:
            if i == turn:
                rowCount += 1
                if rowCount >= 4:
                    return True
            else:
                rowCount = 0


        # Check upward diagonal win
        """diffCof = max(x, y) - min(x, y)
        startingPoint = (x - diffCof, y - diffCof)"""
        xPos = x - min(x, y)
        yPos = y - min(x, y)
        # commented code below is potentially more efficient but more lines
        """if x-y > 0:
            xPos = x-y
        else:
            yPos = y-x"""
        diagCount = 0
        for i in range(min(7-xPos, 6-yPos)):
            if grid[yPos+i][xPos+i] == turn:
                diagCount += 1
                if diagCount >= 4:
                    return True
            else:
                diagCount = 0

        # Check downward diagonal win
        xPos = x + min(6-x, y)
        yPos = y - min(6-x, y)
        """if (6-x)-y > 0:
            xPos = x+y
        else:
            yPos = y-(6-x)"""
        diagCount = 0
        for i in range(min(1+xPos, 6-yPos)):
            if grid[yPos+i][xPos-i] == turn:
                diagCount += 1
                if diagCount >= 4:
                    return True
            else:
                diagCount = 0
        # If no wins detected, return false
                # If board is full and no wins, it's a draw
        if self.is_full(grid):
            print("The game is. ..a draw!")
            return True
        return False

    def minmax(self, ):




# Board object
board = Board()

# adding tokens


board.updateGrid(board.placeToken(1))
board.updateGrid(board.placeToken(2))
board.updateGrid(board.placeToken(2))
board.updateGrid(board.placeToken(3))
board.updateGrid(board.placeToken(4))
board.updateGrid(board.placeToken(4))
board.updateGrid(board.placeToken(4))
board.updateGrid(board.placeToken(4))
board.updateGrid(board.placeToken(6))
board.updateGrid(board.placeToken(5))
board.updateGrid(board.placeToken(5))
board.updateGrid(board.placeToken(3))
board.updateGrid(board.placeToken(3))
board.updateGrid(board.placeToken(1))
board.updateGrid(board.placeToken(3))

# win test checks
print(f"Win: {board.checkWin(4)}")
print(f"Win: {board.checkWin(5)}") # needs to be passed correct token position to detect win

# self explanatory
board.display()


#how to run
#python3 main.py"""
#0 = blank
#1 = red
#2 = yellow


#how to run
#python3 main.py"""