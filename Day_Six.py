def process(start_length):
    with open("input6.txt", "r") as fp:
        current_chars = list(fp.read(start_length))
        current_index = start_length

        while len(set(current_chars)) != start_length:
            current_chars[current_index % start_length] = fp.read(1)
            current_index += 1

        return (''.join(current_chars), current_index)

print(process(4))
print(process(14))
