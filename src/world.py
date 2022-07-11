from src.tiles.tile import Tile
from src.utils.vector import Vector

class World():

    width = 11
    height = 9

    def __init__(self,player):

        self.grid = World.loadGrid("res/grids/temple1.grid")

        self.player = player

    def tick(self,handler):

        self.player.tick(handler,self.grid)

    def render(self,renderer,cam):

        cam.moveTo(self.player)

        for i in range(World.width):

            sx = self.player.pos.x - World.width/2
            x = int(sx) + i + (sx >= 0)
            if 0 <= x < len(self.grid):

                for j in range(World.height):

                    sy = self.player.pos.y - World.height/2
                    y = int(sy) + j + (sy >= 0)
                    if 0 <= y < len(self.grid[x]):

                        renderer.drawCamImage(Tile.getTile(self.grid[x][y]).texture,Vector(x,y),Vector(1,1),cam)

        self.player.render(renderer,cam)


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

        Tile.loadTileset(tilepath)

        return [[grid[j][i] for i in range(len(row))] for j,row in enumerate(grid)]
