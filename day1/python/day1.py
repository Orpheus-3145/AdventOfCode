def read_and_fill(file_name):
    sum = 0
    top_three = [0, 0, 0]
    with open(file_name, "r") as f:
        line = f.readlines()
        for number in line:
            if number != "\n":
                sum += int(number)
            else:
                if top_three[0] <= sum:
                    top_three[2] = top_three[1]
                    top_three[1] = top_three[0]
                    top_three[0] = sum
                elif top_three[1] <= sum:
                    top_three[2] = top_three[1]
                    top_three[1] = sum
                elif top_three[2] <= sum:
                    top_three[2] = sum
                sum = 0
    return (top_three[0] + top_three[1] + top_three[2])

if __name__ == "__main__":
    print("max 3:", read_and_fill("..\input.txt"))
