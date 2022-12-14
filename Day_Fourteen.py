class Grid:
    def __init__(self, width, height, paths, start):
        self.start = start
        self.sand = 0
        self.content = [['.' for i in range(width)] for j in range(height)]

        for path in paths:
            x = None
            y = None
            for point in path:
                new_y, new_x = point
                if x is not None and y is not None:
                    while x != new_x:
                        self.content[x][y] = '#'
                        if x < new_x:
                            x += 1
                        else:
                            x -= 1

                    while y != new_y:
                        self.content[x][y] = '#'
                        if y < new_y:
                            y += 1
                        else:
                            y -= 1
                
                    self.content[x][y] = '#'

                else:
                    x = new_x
                    y = new_y

    def drop_sand(self):
        y, x = self.start
        # opening filled
        if self.content[y][x] != '.': return False

        print(x, y)
        while True:
            # check if can move down
            if y + 1 < len(self.content):
                # check straight down
                if self.content[y+1][x] == '.':
                    y += 1

                # check down left
                elif x - 1 >= 0:
                    if self.content[y+1][x-1] == '.':
                        y += 1
                        x -= 1
                        
                # check down right
                    
                    elif x + 1 < len(self.content[0]):
                        if self.content[y+1][x+1] == '.':
                            y += 1
                            x += 1
                    
                # set position to sand
                        else:
                            self.content[y][x] = '0'
                            self.sand += 1
                            return True

                # sand fell out left side
                else:
                    return False  

                # sand fell into abyss
            else:
                return False

    def __repr__(self):
        return '\n'.join([''.join(row) for row in self.content])

def parser():
    with open("input14.txt", "r") as fp:

        min_x = None
        min_y = 0
        
        max_x = 0
        max_y = 0

        paths = [[[int(coord) for coord in point.split(',')] for point in path.strip().split('->')] for path in fp.readlines()]
        
        for path in paths:
            for point in path:
                x, y = point
                if min_x is None or min_x > x: min_x = x
                if max_x < x: max_x = x
                if max_y < y: max_y = y
        
        paths1 = [[[point[0] - min_x, point[1] - min_y] for point in path] for path in paths]
        start = (0, 500-min_x)
        

        # second part
        paths2 = paths1.copy()
        floor_y = max_y + 2

        # for extra floor width
        paths2 = [[[point[0]+floor_y, point[1]] for point in path] for path in paths2]
        paths2.append([(0, floor_y), (floor_y*3, floor_y)])
        start2 = (0, 500-min_x+floor_y)

        return Grid(max_x+1-min_x, max_y+1-min_y, paths1, start), Grid(floor_y * 3 +1, max_y+1-min_y+2, paths2, start2)
        

def process(data):
    pass

grid, grid2 = parser()

while grid.drop_sand(): pass
while grid2.drop_sand(): pass

print(grid)
print(grid2)
