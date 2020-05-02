//Problem Set 2 - March 2020 Readability

#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int main(void)
{
    string text = get_string("Text: ");
    int lettercount = 0;
    int wordcount = 1;
    int sentencecount = 0;

// calculate counts of words
    for (int i = 0; i < strlen(text); i++)
    {
        if ((text[i] >= 'a' && text[i] <= 'z') || (text[i] >= 'A' && text[i] <= 'Z'))
        {
            lettercount++;
        }
        else if (text[i] == ' ')
        {
            wordcount++;
        }
        else if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentencecount++;
        }
    }

// we will printf("letters: %i; words: i% ; sentences: %i\n", lettercount, wordcount, sentencecount);

    float grade = 0.0588 * (100 * (float) lettercount / (float) wordcount) - 0.296 * (100 * (float) sentencecount / (float) wordcount) - 15.8;
    if (grade < 16 && grade >= 0)
    {
        printf("Grade %i\n", (int) round(grade));
    }
    else if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Before Grade 1\n");
    }
}
