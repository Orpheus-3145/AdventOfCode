def find_priority_badge(group):
	for char in group[0]:
		if char in group[1] and char in group[2]:
			print("common char -->", char)
			if char >= 'a' and char <= 'z':
				return ord(char) - ord('a') + 1
			elif char >= 'A' and char <= 'Z':
				return ord(char) - ord('A') + 27


def sum_comm_ele(file_name):
	total = 0
	group = []
	with open(file_name, "r") as f:
		for line in f.readlines():
			group.append(line)
			if len(group) == 3:
				total += find_priority_badge(group)
				group.clear()
	return(total)


if __name__ == "__main__":
	print("total badge priorities:", sum_comm_ele("../input.txt"))