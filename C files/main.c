#include <stdbool.h>
#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include "../Header files/HashTable.h"
#include "../Header files/SaveHm.h"
#include "../Header files/Testhm.h"
#include "../Header files/AccountMenagment.h"




int main(int argc, char *argv[]){

	char filename3[50];
	strcpy(filename3, argv[1]);
    char username[50] = "Ante";
    char password[50] = "ante";
    

    //struct HashMap *map = CreateHM(100);
    
    //CreateAccount("Data.txt", filename3);
    
    if(Login(username,password, filename3) == true){
        printf("WELCOME\n");
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
    return 0;
	
}

