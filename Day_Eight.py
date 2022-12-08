def parser():
    with open("scratch.txt", "r") as fp:
        return [[int(tree) for tree in row.strip()] for row in fp.readlines()]

def process(trees):
    total_visable_trees = 0
    best_tree = 0

    for row_index in range(len(trees)):
        row = trees[row_index]
        for tree_index in range(len(row)):
            score = 1
            tree  = row[tree_index]
            
            directions = [
                row[tree_index+1:],
                row[:tree_index][::-1],
                [trees[i][tree_index] for i in range(len(trees))][row_index+1:],
                [trees[i][tree_index] for i in range(len(trees))][:row_index][::-1],
            ]

            part1 = True
            for direction in directions:
                if part1 and not any([other_tree >= tree for other_tree in direction]):
                    total_visable_trees += 1
                    part1 = False
            
                visable_trees = 0
                for other_tree in direction:
                    visable_trees += 1
                    if other_tree >= tree:
                        break
                score *= visable_trees

            if score > best_tree:
                best_tree = score 
                
    return total_visable_trees, best_tree

print(process(parser()))
