from random import randint

class Minesweeper:
    def __init__(self, height, width, mines):
        self.height = height
        self.width = width
        self.grid = [['A' for i in xrange(width)] for i in xrange(height)]
        for i in xrange(mines):
            rand1 = randint(0, height-1)
            rand2 = randint(0, width-1)
            while self.grid[rand1][rand2] != 'A':
                rand1 = randint(0, height-1)
                rand2 = randint(0, width-1)
            self.grid[rand1][rand2] = 'X'

    def turn(self, row, column):
        if self.grid[row][column] == 'A':
            adjMines = 0
            adjEmpties = []
            for i in xrange(row-1, row+2):
                for j in xrange(column-1, column+2):
                    if i >= 0 and j >= 0 and i < self.height and j < self.width:
                        if self.grid[i][j] == 'X':
                            adjMines+=1
                        else:
                            adjEmpties.append((i,j))
            self.grid[row][column] = adjMines
            for adjEmpty in adjEmpties:
                self.turn(adjEmpty[0], adjEmpty[1])
            return 1
        elif self.grid[row][column] == 'X':
            return -1

    def __str__(self):
        output = ""
        for row in self.grid:
            for position in row:
                output = output + " " + str(position) + " "
            output = output + "\n"
        return output
