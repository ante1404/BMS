#include <alloca.h>
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
	Insert(12, Map, name);
	WriteHm(Map, hash_map);

}
