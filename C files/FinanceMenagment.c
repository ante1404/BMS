#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
#include "../Header files/HashTable.h"
#include "../Header files/SaveHm.h"
#include "../Header files/AccountMenagment.h"
#include "../Header files/FinanceMenagment.h"


int CreditCardCreation(char *account, char *hash_map, int card_info[]){

    char buffer[50][2048];
    time_t t;
    srand(time(NULL));

    FILE *data = fopen(account, "a+");
    struct HashMap *map = ReadHm(hash_map);

    int i = 0;
    char card1[50];
    int n = 0;

    while (!feof(data))
    {
        fgets(buffer[i], sizeof(buffer), data);
        i++;
    }
    if (card_info[1] == 15){

        while (1)
        {
            int *card;
            card = (int*)malloc(card_info[1] * sizeof(int));
            memset(card, 0, card_info[1] * sizeof(int));
            card[0] = 3;
            card[1] = 7;

            for (int i = 2; i < card_info[1]; i++)
            {
                card[i] = rand() % 10;
            }

            int check = LuhnAlgo(card, card_info[1]);
            if (check == 0)
            {
                n = card_info[1];
                for (int i = 0; i < n; i++) {
                    if (i == 0)
                    {
                        fprintf(data, "\n");
                    }
                    fprintf(data, "%d", card[i]);
                }
                break;
            }
        }
    }
    else{

        while (1)
        {
            int *card;
            card = (int*)malloc(card_info[1] * sizeof(int));
            memset(card, 0, card_info[1] * sizeof(int));
            card[0] = card_info[0];

            for (int i = 1; i < card_info[1]; i++)
            {
                card[i] = rand() % 10;
            }
            int check = LuhnAlgo(card, card_info[1]);
            if (check == 0)
            {
                n = card_info[1];
                n = card_info[1];
                for (int i = 0; i < n; i++) {
                    if (i == 0)
                    {
                        fprintf(data, "\n");
                    }
                    fprintf(data, "%d", card[i]);
                }

                break;
            }
        }
    }

    char temp[21];
    int ban_nums[19];
    memset(ban_nums,0, 19 * sizeof(int));
    for (int i = 0; i < 9; i++)
    {
        ban_nums[i] = rand() % 10;
        sprintf(temp + i * 2, "%02X", ban_nums[i]);
    }
    char iban[50] = "HR";
    strcat(iban, temp);


    fprintf(data, "\n%s\n", iban);
    fprintf(data, "%s\n", card1);

    fclose(data);

    return 0;

}

int LuhnAlgo(int card_num[], size_t n){


    int multiplyd_nums = 0;
    int other_nums = 0;
    int sum = 0;
    int temp = 0;
    int temp2= 0;

    if (n == 15){

        for (int i = 0; i < n; i++){
            if (i % 2 != 0){

                multiplyd_nums = card_num[i] * 2;
                if (multiplyd_nums > 9){

                    temp = multiplyd_nums % 10;
                    temp2 = multiplyd_nums / 10;
                    sum += temp + temp2;
                }
                else{
                    sum += multiplyd_nums;
                }
            }
            else{
                other_nums+=card_num[i];
            }
        }
        sum += other_nums;

        if (sum % 10 == 0)
        {
            return 0;
        }
        else{
            return 1;
        }
    }


    for (int i = 0; i < n; i++)
    {
        if (i % 2 == 0)
        {
            multiplyd_nums = card_num[i] * 2;
            if (multiplyd_nums > 9)
            {
                temp = multiplyd_nums % 10;
                temp2 = multiplyd_nums / 10;
                sum += temp + temp2;
            }
            else{
                sum += multiplyd_nums;
            }
        }
        else{
            other_nums+=card_num[i];
        }
    }
    sum += other_nums;

    if (sum % 10 == 0)
    {
        return 0;
    }

    return 1;

}

