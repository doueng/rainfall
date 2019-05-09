#include <stdio.h>
void main()
{
    int i = 10;
    int max = 0xffffff;
    printf("%%jx   (%jx)\n", max);
    printf("%%jx   (%jx)\n", i);
    printf("%%jx   (%jx)\n", &max);
    printf("%%p    (%p)\n", &max);
    /*printf("%%8qd  (%8jdx)\n", max);*/
    printf("%%8x   (%8x)\n", 10000000000000);
    printf("%%8x   (%8x)\n", 10);
    printf("%%8X   (%8X)\n", 10);
    printf("%%.8d  (%1.d)\n", 10);
    printf("%%p    (%p)\n", &i);
    printf("%%.8d  (%.8d)\n", 10);
    printf("%%8d   (%8d)\n", 10);
    printf("%%8.d  (%8.d)\n", 10);
    printf("%%64.s (%64.s)\n");
}
