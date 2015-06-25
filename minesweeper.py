from random import randint

class Minesweeper:
    def __init__(self, height, width, mines):
        self.grid = [[0 for i in xrange(width)] for i in xrange(height)]
        for i in xrange(mines):
            rand1 = randint(0, height-1)
            rand2 = randint(0, width-1)
            while self.grid[rand1][rand2] != 0:
                rand1 = randint(0, height-1)
                rand2 = randint(0, width-1)
            self.grid[rand1][rand2] = 'X'

    def __str__(self):
        output = ""
        for row in self.grid:
            for position in row:
                output = output + " " + str(position) + " "
            output = output + "\n"
        return output
