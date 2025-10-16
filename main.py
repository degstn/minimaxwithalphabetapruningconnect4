#0 = blank
#1 = red
#2 = yellow


class Board:

    def __init__(self):
        self.grid = [[0 for _ in range(7)] for _ in range(6)]
        self.turn = 1 #red's turn (yellow is 2)
        print(self.grid)
        
    def placeToken(self, x):
        curr = -1
        # for row in self.grid:
        #     if row[x-1] != 0:
        #         pass
        #         break
        #     curr+=1
        
        for thing in self.grid[x-1]:
            if thing != 0:
                pass
                break
            curr = curr + 1
        
        #if curr == -1, then all columns are filled, if curr == len of row then it places on the very bottom
        if curr == -1:
            print("all columns are filled! Please play a different move!")
            return self.grid
        
        print("TEST")
        print(curr)
        newGrid = self.grid
        newGrid[x-1][curr] = self.turn
        self.turn = 3-(self.turn) # SHOULD FLIP TURNS 1 = 2, 2 = 1.
        return newGrid
    
    def updateGrid(self, grid):
        self.grid = grid
        return self
        
    def display(self):
        print("\n  1  2  3  4  5  6  7")  # column headers
        
        for row in range(6):
            for col in self.grid:
                line = ""
                cell = col[row-1]
                if cell == 1:
                    line += " 🔴"
                elif cell == 2:
                    line += " 🟡"
                else:
                    line += " 🔘"
                print(line)
        print()  # extra newline for spacing

        print("\n  1  2  3  4  5  6  7")  # column headers
    
        for row in range(6):  # top to bottom
            line = ""
            for col in range(7):  # left to right
                cell = self.grid[col-1][row-1]
                if cell == 1:
                    line += " 🔴"
                elif cell == 2:
                    line += " 🟡"
                else:
                    line += " 🔘"
            print(line)
        print()  # extra newline for spacing
    
    def gameOver():
        
        #vertical

        #horizantal

        #diagonal

        pass




    
testItem = Board()

testItem.updateGrid(testItem.placeToken(1))
testItem.updateGrid(testItem.placeToken(1))
testItem.updateGrid(testItem.placeToken(1))




print(testItem.grid)

print(testItem.display())


#how to run
#python3 main.py