#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "../Header files/HashTable.h"
#include "../Header files/CreateAccount.h"
#include "../Header files/SaveHm.h"	

uint32_t HashFunction(uint32_t key, uint32_t M){

	uint32_t copy = key;
	uint32_t value = 1;
	uint32_t mod = 0;

	while(key != 0){

		mod = key % 10;
		value *= mod;
		key/= 10;
	}

	value = pow(value,3);

	return value % M;
}

struct HashMap *CreateHM(uint32_t size){

	struct HashMap *Table = (struct HashMap*) malloc(sizeof(struct HashMap));
	if(Table == NULL){
		return NULL;
	}
	Table->size = size;
	Table->table = (struct bin**) malloc(Table->size * sizeof(struct bin*));
	if(Table->table == NULL){
		return NULL;
	}

	for(uint32_t i = 0; i < Table->size; i++){
		Table->table[i] = (struct bin*) malloc(sizeof(struct bin));
		if(Table->table[i] == NULL){
			printf("FAILD");
			return NULL;
		}
		Table->table[i]->head = (struct Node*)malloc(sizeof(struct Node));
		Table->table[i]->head = NULL;
		
	}
	return Table;
}
int Insert(uint32_t key, struct HashMap *Table, char fn[50]){
		
	LIST temp = NULL;

	LIST newnode = (struct Node*) malloc(sizeof(struct Node));
	if(newnode == NULL){
		return 1;
	}
	strcpy(newnode->filename, fn);
	newnode->key = key;

	uint32_t HashKey = 	HashFunction(key, Table->size);
	newnode->next = NULL;

	if(Table->table[HashKey]->head == NULL){

		Table->table[HashKey]->head = newnode;
	}

	else
		temp = Table->table[HashKey]->head;
		while(temp){
			temp = temp->next;
		}
		temp = newnode;

	return 0;
}

void* Search(struct HashMap *map, uint32_t key){

	LIST head = map->table[HashFunction(key, map->size)]->head;

	return head;

}

int Delite(struct HashMap *map, uint32_t key){
	
	struct bin *b = map->table[HashFunction(key, map->size)];
	
	LIST temp = NULL;

	while(b->head){
		temp = b->head->next;
		free(b->head);
		b->head = temp;
	}

	return 0;
}

