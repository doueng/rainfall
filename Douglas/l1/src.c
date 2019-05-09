#include <stdio.h>
#include <stdlib.h>

int run()
{
	fwrite("Good... Wait what?\n",
		   1,
		   0x13,
		   stdout);
	return (system("/bin/sh"));
}

int main()
{
	char padd[0x50];
	char *g = &padd[0x40];
	return gets(g);
}
