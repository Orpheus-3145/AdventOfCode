# include <unistd.h>
# include <fcntl.h>
# include <stdio.h>

int result_round(int a, int b)
{
    int result;

    result = a - b;
    if (! result)
        return (3);
    if (a == 1)
        return (6 * (result == -1));
    else
        return (6 * (result != 1));
}

void find_total_coded(char* file_name)
{
    char round[4];
    int fd;
    int n_1;
    int n_2;
    int result;

    fd = open(file_name, O_RDONLY);
    result = 0;
    while (read(fd, round, 4))
    {
        n_1 = round[0] - 'A' + 1;
        n_2 = round[2] - 'X' + 1;
        result += result_round(n_1, n_2) + n_2;
    }
    printf("%d\n", result);
    close(fd);
    
}

int find_expected(int input, int result)
{
    if (result == 1)        // loss
        return (input - 1 + 3 * (input == 1));
    else if (result == 2)   // draw
        return (input);
    else                    // win
        return (input + 1 - 3 * (input == 3));
}

void find_total_encoded(char* file_name)
{
    char round[4];
    int fd;
    int n_1;
    int n_2;
    int result;
    int total;

    fd = open(file_name, O_RDONLY);
    total = 0;
    while (read(fd, round, 4))
    {
        n_1 = round[0] - 'A' + 1;
        result = round[2] - 'X' + 1;
        n_2 = find_expected(n_1, result);
        total += result_round(n_1, n_2) + n_2;
    }
    printf("%d\n", total);
    close(fd);
    
}

int main()
{
    find_total_coded("../input.txt");
    find_total_encoded("../input.txt");
	return (0);
}
