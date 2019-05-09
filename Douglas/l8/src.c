#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *service = "";
char *auth = "";
char *login = "";

int main()
{
	char	*input;
	int		i;
	char	*cmp;

	i = 0;
	printf("%p, %p \n", auth, service);
	if (0 != fgets(input, 0x80, stdin))
	{
        if (0 == strncmp("auth ", input, 5))
		{
			auth = malloc(4);
            if (strlen((input+5)) <= 0x1e)
                strcpy(auth, (input+5));
		}
        if (0 == strncmp("reset", input, 5))
            free(auth);
        if (0 == strncmp("service", input, 7))
            service = strdup((input + 7));
        if (0 == strncmp("login", input, 5))
        {
            if (auth[0x20] != 0)
                system("/bin/sh");
            else
                fwrite("Password:\n", 1, 0xa, stdout);
        }
	}
	return (0);
}
