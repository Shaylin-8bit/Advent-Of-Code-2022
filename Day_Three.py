def parser():
    with open("input3.txt") as fp:
        return [(line[0: len(line)//2], line[len(line)//2: -1]) for line in fp.readlines()]

def parser2():
    with open("input3.txt") as fp:
        lines = fp.readlines()
        result = []
        for i in range(len(lines)):
            if not i % 3: result.append([])
            result[-1].append(lines[i].strip('\n'))

        return result

priorities = lambda l: ord(l) - ord(('A', 'a')[l.islower()]) + (27, 1)[l.islower()]

def process(rucksacks):
    return sum([priorities(''.join(set(sack[0]).intersection(sack[1]))) for sack in rucksacks])

def process2(groups):
    return sum([priorities(''.join(set(group[0]).intersection(group[1], group[2]))) for group in groups])
    
print(process(parser()))
print(process2(parser2()))
