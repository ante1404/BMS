#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <wchar.h>
#include <locale.h>
#include "../Header files/FinanceMenagment.h"
#include "../Header files/AccountMenagment.h"
#include "../Header files/HashTable.h"
#include "../Header files/SaveHm.h"


char *CreateAccount(char *data_file, char *hash_map){

	//argv[1] is the name of the of the  file containing the data for creating account.

	FILE *data = fopen(data_file, "r");
	if (data == NULL)
	{
		return NULL;
	}

    char buffer[50][2048];
    for (int i = 0; i < 50; i++) {
        memset(buffer[i], 0, 2048);
    }

	int i = 0;
	struct HashMap *Map = ReadHm(hash_map);

	//Read data from file into buffer
	while(!feof(data)){

		fgets(buffer[i], sizeof(buffer), data);
		i++;
	}

	char name[50] = "";
	char path[100] = "Path to folder containing Accounts";
	strcpy(name, buffer[0]);

	int len = 0;
    len = strlen(buffer[0]);
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
    InsertElement(Map, key, name);
	WriteHm(Map, hash_map);
    Delete(Map);

	char *acc;
	acc = (char*)malloc(100 * sizeof(char));
	strcpy(acc, path);
	return acc;

}


bool Login(char *username, char *password, char *hash_map){

	struct HashMap *map = ReadHm(hash_map);
	char buffer[50][2048];
	int j = 0;
    uint32_t key = StrToInt(password);
	key = HashFunction(key, map->size);
	struct bin *b = map->table[key];
	while (b->head)
	{

		char path[100] = "Path to folder containing Accounts";
		strcat(path, b->head->filename);
		FILE *acc = fopen(path, "r");
		while (!feof(acc))
		{
			fgets(buffer[j], sizeof(buffer), acc);
			j++;
		}

		int len = strlen(buffer[0]);
		int len2 = strlen(buffer[2]);

		if (buffer[0][len - 1] == '\n')
		{
			buffer[0][len - 1] = '\0';
			buffer[2][len2 - 1] = '\0';
		}
		if (strcmp(buffer[0], username) == 0 && strcmp(buffer[2], password) == 0)
		{
			printf("%s", path);
			Delete(map);
			return true;
		}
		b->head = b->head->next;
		j = 0;
		fclose(acc);

	}
    Delete(map);
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
