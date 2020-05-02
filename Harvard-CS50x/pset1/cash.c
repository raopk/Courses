#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    float change;
    do
    {
        change = get_float("Change owed: ");
    }      
    while (change < 0);
    
    //convert change to int
    int coins = round(change * 100);
    
    //find out how many of each coin
    int counter = 0;
    while (coins > 24)
    {
        coins = coins - 25;
        counter ++;
    }
    while (coins > 9)
    {
        coins = coins - 10;
        counter ++;
    }
    while (coins > 4)
    {
        coins = coins - 5;
        counter ++;
    }
    counter = counter + coins;
    printf("%i\n", counter);
}
