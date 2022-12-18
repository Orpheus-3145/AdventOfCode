def parse_line(line):
    return 0 if line == "noop" else int(line.split()[1])

def count_signals(file_name):
    X = 1
    C = 1
    i = 0
    tot_sig_sum = 0
    pause = False
    with open(file_name, 'r') as fd:
        instructions = fd.read().split('\n')
        while True:
            if pause:
                X += amount
                pause = False
            else:
                amount = parse_line(instructions[i])
                i += 1
                if amount:
                    pause = True
            C += 1
            if (C - 20) % 40 == 0:
                tot_sig_sum += C * X
            if i == len(instructions):
                break
    return tot_sig_sum

def draw_signals(file_name):
    pos = 1
    C = 1
    i = 0
    pause = False
    with open(file_name, 'r') as fd:
        instructions = fd.read().split('\n')
        while True:
            if C in range(pos, pos + 3):
                print("#", end="")
            else:
                print(".", end="")
            if pause:
                pos += amount
                pause = False
            else:
                amount = parse_line(instructions[i])
                i += 1
                if amount:
                    pause = True
            C += 1
            if C > 40:
                C -= 40
                print("")
            if i == len(instructions):
                break


if __name__ == "__main__":
    print("Totale somma instensità segnali:", count_signals("..\\input.txt"))
    draw_signals("..\\input.txt")