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
    

   //struct HashMap *map = CreateHM(100);
    

    CreateAccount(argv[2], filename3);
    
    struct HashMap *map = ReadHm(filename3);
    for (int i = 0; i < map->size; i++) {
        struct bin *b = map->table[i];
        if (b->head != NULL)
        {   
            while (b->head) {
                printf("Pointer = %p, Key = %d,index = %d, Filename = %s, next pointer = %p\n", b->head, b->head->key,i, b->head->filename, b->head->next);
                b->head = b->head->next;

            }
        }

    }
    printf("\n");

   // WriteHm(map, filename3);


    return 0;
	
}

