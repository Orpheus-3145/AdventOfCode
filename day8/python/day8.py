def create_matrix(lines):
    mtx = []
    i = 0
    for line in lines:
        mtx.append([])
        for tree in [char for char in line if char != '\n']:
            mtx[i].append(int(tree))
        i += 1
    return (mtx)

def check_tree(mtx, i, j):
    side = len(mtx)
    to_check = mtx[i][j]
    for jj in range(0, j):
        if mtx[i][jj] >= to_check:
            break
    else:
        return True
    for jj in range(side - 1, j, -1):
        if mtx[i][jj] >= to_check:
            break
    else:
        return True
    for ii in range(0, i):
        if mtx[ii][j] >= to_check:
            break
    else:
        return True
    for ii in range(side - 1, i, -1):
        if mtx[ii][j] >= to_check:
            break
    else:
        return True
    return False

def visible_trees(trees):
    side = len(trees)
    v_trees = side * 4 - 4
    for i in range(1, side - 1):
        for j in range(1, side - 1):
            if (check_tree(trees, i, j)):
                v_trees += 1
    return (v_trees)

def calculate_view(mtx, i, j):
    to_check = mtx[i][j]
    l_view = 1
    r_view = 1
    u_view = 1
    d_view = 1
    side = len(mtx)
    for jj in range(j - 1, 0, -1):
        if mtx[i][jj] < to_check:
            l_view += 1
        else:
            break
    for jj in range(j + 1, side - 1):
        if mtx[i][jj] < to_check:
            r_view += 1
        else:
            break
    for ii in range(i - 1, 0, -1):
        if mtx[ii][j] < to_check:
            u_view += 1
        else:
            break
    for ii in range(i + 1, side - 1):
        if mtx[ii][j] < to_check:
            d_view += 1
        else:
            break
    return l_view * r_view * u_view * d_view

def find_best_view(trees):
    side = len(trees)
    best_view = 0
    for i in range(1, side - 1):
        for j in range(1, side - 1):
            view = calculate_view(trees, i, j)
            if view > best_view:
                best_view = view
    return (best_view)
            
def get_tot_sum(file_name):
    with open(file_name, 'r') as fd:
        trees = create_matrix(fd.readlines())
        return (visible_trees(trees))

def get_best_view(file_name):
    with open(file_name, 'r') as fd:
        trees = create_matrix(fd.readlines())
        return (find_best_view(trees))

if __name__ == "__main__":
    print("number visible trees:", get_tot_sum("..\\input.txt"))
    print("best view:", get_best_view("..\\input.txt"))