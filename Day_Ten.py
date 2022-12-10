def parser():
    with open("input10.txt", "r") as fp:
        lines = fp.readlines()
        result = [0]
        
        for line_index in range(len(lines)):
            line = lines[line_index]
            parts = line.strip().split()
            if parts[0] == 'addx':
                result.extend([0, int(parts[1])])

            else:
                result.append(0)
            
        return result


def compute(instructions):
    full = []
    interesting = []
    x = 1
    cycle = 0
    for instruction in instructions:

        full.append(x)
        
        if cycle % 40 - 20 == 0:
            interesting.append(x * cycle)

        cycle += 1
        x += instruction

    return full, interesting


def draw(computed):

    print('\n\n')

    for i in range(6):
        for j in range(1, 41):
            value = computed[i*40 + j]
            if j in [value, value+2, value+1]:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print('\n\n')

computed, part1 = compute(parser())
draw(computed)
print("part 1:", sum(part1))
