class Node:
    def __init__(self, next_node, last_node, start_position):
        self.next = next_node
        self.last = last_node
        self.position = start_position
        self.positions = [start_position.copy()]

class Rope:
    def __init__(self, length):
        self.head = Node(None, None, [0, 0])
        self.direction_map = {
            'R': ( 1,  0),
            'L': (-1,  0),
            'U': ( 0,  1),
            'D': ( 0, -1),
        }

        for i in range(length-1):
            self.append([0, 0])

    def get_tail(self):
        current = self.head
        while current.next is not None:
            current = current.next

        return current

    def append(self, start_position):
        tail = self.get_tail()
        tail.next = Node(None, tail, start_position)

    def pull(self, move):
        direction, units = move
        mod = self.direction_map[direction]

        for unit in range(units):
            self.head.position[0] += mod[0]
            self.head.position[1] += mod[1]

            for node in self:
                if node.last is not None:
                    move = False
                    x_difference = abs(node.position[0] - node.last.position[0])
                    y_difference = abs(node.position[1] - node.last.position[1])

                    if (x_difference > 1 and y_difference) or (y_difference > 1 and x_difference):
                        node.position[0] += 1 if node.position[0] < node.last.position[0] else -1
                        node.position[1] += 1 if node.position[1] < node.last.position[1] else -1
                        move = True

                    elif x_difference > 1:
                        node.position[0] += 1 if node.position[0] < node.last.position[0] else -1
                        move = True

                    elif y_difference > 1:
                        node.position[1] += 1 if node.position[1] < node.last.position[1] else -1
                        move = True

                    if move and (node.position not in node.positions):  
                        node.positions.append(node.position.copy())

    def pull_multiple(self, moves):
        for move in moves:
            self.pull(move)
    
    def __iter__(self):
        self.pos = self.head
        return self

    def __next__(self):
        if self.pos.next is not None:
            self.pos = self.pos.next
        else:
            raise StopIteration

        return self.pos



def parser():
    with open("input9.txt", "r") as fp:
        return [(i.split()[0], int(i.split()[1])) for i in fp.readlines()]

def process():
    moves = parser()

    rope1 = Rope(2)
    rope2 = Rope(10)

    rope1.pull_multiple(moves)
    rope2.pull_multiple(moves)

    return len(rope1.get_tail().positions), len(rope2.get_tail().positions)

print(process())
