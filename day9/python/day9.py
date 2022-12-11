
def read_file(file_name):
    with open(file_name, 'r') as fd:
        moves = []
        for line in fd.readlines():
            moves.append([line.split()[0], int(line.split()[1])])
        return (moves)

def move_head(pos, istruction):
    if istruction[0] in ['L', 'D']:
        rev = -1
    elif istruction[0] in ['R', 'U']:
        rev = 1
    if istruction[0] in ['L', 'R']:
        pos['x'] += istruction[1] * rev
    elif istruction[0] in ['D', 'U']:
        pos['y'] += istruction[1] * rev

def move_tail(pos, istruction):
    pass

def check_tail(pos_h, pos_t):
    pass

def count_tail(file_name):
    pos_h = {'x': 0, 'y': 0}
    pos_t = {'x': 0, 'y': 0}
    past_t_pos = [pos_t]
    istructions = read_file(file_name)
    for istruction in istructions:
        move_head(pos_h, istruction)
        if check_tail(pos_h, pos_t):
            move_tail(pos_t, istruction)
            if pos_t not in past_t_pos:
                past_t_pos.append(pos_t)
        

if __name__ == "__main__":
    print("tail tiles:", count_tail("..\\input2.txt"))