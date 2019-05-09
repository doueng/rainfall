#define    _GNU_SOURCE
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main (int argc, char **argv)
{
    gid_t gid;
    uid_t uid;
    char  *shell[2];

    if (atoi(*(argv + 1)) == 0x1a7)
    {
        shell[0] = strdup("/bin/sh");
        shell[1] = NULL;
        gid = getegid();
        uid = geteuid();
        setresgid(gid, gid, gid);
        setresuid(uid, uid, uid);
        execv("/bin/sh", shell);
        return 0;
    }
    fwrite("No !\n", 0x1, 0x5, stderr);
    return 0;
}
