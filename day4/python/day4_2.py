def find_included_sectors(file_name):
    tot_count = 0
    with open(file_name, "r") as f:
        for elf1, elf2 in [sectors.split(',') for sectors in f.readlines()]:
            start1, end1 = [int(sector) for sector in elf1.split('-')]
            start2, end2 = [int(sector) for sector in elf2.split('-')]
            if (end1 >= start2 and end2 >= start1) or (end2 >= start1 and end1 >= start2):
                tot_count += 1
    return(tot_count)
    

if __name__ == "__main__":
    print("tot overlapped couples:", find_included_sectors("../input.txt"))