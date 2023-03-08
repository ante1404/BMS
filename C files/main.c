#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include "../Header files/HashTable.h"
#include "../Header files/SaveHm.h"
#include "../Header files/Testhm.h"



int main(int argc, char *argv[]){

	char filename3[50];
	strcpy(filename3, argv[1]);


    struct HashMap *MAP = CreateHM(100);

    // Import 10 files into the hash map
    char filenames[10][50] = {"file021aad1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt", "file6.txt", "file7.txt", "file8.txt", "file9.txt", "file10.txt"};
    char content[50] = "Bunch of fucking idiots\n";
    uint32_t keys[10] = {24680,55555,12312, 234, 19, 2, 457,567,345,7897};
    
    for (int i = 0; i < 10; i++) {
        char filename[50];
        strcpy(filename, filenames[i]);
        FILE *fp = fopen(filename, "w");
        fprintf(fp, "%s", content);
        fclose(fp);
        Insert(keys[i], MAP, filename);
    }

    // Print the pointers for each bin
    for (int i = 0; i < MAP->size; i++) {
        struct bin *b = MAP->table[i];
        if (b->head != NULL)
        {
            printf("filename = %s, keys =%d\n", b->head->filename, b->head->key);
        }
    }

    // Export the hash map to a file
    WriteHm(MAP, filename3);

    // Read the hash map from the file and print the contents
    struct HashMap *map = ReadHm(filename3);
    for (int i = 0; i < map->size; i++) {
        struct bin *b = map->table[i];
        if (b->head != NULL)
        {
            printf("Pointer = %p, Key = %d, Filename = %s\n", b->head, b->head->key, b->head->filename);
        }
    }
    printf("\n");

    return 0;
	
}

