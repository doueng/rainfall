int p(char *arg1, char *arg2)
{
    char buf[0x1000];

    puts(arg2);
    read(0, buf, 0x1000);
    // 0xa == \n
    *(strchr(buf, 0xa)) = 0;
    strncpy(arg1, buf, 0x14);
}

int pp(char *m)
{
    char s1[0x1c]; // ebp - 0x1c
    char s2[0x1c]; // ebp - 0x30
    int  len;

    p(s1, " - ");
    p(s2, " - ");
    strcpy(m, s2);
    len = strlen(s1);
    strcat(m, " ");
    strcat(m, s1);
}

int main()
{
    char m[0x24];

    pp(m);
    puts(m);
    return 0;
}

