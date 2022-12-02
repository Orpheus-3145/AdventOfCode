# include <stddef.h>
# include <stdlib.h>
# include <unistd.h>
# include <fcntl.h>
# include <stdio.h>

int satoi(char *char_nbr)
{
    int nbr;
    
    nbr = 0;
    while(*char_nbr > '0' && *char_nbr < '9')
        nbr = (nbr * 10) + (*char_nbr++ - '0');
    return (nbr);
}

void check_max(int* max, int to_check)
{

}

int len_line(char *str)
{
    int cnt;

    cnt = 0;
    while(*str++)
        cnt++;
    return (cnt);
}
void find_max_kal(char* file_name)
{
    FILE *fp;
    char line[7];
    int total;
    int first_three[] = {0, 0, 0};
    int max;

    max = 0;
    total = 0;
    fp = fopen(file_name, "r");
    while (fgets(line, 8, (FILE*) fp) != NULL)
    {
        //printf("%s", line);
        if (*line != '\n')
            total += satoi(line);
        else
        {
            if (max < total)
            {
                max = total;
                printf("%d\n", max);
            }
            total = 0;
        }
    }
    fclose(fp);
    printf("max: %d\n", max);
}

int main()
{
    find_max_kal("../input.txt");
    return (0);
}