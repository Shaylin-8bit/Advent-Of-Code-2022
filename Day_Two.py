def parser():
    with open('input2.txt') as fp:
        return [line.split() for line in fp.readlines()]

def process(pairs):
    pair_map = {
        'X': (1, 'C', 'A'),
        'Y': (2, 'A', 'B'),
        'Z': (3, 'B', 'C')
    }

    return sum([pair_map[pair[1]][0] + (6 if pair_map[pair[1]][1] == pair[0] else (3 if pair_map[pair[1]][2] == pair[0] else 0)) for pair in pairs])


def process2(pairs):
    pair_map = {
        'X': (0, {'A': 3, 'B': 1, 'C': 2}),
        'Y': (3, {'A': 1, 'B': 2, 'C': 3}),
        'Z': (6, {'A': 2, 'B': 3, 'C': 1})
    }

    return sum([pair_map[pair[1]][0] + pair_map[pair[1]][1][pair[0]] for pair in pairs])

print(process(parser()))
print(process2(parser()))
