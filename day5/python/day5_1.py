def create_matrix(file_name):
    mtx = []
    for i in range(9):
        with open(file_name, "r") as f:
            mtx.append([])
            while True:
                line = f.readline()[i * 4:]
                if not line:
                    break
                elif line[0] != '[':
                    continue
                else:
                    mtx[i].append(line[1:2])
            mtx[i].reverse()
    return mtx


def get_numbers(file_name):
    with open(file_name, 'r') as f:
        for line in f.readlines():
            if line[0] == 'm':
                yield isolate_numbers(line)


def isolate_numbers(line):
    org_i = int(line[line.index('f') + 5]) - 1
    dst_i = int(line[line.index('f') + 10]) - 1
    n = int(line[line.index('m') + 5: line.index('f') - 1])
    return n, org_i, dst_i


def read_sequence(file_name):
    mtx = create_matrix(file_name)
    for n, org_i, dst_i in get_numbers(file_name):
        
        for j in range(n):
            mtx[dst_i].append(mtx[org_i].pop())
    return [mtx[i][-1] for i in range(9)]


if __name__ == "__main__":
    print("sequence is:", read_sequence("../input.txt"))
