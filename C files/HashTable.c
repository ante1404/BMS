#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "../Header files/HashTable.h"
#include "../Header files/CreateAccount.h"
#include "../Header files/SaveHm.h"
/*
int main(void){
		
	struct HashMap *MAP = NULL;
	MAP = CreateHM(100);

	FILE *cvs = NULL;
	char filename[50] = "demo.txt";

	FILE *cvs2 = fopen("demo2.txt", "w+");
	char filename2[50] = "demo2.txt";

	char *str2 = "Fuck you, world\n";
	fprintf(cvs2, "%s", str2);

	//Create a file and write some txt to it.
	cvs = fopen("demo.txt", "w+");
	char *str = "Hello, world\n";
	fprintf(cvs, "%s", str);

	Insert(cvs2, 19, MAP, filename2);
	Insert(cvs, 234, MAP, filename);
	fclose(cvs2);
	fclose(cvs);


	//find a head pointer and open its file and print the contents.
	LIST hed = Search(MAP, 234);

	FILE *fp = fopen(hed->filename, "r+");

	//Set the file pointer to end
	fseek(fp, 0, SEEK_END);
	//get the size of sile in bytes.
	long size = ftell(fp);
	//return file pointer to the beginning of the file.
	rewind(fp);

	char* buffer = (char*) malloc(size + 1);
	size_t result = fread(buffer, 1, size, fp);

	buffer[size] = '\0';
	printf("File contents: %s", buffer);

	free(buffer);
	fclose(fp);

	for(int i = 0; i < MAP->size; i++){
		struct bin *a = MAP->table[i];
		printf("%p\n", a->head);
	};
	char binf[50] =  "hm.bin";
		
	WriteHm(MAP, binf);

	*/	

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




