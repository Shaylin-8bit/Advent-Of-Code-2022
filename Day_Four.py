def parser():
    with open("input4.txt", "r") as fp:
        return [[[int(num) for num in pair.split('-')] for pair in line.strip('\n').split(',')] for line in fp.readlines()]

def process(pairs):
    helper = lambda pair: (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]) or (pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1])
    return sum([helper(pair) for pair in pairs])

def process2(pairs):
    helper = lambda pair: (pair[1][0] <= pair[0][0] <= pair[1][1]) or \
                          (pair[1][0] <= pair[0][1] <= pair[1][1]) or \
                          (pair[0][0] <= pair[1][0] <= pair[0][1]) or \
                          (pair[0][0] <= pair[1][1] <= pair[0][1])

    return sum([helper(pair) for pair in pairs])

print(process(parser()))
print(process2(parser()))
