# include <stddef.h>
# include <stdlib.h>
# include <unistd.h>
# include <fcntl.h>
# include <stdio.h>

int simple_atoi(char *char_nbr)
{
    int nbr;
    
    nbr = 0;
    while(*char_nbr >= '0' && *char_nbr <= '9')
        nbr = (nbr * 10) + (*char_nbr++ - '0');
    return (nbr);
}

void check_max(int* max, int to_check)
{
    if (max[0] < to_check)
    {
        max[2] = max[1];
        max[1] = max[0];
        max[0] = to_check;
    }
    else if (max[1] < to_check)
    {
        max[2] = max[1];
        max[1] = to_check;
    }
    else if (max[2] < to_check)
        max[2] = to_check;
}

void find_max_kal(char* file_name)
{
    FILE *fp;
    char line[7];
    int total;
    int first_three[] = {0, 0, 0};

    total = 0;
    fp = fopen(file_name, "r");
    while (fgets(line, 7, (FILE*) fp) != NULL)
    {
        if (*line != '\n')
            total += simple_atoi(line);
        else
        {
            check_max(first_three, total);
            total = 0;
        }
    }
    fclose(fp);
    printf("tot 3 max: %d\n", first_three[0] + first_three[1] + first_three[2]);
}

int main()
{
    find_max_kal("../input.txt");
    return (0);
}