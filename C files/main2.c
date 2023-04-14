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
    filename3[0] = '\0';
	strcpy(filename3, argv[3]);
    char username[50];
    username[0] = '\0';
    strcpy(username,argv[1]);
    char password[50];
    password[0] = '\0';
    strcpy(password,argv[2]);

    bool out = Login(username, password, filename3);
    if(out == true){
        return 0;
    }
    return 1;

}
