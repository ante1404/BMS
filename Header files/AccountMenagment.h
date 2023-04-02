#ifndef ACCOUNT_MENAGMENT_H
#define ACCOUNT_MENAGMENT_H
#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>

struct DOF
{
	int dd;
	int mm;
	int yyyy;
};

struct PersonalInfo
{
	uint64_t OIB[11];
    uint64_t phone_number[50];
	uint32_t sallary;
	uint32_t income;
	uint32_t debt;
	uint32_t monthly_expences;
};

struct Account
{
	uint32_t initial_deposit;
	uint32_t withdrawl;
	uint32_t deposit;
	signed long int account_balance;
};

struct Address
{
	char city[50];
	char state[50];
	char street[50];
	int house_number;
};


struct Person
{
	char name[50];
	char last_Name[50];
	char job_title[50];
	char email[50];
	char password[50];
	struct DOF dof;
	struct PersonalInfo personal_info;
	struct Account account;
	struct Address address;
};



void CreateAccount(char *data_file, char *hash_map);
uint32_t StrToInt(char *password);
bool Login(char *username, char *password, char *hash_map);


#endif
