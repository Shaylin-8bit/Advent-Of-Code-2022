import math

class Monkey:
    def __init__(self, items, op_input, test, if_true, if_false):
        self.items    = items.copy()
        self.test     = test
        self.next     = (if_false, if_true)
        self.op_input = op_input.copy()
        self.times    = 0

    def cycle(self, limiter=0):
        result = []
        for i in range(len(self.items)):
            self.times += 1
            item = self.items[i]
            mod  = int(self.op_input[1]) if self.op_input[1].isnumeric() else item

            match self.op_input[0]:
                case '*': self.items[i] = item * mod
                case '/': self.items[i] = item / mod
                case '+': self.items[i] = item + mod
                case '-': self.items[i] = item - mod

            if limiter: 
                self.items[i] %= limiter
            else:
                self.items[i] = self.items[i] // 3
            result.append(self.next[self.items[i] % self.test == 0])

        return result

def parser():
    with open("input11.txt", "r") as fp:
        result = []
        monkeys = fp.read().split('\n\n')
        for monkey in monkeys:
            lines = monkey.split('\n')[1:]
            items = [int(item.strip(',')) for item in lines[0].split() if item.strip(',').isnumeric()]
            op_input = lines[1].split()[-2:]
            test = int(lines[2].split()[-1])
            true = int(lines[3].split()[-1])
            false = int(lines[4].split()[-1])

            result.append(Monkey(items, op_input, test, true, false))
    
    return result

def process(monkeys, rounds):
    for round in range(rounds):
        for monkey in monkeys:
            pass_to = monkey.cycle(0)
            for i in pass_to:
                item = monkey.items.pop(0)
                next_monkey = monkeys[i]
                next_monkey.items.append(item)

    in_order = sorted([monkey.times for monkey in monkeys])
    return in_order[-1] * in_order[-2]

def process2(monkeys, rounds):
    tests = [monkey.test for monkey in monkeys]
    limiter = 1
    for test in tests: limiter *= test

    for round in range(rounds):
        for monkey in monkeys:
            pass_to = monkey.cycle(limiter)
            for i in pass_to:
                item = monkey.items.pop(0)
                next_monkey = monkeys[i]
                next_monkey.items.append(item)

    in_order = sorted([monkey.times for monkey in monkeys])
    return in_order[-1] * in_order[-2]

print(process(parser(), 20))
print(process2(parser(), 10000))
