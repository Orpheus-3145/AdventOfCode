from collections import Counter

def unique(strng):
    cnt_dict = Counter(strng)
    for count in cnt_dict.values():
        if count != 1:
            return False
    return True


def find_marker_position(file_name, size_marker):
    marker = ""
    tot_chars = 0
    with open(file_name, 'r') as fd:
        while True:
            char = fd.read(1)
            marker += char
            tot_chars += 1
            if len(marker) == size_marker:
                if unique(marker):
                    return tot_chars
                else:
                    marker = marker[1:]
            

if __name__ == "__main__":
    print("marker position:", find_marker_position("..\\input.txt", 4))
    print("marker position:", find_marker_position("..\\input.txt", 14))