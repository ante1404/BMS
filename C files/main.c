#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "../Header files/FinanceMenagment.h"
#include "../Header files/HashTable.h"
#include "../Header files/SaveHm.h"
#include "../Header files/AccountMenagment.h"

int main(int argc, char *argv[]){

	char data[50];
    strcpy(data, argv[2]);
    char filename3[50];
    strcpy(filename3, argv[1]);

    /*
    struct HashMap *map = CreateHM(100);

    bool out = Login(username, password, filename3);
    if(out == true){
        return 0;
    }
    */
    char buffer[50][2048];
    FILE *card_type = fopen(data, "r");
    int i = 0;
    while (!feof(card_type))
    {
        fgets(buffer[i], sizeof(buffer), card_type);
        i++;
    }
    int visa[2] = {4, 16};
    int mastercard[2] = {5, 16};
    int amex[2] = {37, 15};

    char *acc = CreateAccount(data, filename3);

    printf("%s",acc);

    int card = 1;
    _strlwr(buffer[17]);

    int n = 0;
    if (strcmp(buffer[17], "visa\n") == 0){
        card = CreditCardCreation(acc, filename3,visa);
    }
    else if(strcmp(buffer[17], "mastercard\n") == 0){
        card = CreditCardCreation(acc, filename3,mastercard);
    }
    else if(strcmp(buffer[17], "amex\n") == 0){
        card = CreditCardCreation(acc, filename3,amex);

    }
    return 0;
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

