#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int unlekhmus(int given){
	int output = 15 - given;
	return output;
}

int unkaten(int given){
	given = (double) given;
	given = given/2;
	double output = cbrt(given);
	given = (int) output;
	return output;
}

int unmorgan(int given){
	int output = given - 2;
	return output;
}

int unlucas(int given){
	int output = given / 2;
	return output;
}

int unmiano(int given){
	int output = given * 2;
	return output;
}

void main(int argc, char *argv[]){
	int given = 0;
	int bonus = 0;
	if(argc != 2){
		return;
	}
	else{
		given = atoi(argv[1]);
		given = unlekhmus(given);
		given = unkaten(given);
		given = unmorgan(given);
		given = unlucas(given);
		given = unmiano(given);
		bonus = given + 1;
	}
	printf("(%d, %d)", given, bonus);
	return;
}
