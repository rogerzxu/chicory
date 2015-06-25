class Minesweeper:
    def __init__(self, height, width, mines):
        self.grid = [[0 for i in xrange(height)] for i in xrange(width)]