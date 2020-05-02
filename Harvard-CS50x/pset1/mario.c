#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //get integer between 1 and 8
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);
    for (int i = 0; i < n; i++)
    {

        for (int j = n - 1; j > i; j--)
        {
            printf(" ");
        }
       
        for (int k = -1; k < i; k++)
        {
            printf("#");
        }
        printf("\n");
    }
}
