#ifndef HASH_TABLE_H
#define HASH_TABLE_H

#include <stdio.h>
#include <stdint.h>

#define MAX 100000

typedef struct Node *LIST;
typedef struct HashMap *HM;


struct Node
{	
	LIST next;
	uint32_t key;
	char filename[50];
};

struct bin
{
	LIST head;
};

struct HashMap
{
	struct bin **table;
	uint32_t size;
};



uint32_t HashFunction(uint32_t key,uint32_t M);
struct HashMap *CreateHM(uint32_t size);
int Insert(uint32_t key, struct HashMap *Table, char fn[50]);
void* Search(struct HashMap *map, uint32_t key);
int Delite(struct HashMap *map, uint32_t key);


#endif
