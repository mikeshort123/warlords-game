from src.tiles.tileset import Tileset
from src.utils.vector import Vector

class Grid:

    width = 11 # temporary
    height = 9

    def __init__(self):

        self.grid = Grid.loadGrid("res/grids/temple1.grid")


    def render(self,renderer,cam):

        for i in range(Grid.width):

            sx = cam.pos.x - Grid.width/2
            x = int(sx) + i + (sx >= 0)
            if 0 <= x < len(self.grid):

                for j in range(Grid.height):

                    sy = cam.pos.y - Grid.height/2
                    y = int(sy) + j + (sy >= 0)
                    if 0 <= y < len(self.grid[x]):

                        renderer.drawCamImage(self.grid[x][y].texture,Vector(x,y),Vector(1,1),cam)


    def getSolid(self,x,y):
        return self.grid[x][y].solid


    @staticmethod
    def loadGrid(fn):

        with open(fn) as f:
            d = f.read()

        tilepath = ""

        for i, c in enumerate(d):
            if c == "\n":
                break
            tilepath += c

        grid = []
        line = []
        current = ""

        for c in d[i+1:]:
            if c == ",":
                line.append(int(current))
                current = ""

            elif c == "\n":
                grid.append(line)
                line = []

            else:
                current += c

        tileset = Tileset(tilepath)

        return [[tileset.getTile(grid[j][i]) for i in range(len(row))] for j,row in enumerate(grid)]
