#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "../Header files/HashTable.h"
#include "../Header files/AccountMenagment.h"
#include "../Header files/SaveHm.h"	

uint32_t HashFunction(uint32_t key, uint32_t M){

	

	return key % M;
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

	else{
		temp = Table->table[HashKey]->head;
			while(temp->next){
				temp = temp->next;
			}
		temp->next = newnode;
	}

	return 0;
}

void* Search(struct HashMap *map, uint32_t key){

	LIST head = map->table[HashFunction(key, map->size)]->head;

	return head;

}

int Delete(struct HashMap *map, uint32_t key){
	
	struct bin *b = map->table[HashFunction(key, map->size)];
	
	LIST temp = NULL;

	while(b->head){
		temp = b->head->next;
		free(b->head);
		b->head = temp;
	}
	free(map->table);
	free(map);
	return 0;
}

