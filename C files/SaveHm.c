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

    struct Node *temp = NULL;

    fwrite(&map->size, sizeof(uint32_t), 1, HM);
    for (int i = 0; i < map->size; i++)
    {
        struct bin *b = map->table[i];
        if (b->head != NULL)
        {
            temp = b->head;
            while (temp) {
                fwrite(&temp->key, sizeof(uint32_t), 1, HM);
                int len = strlen(temp->filename);
                fwrite(&len, sizeof(int), 1, HM);
                fwrite(temp->filename, len, 1, HM);
                temp = temp->next;
            }
        }
    }
    fclose(HM);

}

struct HashMap *ReadHm(char *filename) {

    FILE *fp1 = NULL;
    fp1 = fopen(filename, "rb");

    uint32_t size = 0;
    fread(&size, sizeof(uint32_t), 1, fp1);

    struct Data *data = NULL;
    data = (struct Data*) malloc(size * sizeof(struct Data));
    for (int i = 0; i < size; i++) {
        data[i].key = 0;
        data[i].empty = 0;
        memset(data[i].filename, 0, sizeof(data[i].filename));
    }

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
    struct HashMap *Table = NULL;
    Table = CreateHM(size);
    for (int i = 0; i < size; i++)
    {
        if (data[i].empty == 1)
        {
            InsertElement(Table,data[i].key ,data[i].filename);
        }

    }
    fclose(fp1);
    free(data);

    return Table;
}

