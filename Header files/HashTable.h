#ifndef HASH_TABLE_H
#define HASH_TABLE_H

#include "stdint.h"
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
	struct Node *head;
};

struct HashMap
{
	struct bin **table;
	uint32_t size;
};



uint32_t HashFunction(uint32_t key,uint32_t M);
struct HashMap *CreateHM(uint32_t size);
struct Node *Newnode(uint32_t key, struct HashMap *Table, char fn[50]);
void InsertElement(struct HashMap *map, uint32_t key, char fn[50]);
void* Search(struct HashMap *map, uint32_t key);
int Delete(struct HashMap *map);


#endif
