#ifndef SAVE_HM_H
#define SAVE_HM_H
#include "../Header files/HashTable.h"


struct Data {
    uint32_t key[100];
    char filename[50];
    uint32_t empty;
};


void WriteHm(struct HashMap *map, char *filename);
struct HashMap *ReadHm(char *filename);

#endif
