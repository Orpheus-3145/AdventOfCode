def read_and_fill(file_name):
    with open(file_name, "r") as f:
        return max([sum(list(map(int, meals.split('\n')))) for meals in f.read().split("\n\n")])
        
def read_and_fill_3(file_name):
    with open(file_name, "r") as f:
        return sum(sorted([sum(list(map(int, meals.split('\n')))) for meals in f.read().split("\n\n")], reverse=True)[:3])

if __name__ == "__main__":
    print("max 3:", read_and_fill("..\input.txt"))
    print("max 3:", read_and_fill_3("..\input.txt"))
