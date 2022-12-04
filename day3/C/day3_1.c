# include <unistd.h>
# include <fcntl.h>
# include <stdio.h>

int find_priority_badge(char group[3][52])
{
    return (0);
}

void print_misplaced_item(char* file_name)
{
    FILE *fp;
    char line[3][52];
    //char* group[3];
    int count;
    int total;
    char* tmp;

    fp = fopen(file_name, "r");
    count = 0;
    total = 0;
    tmp = fgets(line[count], 52, (FILE*) fp);
    while (tmp)
    {
        printf("--> %s", tmp);
        if (count == 3)
        {
            total += find_priority_badge(line);
            count = 0;
            printf("%s%s%s\n", line[0], line[1], line[2]);
        }
        //printf("1) %s", line[0]);
        //if (count == 1)
        //    printf("2) %s", line[1]);
        //if (count == 2)
        //{
        //    printf("2) %s", line[1]);
        //    printf("3) %s", line[2]);
        //}
        count++;
        tmp = fgets(line[count], 50, (FILE*) fp);
    }
    fclose(fp);
    printf("total: %d\n", total);
}


int main()
{
    print_misplaced_item("../input.txt");
    return (0);
}