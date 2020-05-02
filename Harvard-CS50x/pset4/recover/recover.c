//Problem Set 4

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
// checks to make sure namefiles are specified correctly
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover image\n");
        return 1;
    }

    // This line will verify whether our card - memory card is opened
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        fprintf(stderr, "Could not open file %s.\n", argv[1]);
        return 1;
    }

    //Create variables we will use and for memory allocation
    FILE *img;
    char filename[7];
    unsigned char *bf = malloc(512);
    int end = 1000;
    int counter = 0;

    while (fread(bf, 512, 1, file))
    {
        // new jpg file found
        if (bf[0] == 0xff && bf[1] == 0xd8 && bf[2] == 0xff && (bf[3] & 0xf0) == 0xe0)
        {
            // close previous jpg file if those files exists
            if (counter > 0)
            {
                fclose(img);
            }

            // creates filename
            sprintf(filename, "%03d.jpg", counter);
            // open new image file
            img = fopen(filename, "w");

            // checkes if jpg file is created
            if (img == NULL)
            {
                fclose(file);
                free(bf);
                fprintf(stderr, "Could not create output JPG %s", filename);
                return 3;
            }

            counter++;
        }

        //if any jpg file exists writes on the file currently opened
        if (counter > 0)
        {
            fwrite(bf, 512, 1, img);
        }
    }

    //This will free up memory while closing files
    fclose(img);
    fclose(file);
    free(bf);
    return 0;
}
