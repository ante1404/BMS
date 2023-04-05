#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <wchar.h>
#include <locale.h>
#include "../Header files/AccountMenagment.h"
#include "../Header files/HashTable.h"
#include "../Header files/SaveHm.h"


void CreateAccount(char *data_file, char *hash_map){
	
	//argv[1] is the name of the of the  file containing the data for creating account.
	
	FILE *data = fopen(data_file, "r");
	if (data == NULL)
	{
		return;
	}
	
	char buffer[50][2048];	
	int i = 0;
	struct HashMap *Map = ReadHm(hash_map);
	//Read data from file into buffer
	while(!feof(data)){

		//fread(&buffer[i], sizeof(char), 1, data);
		fgets(buffer[i], sizeof(buffer), data);
		i++;
	}

	char name[50];
	char path[100] = "C:/Users/Ante/Desktop/GUI/Accounts/";
	strcpy(name, buffer[0]);
	int len = strlen(buffer[0]);
	if (strcmp(&buffer[0][len-1], "\n") == 0) {
		name[len-1] = '\0';
	}
	
	strcat(name, ".txt");
	strcat(path, name);
	FILE *account = fopen(path, "w");
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
	char buffer[50][2048];
	int j = 0;

	for (int i = 0; i < map->size; i++) {
		
		struct bin *b = map->table[i];
		if (b->head != NULL) {
			while (b->head) {

				char path[100] = "C:/Users/Ante/Desktop/GUI/Accounts/";
				strcat(path, b->head->filename);
				FILE *acc = fopen(path, "r");
				while(!feof(acc)){
					fgets(buffer[j], sizeof(buffer), acc);
					j++;
				}
				int len = strlen(buffer[0]);
				int len2 = strlen(buffer[2]);
				
				if (buffer[0][len-1] == '\n') {
					buffer[0][len-1] = '\0';
					buffer[2][len2-1] ='\0';
				}
				if(strcmp(buffer[0], username) == 0 && strcmp(buffer[2], password) == 0){
					return true;
				}
				b->head = b->head->next;
				j=0;
				fclose(acc);
			}
		}
	}

	return false;
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
