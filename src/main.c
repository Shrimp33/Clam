// Calls main.py
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    char buffer[1024];
    char src[256];
    char out[256];
    printf("Enter source file: ");
    scanf("%s", src);
    printf("Enter output file: ");
    scanf("%s", out);
    sprintf(buffer, "python main.py %s %s", src, out);
    system(buffer);
    printf("%s\n", buffer);
    printf("Done.\n");
    return 0;
}