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

	struct HashMap *MAP = ReadHm(hash_map);
	
	char c;
	char buffer[50];
	int i = 0;
	char name[50];
	FILE *account = NULL;
	while((c = fgetc(data)) != EOF){
		buffer[i] = c;
		i++;
		//
		if (c == '/' && i == 0) {
			buffer[i] = '\0';
			strcpy(name, buffer);
			account = fopen(name, "w");

		}
		fprintf(account, "%s", buffer);
	}

	Insert(4353, MAP, name);

}
