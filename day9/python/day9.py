
def parse_line(line):
    direction = line.split()[0]
    amount = int(line.split()[1])
    
    amount *= (-1 + 2 * int(direction in ['R', 'U']))            # if left of down change the direction
    direction = 'x' if direction in ['L', 'R'] else 'y'     # left or right ==> x axis, up or down ==> y axis
    return [direction, amount]

def read_file(file_name):
    with open(file_name, 'r') as fd:
        moves = []
        for line in fd.readlines():
            moves.append(parse_line(line))
        return (moves)
   
def check_touch(pos_h, pos_t):
    if pos_h == pos_t or check_edges(pos_h, pos_t):
        return True
    elif pos_t['x'] == pos_h['x'] and pos_t['y'] in [pos_h['y'] - 1, pos_h['y'] + 1]:
        return True
    elif pos_t['y'] == pos_h['y'] and pos_t['x'] in [pos_h['x'] - 1, pos_h['x'] + 1]:
        return True
    else:
        return False

def check_edges(pos_h, pos_t):
    if pos_h['x'] == pos_t['x'] + 1 and pos_h['y'] == pos_t['y'] + 1:
        return [1, 1]
    if pos_h['x'] == pos_t['x'] - 1 and pos_h['y'] == pos_t['y'] + 1:
        return [1, -1]
    if pos_h['x'] == pos_t['x'] + 1 and pos_h['y'] == pos_t['y'] - 1:
        return [-1, 1]
    if pos_h['x'] == pos_t['x'] - 1 and pos_h['y'] == pos_t['y'] - 1:
        return [-1, -1]
    else:
        return []

def move_rope(pos_h, pos_t, istruction, past_t_pos):
    coor = istruction[0]
    amount = istruction[1]
    reverse = 1
    if amount < 0:
        reverse = -1
        amount *= -1
    for i in range(0, amount):
        pos_h[coor] += 1 * reverse
        if not check_touch(pos_h, pos_t):
            pos_t[coor] += 1 * reverse
            edges = check_edges(pos_h, pos_t)
            if edges:
                if coor == 'x':
                    pos_t['y'] += edges[0]
                elif coor == 'y':
                    pos_t['x'] += edges[1]
            if [pos_t['x'], pos_t['y']] not in past_t_pos:
                past_t_pos.append([pos_t['x'], pos_t['y']])

def count_tail(file_name):
    pos_h = {'x': 0, 'y': 0}
    pos_t = {'x': 0, 'y': 0}
    past_t_pos = [[pos_h['x'], pos_h['y']]]
    istructions = read_file(file_name)
    for istruction in istructions:
        move_rope(pos_h, pos_t, istruction, past_t_pos)
    return (len(past_t_pos))
        
        

if __name__ == "__main__":
    print("tail tiles:", count_tail("..\\input.txt"))