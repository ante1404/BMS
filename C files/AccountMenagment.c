#include <alloca.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "../Header files/AccountMenagment.h"
#include "../Header files/HashTable.h"
#include "../Header files/SaveHm.h"

void CreateAccount(char *data_file, char *hash_map){

	//argv[1] is the name of the of the  file containing the data for creating account.
	FILE *data = fopen(data_file, "r");
	char buffer[50][2048];
	int i = 0;

	struct HashMap *Map = ReadHm(hash_map);

	//Read data from file into buffer
	while(!feof(data)){
	
		fgets(buffer[i], sizeof(buffer), data);
		i++;
	}

	char name[50];
	strcpy(name, buffer[0]);
	int len = strlen(buffer[0]);
	if (buffer[0][len-1] == '\n') {
		name[len-1] = '\0';
	}
	strcat(name, ".txt");
	FILE *account = fopen(name, "w");

	for (int i = 0; i < 50; i++) {
	
		fprintf(account, "%s", buffer[i]);
	}

	fclose(account);
	fclose(data);
	uint32_t key = StrToInt(buffer[2]);
	Insert(key, Map, name);
	WriteHm(Map, hash_map);

}

bool Login(char *username, char *password, char *hash_map){

	struct HashMap *map = ReadHm(hash_map);


	for (int i = 0; i < map->size; i++) {
		
		struct bin *b = map->table[i];
		if (b->head != NULL) {
			


		}
			
	}

	return true;
}

uint32_t StrToInt(char *password){
	
	uint32_t key = 0;

	int len = strlen(password);
	if (password[len-1] == '\n') {
		password[len-1] = '\0';
	}

	for (int i = 0; i < strlen(password); i++) {
		key += password[i];
	}

	return key;
}
