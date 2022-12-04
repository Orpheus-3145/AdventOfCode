def find_included_sectors(file_name):
    tot_count = 0
    with open(file_name, "r") as f:
        for elf1, elf2 in [sectors.split(',') for sectors in f.readlines()]:
            start1, end1 = [int(sector) for sector in elf1.split('-')]
            start2, end2 = [int(sector) for sector in elf2.split('-')]
            if (start1 >= start2 and end1 <= end2) or (start2 >= start1 and end2 <= end1):
                tot_count += 1
    return(tot_count)
    

if __name__ == "__main__":
    print("tot contained couples:", find_included_sectors("../input.txt"))