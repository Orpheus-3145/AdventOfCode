import re

def append_entity(line, tree):
    if line.startswith("dir"):
        return line.split(' ')[1]
    elif not line.startswith("$"):
        return int(line.split(' ')[0])
    else:
        return None

def get_total_sum(dir_tree)
{
    int 
}
def sum_dir_tree(file_name):
    dir_tree = []
    with open(file_name, 'r') as fd:
        while True:
            line = fd.readline()
            if not line:
                return dir_tree
            if re.search("$ cd [^.]", line):
                print(line)
            # if line.startswith("$ ls"):
            #     dir_tree.append({dir_name: "", dir_list: [], size_dir: 0})
            #     line = fd.readline()


if __name__ == "__main__":
    print("total sum dirs:", sum_dir_tree("..\\input.txt"))