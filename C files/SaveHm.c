#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include "../Header files/HashTable.h"

struct Data{
	uint32_t key;
	char filename[50];
	uint32_t empty;
};



void WriteHm(struct HashMap *map, char *filename){

	FILE *HM = fopen(filename, "wb");
    if (HM == NULL)
    {
        return;
    }
    fwrite(&map->size, sizeof(uint32_t), 1, HM);
    for (int i = 0; i < map->size; i++)
    {
        struct bin *b = map->table[i];
        if (b->head != NULL)
        {
            while (b->head) {
                fwrite(&b->head->key, sizeof(uint32_t), 1, HM);
                int len = strlen(b->head->filename);
                fwrite(&len, sizeof(int), 1, HM);
                fwrite(b->head->filename, len, 1, HM);
                b->head = b->head->next;
            }
        }
    }
    fclose(HM);

}

struct HashMap *ReadHm(char *filename) {
    FILE *fp1 = fopen(filename, "rb");

    uint32_t size = 0;
    fread(&size, sizeof(uint32_t), 1, fp1);

    struct Data *data = (struct Data*) malloc(size * sizeof(struct Data));

    int i = 0;
    int len = 0;
    while (fread(&data[i].key, sizeof(uint32_t), 1, fp1))
    {
        fread(&len, sizeof(int), 1 , fp1);
        fgets(data[i].filename, len + 1, fp1);
        //data[i].filename[len] = '\0'; // add null terminator
        data[i].empty = 1;
        i++;
    }
    struct HashMap *Table = CreateHM(size);
    for (int i = 0; i < size; i++)
    {
        if (data[i].empty == 1)
        {
            Insert(data[i].key, Table, data[i].filename);
        }
        
    }
    fclose(fp1);

    return Table;
}

