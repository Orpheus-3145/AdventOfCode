import re

class Node():
    def __init__(self, dir_name = ""):
        self.dir_name = dir_name
        self.total_size = 0
        self.subdirs = []
        self.parent = None
    
    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return not self.subdirs

    def add_subdir(self, node):
        node.parent = self  
        self.subdirs.append(node)

    def add_file(self, file_size):
        self.total_size += file_size

    def __str__(self):
        return self.dir_name

    def size_node(self):
        tot = self.total_size
        if self.is_leaf():
            return tot
        else:
            return tot + sum([dir.size_node() for dir in self.subdirs])
        

class Tree():
    def __init__(self):
        self.root = None
        self.sub_elements = []

    def new_node(self, node, parent):
        if parent is not None:
            parent.add_subdir(node)
        else:
            if self.root is None:
                self.root = node
        self.sub_elements.append(node)

    def get_node(self, name):
        return self.sub_elements[name]

    def root(self):
        return self.root

    def elems_greater_than_max(self, max):
        tot = 0
        for nodes in [node for node in self.sub_elements if node.size_node() < max]:
            tot += nodes.size_node()
        return tot

    def find_smallest_dir(self, max):
        return sorted([dirs.size_node() for dirs in self.sub_elements if dirs.size_node() > max])[0]


class FileParser():
    def __init__(self, file_name, max_dir_size=100000):
        self.fd = open(file_name, 'r')
        self.max_dir_size = max_dir_size
        self.tree_obj = None
        self.space_available = 70000000
        self.space_to_be_empty = 30000000
        self.space_occupied = 0
        self.space_empty = 0
        self.space_to_free = 0

    def start_parsing(self):
        self.tree_obj = Tree()
        new_node = None
        parent_node = None
        for line in [l.rstrip() for l in self.fd]:
            if re.search(r"\$ cd ([a-z//])", line):
                new_node = Node(line.split()[2])
                self.tree_obj.new_node(new_node, parent_node)
                parent_node = new_node
            elif line == "$ cd ..":
                parent_node = parent_node.parent
            elif re.search(r"^[0-9]", line):
                new_node.add_file(int(line.split()[0]))
    
    def print_tree(self):
        if self.tree_obj is not None:
            for nodes in self.tree_obj.sub_elements:
                print(nodes.dir_name, nodes.size_node())

    def sum_dirs_under_max(self):
        tot = self.tree_obj.elems_greater_than_max(self.max_dir_size)
        print("somma di tutti gli elementi con dimensione inferiore a {}: {}".format(self.max_dir_size, tot))
    
    def max_dir_to_free(self):
        self.space_occupied = self.tree_obj.root.size_node()
        self.space_empty = self.space_available - self.space_occupied
        self.space_to_free = self.space_to_be_empty - self.space_empty
        tot = self.tree_obj.find_smallest_dir(self.space_to_free)
        print("size cartella da eliminare più piccola maggiore di {}: {}".format(self.space_to_free, tot))

            

if __name__ == "__main__":
    parser = FileParser("..\\input.txt")
    parser.start_parsing()
    parser.sum_dirs_under_max()
    parser.max_dir_to_free()