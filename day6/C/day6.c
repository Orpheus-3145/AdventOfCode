#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

void add_element(char vect[14], char new_ele)
{
    int i;

    i = 0;
    while (i < 13)
    {
        vect[13 - i] = vect[12 - i];
        i++;
    }
    vect[0] = new_ele;
}

int check_vect(char vect[14])
{
    int i;
    int j;

    i = 0;
    while (i < 14)
    {
        j = 0;
        while (j < i)
        {
            if(vect[i] == vect[j])
                return (0);
            j++;
        }
        i++;
    }
    return (1);
}

int find_pos_marker(char* file_name)
{
    int fd;
    char inspector[14] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    int total;
    char char_read;
    fd = open(file_name, O_RDONLY);
    if (fd < 0)
        return (-1);
    total = 0;
    while(1)
    {
        if (read(fd, &char_read, 1) <= 0)
            return (0);
        else
            total++;
        add_element(inspector, char_read);
        if (total > 14 && check_vect(inspector))
            return (total);
    }
}

int main()
{
    printf("marker position: %d\n", find_pos_marker("..\\input.txt"));
    return (0);
}
