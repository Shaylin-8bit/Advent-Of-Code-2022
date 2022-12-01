def parser():
    with open('input.txt') as fp:
        return [[int(calories) for calories in elf.split('\n')] for elf in ''.join(fp.readlines()).split('\n\n')]
        
def process(calories):
    return max([sum(lst) for lst in calories])

def process2(calories):
    return sum(sorted([sum(lst) for lst in calories])[:-4:-1])

print(process(parser()))
print(process2(parser()))
