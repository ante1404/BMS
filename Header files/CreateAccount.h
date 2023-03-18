#ifndef CREATE_ACCOUNTS_H
#define CREATE_ACCOUNTS_H

#include <stdio.h>

void Cunt();

typedef int NUM;

struct DOF
{
	NUM dd;
	NUM mm;
	NUM yyyy;
};

struct PersonalInfo
{
	signed long int OIB[11];
    unsigned long int phone_number[50];
	unsigned int sallary;
	unsigned int income;
	unsigned int debt;
	unsigned int monthly_expences;
};

struct Account
{
	unsigned int initial_deposit;
	unsigned int withdrawl;
	unsigned int deposit;
	signed long int account_balance;
};

struct Address
{
	char city[50];
	char state[50];
	char street[50];
	NUM house_number;
};


struct Person
{
	char name[50];
	char last_Name[50];
	char job_title[50];
	char email[50];
	struct DOF dof;
	struct PersonalInfo personal_info;
	struct Account account;
	struct Address address;
};



#endif
