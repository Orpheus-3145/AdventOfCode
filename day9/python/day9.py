
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
   
def touching(pos_h, pos_t):
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

def move_rope(pos_h, pos_t, istruction):
    coor, amount = istruction
    reverse = 1
    if amount < 0:
        reverse = -1
        amount *= -1
    for i in range(0, amount):
        pos_h[coor] += 1 * reverse
        current = pos_h
        if not touching(pos_h, pos_t):
            pos_t[coor] += 1 * reverse
            edges = check_edges(pos_h, pos_t)
            if edges:
                if coor == 'x':
                    pos_t['y'] += edges[0]
                elif coor == 'y':
                    pos_t['x'] += edges[1]

def print_snake(snake):
    for i in range(len(snake)):
        print(i, " -- ", snake[i])
    print("")
    for i in range(-10, 10):
        for j in range(-10, 10):
            if i == 0 and j == 0:
                print('{}'.format('|s' if {'x': 0, 'y': 0} not in snake else '|O'), end="")
            elif {'x': j, 'y': -i} in snake:
                print('|O', end="")
            else:
                print("|_", end="")  # ({:^2}:{:^2})".format(i if i > 0 else -i, j if j > 0 else -j), end="")
        print("")

def move_snake_bk(snake, istruction):
    coor, amount = istruction
    neg = 1
    if amount < 0:
        neg = -1
        amount *= -1
    for i in range(0, amount):
        snake[0][coor] += 1 * neg
        for i in range(1, 10):
            current = snake[i - 1]
            print("\t--", current, snake[i], end="")
            if not touching(current, snake[i]):
                print(" -- no touch", end="")
                snake[i][coor] += 1 * neg
                print(" -- fix move", snake[i], end="")
                edges = check_edges(current, snake[i])
                if edges:
                    print(" -- move diag", end="")
                    if coor == 'x':
                        snake[i]['y'] += edges[0]
                    elif coor == 'y':
                        snake[i]['x'] += edges[1]
                    print(snake[i])
                else:
                    print("")
            else:
                print("\nbreak!")
                break
    print_snake(snake)

def move_snake_bk_bk(snake, istruction):
    print("\t\t\tcoor:", istruction[0], "amount:", istruction[1])
    coor, amount = istruction
    neg = 1
    if amount < 0:
        neg = -1
        amount *= -1
    for i in range(0, amount):
        current_move = [coor, neg]
        single_move(snake[0], current_move)
        edge_move = []
        for i in range(1, 10):
            # print("\t--", snake[i - 1], snake[i], end="")
            if not touching(snake[i - 1], snake[i]):
                # print(" -- no touch", end="")
                single_move(snake[i], current_move)
                # print(" -- fix move", snake[i], end="")
                edges = check_edges(snake[i - 1], snake[i])
                if edges:  # and not edge_move:
                    # print(" -- move diag", end="")
                    if coor == 'x':
                        edge_move = ['y', edges[0]]
                    elif coor == 'y':
                        edge_move =  ['x', edges[1]]
                    single_move(snake[i], edge_move)
                # if edge_move:
                #     single_move(snake[i], edge_move)
                    # print(snake[i])
            else:
                # print("\nbreak!")
                break
        print_snake(snake)

def single_move(snake, istruction):
    coor = istruction[0]
    dir = istruction[1]
    snake[coor] += dir

def count_tail(file_name):
    pos_h = {'x': 0, 'y': 0}
    pos_t = {'x': 0, 'y': 0}
    snake = []
    for i in range(10):
        snake.append({'x': 0, 'y': 0})

    single_past_t_pos = [{'x': 0, 'y': 0}]
    snake_past_t_pos = [{'x': 0, 'y': 0}]
    istructions = read_file(file_name)
    for istruction in istructions:
        move_rope(pos_h, pos_t, istruction)
        move_snake_bk_bk(snake, istruction)
        if [pos_t['x'], pos_t['y']] not in single_past_t_pos:
            single_past_t_pos.append([pos_t['x'], pos_t['y']])
        if [snake[9]['x'], snake[9]['y']] not in snake_past_t_pos:     # passare l'elemento come dict invece che lista
            snake_past_t_pos.append([snake[9]['x'], snake[9]['y']])
        # print("\n\n")
    return len(single_past_t_pos), len(snake_past_t_pos)
        
if __name__ == "__main__":
    single, snake = count_tail("..//input2.txt")
    print("tail position: {}, snake tail position: {}".format(single, snake))