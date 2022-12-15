from intervaltree import IntervalTree

class Grid:
    def __init__(self, receivers, min_x, min_y, max_x, max_y):
        self.receivers = receivers
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y

    def num_impossible_on_y(self, y):
        ranges = [x for receiver in self.receivers if (x := receiver.range_on_y(y)) is not None]
        tree = IntervalTree.from_tuples(ranges)        
        tree.merge_overlaps()
        
        beacons_on_line = set(i.closest for i in self.receivers if i.closest[1] == y)
        sensors_on_line = set(i.position for i in self.receivers if i.position[1] == y)

        return sum([i.end - i.begin for i in tree]) - len(beacons_on_line) - len(sensors_on_line)

    def get_ranges_y(self, y):
        ranges = [x for receiver in self.receivers if (x := receiver.range_on_y(y)) is not None]
        tree = IntervalTree.from_tuples(ranges)        
        tree.merge_overlaps(strict=False)

        return tree

    def find_coords(self, rng):
        x = y = percent = 0

        for i in range(rng+1):
            ranges = self.get_ranges_y(i)
            new_percent = int(i / rng * 100)

            if new_percent > percent: print((percent := new_percent), "percent scanned")

            if len(ranges)-1: 
                x, y = list(ranges.at(0))[0].end, i
                break

        return x * 4000000 + y

class Receiver:
    def __init__(self, position, closest):
        self.closest  = closest
        self.position = position
        self.range    = abs(position[0] - closest[0]) + abs(position[1] - closest[1])

    def range_on_y(self, y):
        mod = self.range - abs(y - self.position[1])
        result = self.position[0] - mod, self.position[0] + mod
        return (result[0], result[1] +1) if result[0] <= result[1] else None

def parser():
    receivers = []

    min_x = None
    max_x = None

    min_y = None
    max_y = None
    
    with open("input15.txt", "r") as fp:
        receivers_data = [tuple(int(word.strip(':').strip(',').split('=')[-1]) for word in line.split() if '=' in word) for line in fp.readlines()]
        coords = []

        for receiver in receivers_data:
            receivers.append(Receiver(receiver[0:2], receiver[2:]))
            coords.append(receiver[0:2])
            coords.append(receiver[2: ])

        for coord in coords:
            x, y = coord
            if min_x is None or x < min_x: min_x = x
            if max_x is None or x > max_x: max_x = x
            if min_y is None or y < min_y: min_y = y
            if max_y is None or y > max_y: max_y = y

    return Grid(receivers, min_x, min_y, max_x, max_y)

grid = parser()

part1 = grid.num_impossible_on_y(2000000)
part2 = grid.find_coords(4000000)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
