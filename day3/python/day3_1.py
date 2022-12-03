def find_comm_ele(str1, str2):
	for ele1 in str1:
		for ele2 in str2:
			if ele1 == ele2:
				if ele1 >= 'a' and ele1 <= 'z':
					return ord(ele1) - ord('a') + 1
				elif ele1 >= 'A' and ele1 <= 'Z':
					return ord(ele1) - ord('A') + 27

def sum_comm_ele(file_name):
	common_ele = 0
	with open(file_name, "r") as f:
		lines = f.readlines()
		for line in lines:
			common_ele += find_comm_ele(line[:len(line) // 2], line[len(line) // 2:])
	return(common_ele)

if __name__ == "__main__":
	print("sum priorities:", sum_comm_ele("../input.txt"))