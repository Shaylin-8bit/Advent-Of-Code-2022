def parser():
    with open("scratch.txt", "r") as  fp:
        commands = ['cd', 'ls']

        # removes $ and splits to list
        lines = [line.replace('$', '').split() for line in fp.readlines()]

        # removes file names, and dir from directories
        for line in lines:
            if line[0] == 'dir': 
                line.pop(0)
            elif line[0].isnumeric():
                line.pop(1)

        # organize commands into command and output
        result = []
        for i in lines:
            if i[0] in commands:
                result.append([' '.join(i), []])

            else:
                result[-1][1].append(i[0])
 
        return result


class Directory:
    def __init__(self, name, parent, children, files_size):
        self.name = name
        self.parent = parent
        self.children = children
        self.files_size = files_size
        self.total_size = 0

    def child(self, name):
        return [i for i in self.children if i.name == name][0] or None

    def __str__(self):
        return f"(name: {self.name}, size: {self.files_size}, total_size: {self.total_size}, children: {', '.join([str(child) for child in self.children])})"

    def __repr__(self):
        return f"(name: {self.name}, size: {self.files_size}, total_size: {self.total_size}, children: {', '.join([str(child) for child in self.children])})"

def get_structure(commands):
    # set top and current directory
    top_directory = Directory('/', None, [], 0)
    current_directory = top_directory
    
    # for each command, either move directories or create new ones for ls
    for command in commands:
        cmd, out = command
        if cmd == 'cd /':
            current_directory = top_directory

        elif cmd == 'cd ..':
            current_directory = current_directory.parent

        elif 'cd' in cmd:
            current_directory = [child for child in current_directory.children if child.name == cmd.split()[1]][0]
        
        elif cmd == 'ls':
            current_directory.children = [Directory(i, current_directory, [], 0) for i in out if i.isalpha()]
            current_directory.files_size = sum([int(i) for i in out if i.isnumeric()])

    return top_directory

# set directory sizes with recursions caculating file sizes plus children
def set_sizes(directory):
    directory.total_size = directory.files_size + sum([set_sizes(child) for child in directory.children])
    return directory.total_size

def setup():
    parsed = parser()
    directory = get_structure(parsed)
    set_sizes(directory)
    return directory

def process(directory, maximum):
    return (directory.total_size if directory.total_size <= maximum else 0) + sum([process(child, maximum) for child in directory.children])

def process2(directory, size_needed, system_size, used_size):
    return min([directory.total_size if used_size - directory.total_size + size_needed <= system_size else system_size, *[process2(child, size_needed, system_size, used_size) for child in directory.children]])


top = setup()
maximum = 100000
print(process(top, 100000))

total = 70000000
needed = 30000000
print(process2(top, needed, total, top.total_size))
