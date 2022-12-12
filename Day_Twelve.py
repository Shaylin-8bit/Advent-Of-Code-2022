class Node:
    def __init__(self, value, connections, index):
        self.index = index
        self.value = value
        self.connections = connections
        self.distance = None
        self.tracked = False

    def __repr__(self):
        return f"Coords: {self.index},\t Value: {self.value},\t Distance: {self.distance},\t Tracked: {self.tracked},\t Connections {self.connections}"

class Map:
    def __init__(self, start, end):
        self.start   = start
        self.end     = end
        self.content = []

def parser():
    with open("input12.txt", "r") as fp:
        grid  = []
        lines = fp.readlines()
        start = None
        end   = None

        for line_index in range(len(lines)):
            grid.append([])
            line = lines[line_index].strip()
            for char_index in range(len(line)):
                char = line[char_index]
                
                if char == 'S':
                    start = (line_index, char_index)
                    grid[-1].append(0)

                elif char == 'E':
                    end = (line_index, char_index)
                    grid[-1].append(ord('z') - ord('a') + 1)
                
                else:
                    grid[-1].append(ord(char) - ord('a') + 1)

        return grid, start, end


def build_map(grid, start, end):
    result = Map(start, end)
    for line_index in range(len(grid)):
        result.content.append([])
        line = grid[line_index]

        for point_index in range(len(line)):
            point = line[point_index]

            connections = []
            if (point_index + 1 < len(line)) and line[point_index + 1] <= point + 1:
                connections.append((line_index, point_index + 1))

            if (point_index) and line[point_index - 1] <= point + 1:
                connections.append((line_index, point_index - 1))

            if (line_index + 1 < len(grid)) and grid[line_index + 1][point_index] <= point + 1:
                connections.append((line_index + 1, point_index))

            if (line_index) and grid[line_index - 1][point_index] - 1 <= point:
                connections.append((line_index - 1, point_index))

            result.content[-1].append(Node(point, connections.copy(), (line_index, point_index)))
    
    return result


def process(grid):
    end_x, end_y = grid.end
    end = grid.content[end_x][end_y]
    
    start_x, start_y = grid.start
    start = grid.content[start_x][start_y]

    start.distance = 0

    next = [start]

    while end.distance is None:
        current = next.copy()
        next = []

        stuck = True

        for point in current:
            point.tracked = True
            for i in point.connections:
                connection = grid.content[i[0]][i[1]]
                if connection.distance is None:
                    stuck = False
                    connection.distance = point.distance + 1
                    next.append(connection)

        if stuck:
            return None

    return end.distance


def process2():
    parsed = parser()
    base = build_map(*parsed)
    targets = []

    for line_index in range(len(base.content)):
        line = base.content[line_index]
        for point_index in range(len(line)):
            point = line[point_index]
            
            if point.value == 1:
                targets.append((line_index, point_index))
    
    results = []
    for target_index in range(len(targets)):
        print(f"{targets[target_index]} - {target_index} / {len(targets)}")
        grid = build_map(*parsed)
        grid.start = targets[target_index]
        results.append(process(grid))

    return min([i for i in results if i is not None])

map = build_map(*parser())
map2 = build_map(*parser())

part1 = process(map)
part2 = process2()

print(part1, part2)
