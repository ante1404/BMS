#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "../Header files/FinanceMenagment.h"
#include "../Header files/HashTable.h"
#include "../Header files/SaveHm.h"
#include "../Header files/AccountMenagment.h"

int main(int argc, char *argv[]){

	char filename3[50];
	strcpy(filename3, argv[3]);
    char username[50];
    strcpy(username,argv[1]);
    char password[50];
    strcpy(password,argv[2]);



    //struct HashMap *map = CreateHM(100);

    //CreateAccount("Data.txt", filename3);


    bool out = Login(username, password, filename3);
    if(out == true){
        return 0;
    }


    struct HashMap *map = ReadHm(filename3);
    for (int i = 0; i < map->size; i++) {
        struct bin *b = map->table[i];
        if (b->head != NULL)
        {
           	LIST curr = b->head;
       		while (curr) {
            	printf("Pointer = %p, Key = %d, index = %d, Filename = %s, next pointer = %p\n", curr, curr->key, i, curr->filename, curr->next);
            	curr = curr->next;
			}
        }
    }
    printf("\n");
    WriteHm(map, filename3);
    return 1;

}
