#include <unistd.h>
#include <stdio.h>

int main()
{
    char* argv[3];
    argv[0] = "python3";
    argv[1] = "FrontEnd_.py";
    argv[2] = NULL;

    execvp(argv[0], argv);

    return 0;
}