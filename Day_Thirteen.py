import json

def parser():
    result = []
    with open("input13.txt", "r") as fp:
        pairs = fp.read().split('\n\n')
        for pair in pairs:
            result.append(tuple(json.loads(lst) for lst in pair.split('\n')))

    return result

def compare(item_a, item_b):
    if isinstance(item_a, int) and isinstance(item_b, int):
        if item_a == item_b:  return None
        return item_a < item_b

    elif isinstance(item_a, list) and isinstance(item_b, list):
        for index in range(len(item_a)):
            
            if index + 1 > len(item_b): return False
            if (check := compare(item_a[index], item_b[index])) is not None: return check
        
        if len(item_a) < len(item_b): return True

    elif isinstance(item_a, list):
        if (check := compare(item_a, [item_b])) is not None: return check
    
    else:
        if (check := compare([item_a], item_b)) is not None: return check

def process(pairs):
    result = 0

    for pair_index in range(len(pairs)):
        list_a, list_b = pairs[pair_index]
        val = compare(list_a, list_b)
        if val is None or val:
            result += pair_index + 1

    return result

def process2(pairs):
    new_list = [[[2]], [[6]]]
    for pair in pairs:
        new_list.extend(pair)

    swapped = False
    for j in range(len(new_list)-1):
        for i in range(len(new_list)-1):
            a = new_list[i]
            b = new_list[i+1]
            if not compare(a, b):
                new_list[i] = b
                new_list[i+1] = a
                swapped = True
        
        if not swapped:
            return new_list
    
    return (new_list.index([[2]])+1) * (new_list.index([[6]])+1)

data = parser()
print(process(data))
print(process2(data))
