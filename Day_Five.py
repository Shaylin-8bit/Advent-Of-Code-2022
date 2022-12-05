def parser():
    with open("input5.txt", "r") as fp:
        stack_stream = []
        line = fp.readline()
        while not any(char.isdigit() for char in line):
            stack_stream.append(''.join([char for char in line.strip('\n').replace('    ', 'a') if char.isalpha()])) 
            line = fp.readline()
        
        stacks = [[] for i in range(len(stack_stream[0]))]

        for i in range(len(stack_stream[0])):
            for j in range(len(stack_stream)):
                c = stack_stream[len(stack_stream) - 1 - j][i]
                if c != 'a':
                    stacks[i].append(c)

        commands = tuple(tuple(int(word) for word in line.split() if word.isnumeric()) for line in fp.readlines() if len(line) > 1)

        return (stacks, commands)

def process(stacks, commands, reverse=True):
    for command in commands:
        amount      = command[0]
        move_from   = stacks[command[1] - 1]
        section_len = len(move_from) - amount
        temp        = move_from[section_len:]

        if reverse: temp = reversed(temp)

        stacks[command[2] - 1].extend(temp)
        stacks[command[1] - 1] = move_from[:section_len]
    
    return ''.join([stack.pop() for stack in stacks])

print(process(*parser()))
print(process(*parser(), False))
