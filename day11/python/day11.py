class MonkeyBreed():
    def __init__(self):
        self.monkeys = []

    def add_monkey(self, new_monkey):
        if isinstance(new_monkey, Monkey):
            self.monkeys.append(new_monkey)
    
    def get_monkey(self, id):
        for monkey in self.monkeys:
            if id == monkey.id:
                return monkey

    def play_round(self, times, worry_level):
        for i in range(times):
            for monkey in self.monkeys:
                for id, new_value in monkey.play_with_items(worry_level):
                    self.get_monkey(id).add_item(new_value)
                    monkey.no_pass += 1
                monkey.items.clear()
        
    def get_2_worst_monkeys(self):
        self.monkeys.sort(key=lambda m1 : m1.no_pass)
        return self.monkeys[-1].no_pass * self.monkeys[-2].no_pass

    def parse_monkeys(self, file_name):
        with open(file_name, 'r') as fd:
            while True:
                line = fd.readline().rstrip()
                if not line:
                    break
                else:
                    monkey = Monkey(int(line[-2]))
                line = fd.readline().rstrip()
                for item in line[18:].split(", "):
                    monkey.add_item(item)
                line = fd.readline().rstrip()
                monkey.set_ops(line.split()[-3:])
                line = fd.readline().rstrip()
                monkey.div = int(line.split()[-1])
                line = fd.readline().rstrip()
                monkey.true_monkey = int(line.split()[-1])
                line = fd.readline().rstrip()
                monkey.false_monkey = int(line.split()[-1])
                self.add_monkey(monkey)
                fd.readline()


class Monkey():
    def __init__(self, id):
        self.id = id
        self.items = []
        self.operation = None
        self.div = 0
        self.true_monkey = -1
        self.false_monkey = -1
        self.no_pass = 0

    def add_item(self, new_item):
        self.items.append(int(new_item))

    def set_ops(self, ops):
        value = None
        same = False
        if ops[0] != "old":
            value = int(ops[0])
        elif ops[2] != "old":
            value = int(ops[2])
        else:
            same = True
        if ops[1] == '+':
            if same:
                self.operation = lambda worry : worry + worry
            else:
                self.operation = lambda worry : worry + value
        elif ops[1] == '*':
            if same:
                self.operation = lambda worry : worry * worry
            else:
                self.operation = lambda worry : worry * value

    def check(self, value):
        if value % self.div == 0:
            return self.true_monkey, value
        else:
            return self.false_monkey, value

    def play_with_items(self, worry_level):
        for item in self.items:
            new_value = self.operation(item) // worry_level
            yield self.check(new_value)


def fetch_items(file_name, times, worry_level):
    monkeys = MonkeyBreed()
    monkeys.parse_monkeys(file_name)
    monkeys.play_round(times, worry_level)
    return (monkeys.get_2_worst_monkeys())

if __name__ == "__main__":
    rounds, worry_div = 20, 3
    print("worst 2 monkeys, in {} rounds, worry level={}: {}".format(rounds, worry_div, fetch_items("..\\input.txt", rounds, worry_div)))
    rounds, worry_div = 10000, 1
    print("worst 2 monkeys, in {} rounds, worry level={}: {}".format(rounds, worry_div, fetch_items("..\\input2.txt", rounds, worry_div)))