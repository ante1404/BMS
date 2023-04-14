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

        Table->table[i]->head = NULL;


	}
	return Table;
}


struct Node *Newnode(uint32_t key, struct HashMap *Table, char fn[50]){

    struct Node *newnode = (struct Node*) malloc(sizeof(struct Node));
	if(newnode == NULL){
		return NULL;
	}
	strcpy(newnode->filename, fn);
	newnode->key = key;
	newnode->next = NULL;

	return newnode;
}

void InsertElement(struct HashMap *map, uint32_t key, char fn[50]){
        struct Node *curr = NULL;
        struct Node *newnode = Newnode(key, map, fn);
        uint32_t HashKey = HashFunction(key, map->size);
        if(map->table[HashKey]->head == NULL){

            map->table[HashKey]->head = newnode;
        }
        else{
            curr = map->table[HashKey]->head;
            while(curr->next){
                curr = curr->next;
            }
            curr->next = newnode;
        }
}


void* Search(struct HashMap *map, uint32_t key){

	LIST head = map->table[HashFunction(key, map->size)]->head;

	return head;

}

int Delete(struct HashMap *map){

    struct Node *temp = NULL;
    struct Node *temp1 = NULL;

    for (int i = 0; i < map->size; i++) {
        if (map->table[i]->head != NULL) {
            temp = map->table[i]->head;
            while (temp) {
                temp1 = temp->next;
                free(temp);
                temp = temp1;
            }
        }
        free(map->table[i]);
    }

    free(map->table);
	free(map);
	return 0;
}

