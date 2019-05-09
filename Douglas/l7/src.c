#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdio.h>

int m()
{
	return (printf("%s - %d\n", (char*)0x8049960, (int)time(0)));
}

int main(int argc, char *argv[])
{
	int *first;
	int *second;

	first = malloc(8);
	*first = 1;
	first[1] = (int)malloc(8);

	second = malloc(8);
	*second = 2;
	second[1] = (int)malloc(8);

	strcpy((char*)(first[1]), *(argv+1));
	strcpy((char*)(second[1]), *(argv+2));

	fgets((char*)0x8049960,
		  0x44,
		  fopen("/home/user/level8/.pass", "r"));
	puts((char*)0x8048703);
}
