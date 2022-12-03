def find_comm_ele(str1, str2):
	for ele1 in str1:
		for ele2 in str2:
			if ele1 == ele2:
				if ele1 >= 'a' and ele1 <= 'z':
					return ord(ele1) - ord('a') + 1
				elif ele1 >= 'A' and ele1 <= 'Z':
					return ord(ele1) - ord('A') + 27

def find_pri_badge(group_line):
	first_sep = group_line.index()
	for char in group_line:
		


def remove_nl(line):
	if line[-1] == '\n':
		line = line[:-1]
	return line

def sum_comm_ele(file_name):
	total = 0
	count = 0
	group_line = ""
	with open(file_name, "r") as f:
		lines = f.readlines()
		for line in lines:
			if count < 3:
				# print("incrementing... ", count)
				count += 1
			else:
				# total += find_pri_badge(group_line)
				# printf("resetting... ")
				group_line += remove_nl(line) + "|"
				count = 1
				group_line = ""
			# print(count, remove_nl(line), "\n")
			print(group_line)
	return(total)

if __name__ == "__main__":
	print("sum priorities:", sum_comm_ele("../input.txt"))