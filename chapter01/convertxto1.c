#include <stdio.h>

int convert()
{
    char x;
    int digitx;
    int numx = 0 ;
    while(x != ' ') {
        scanf("%c", &x);
        if (x != ' ') {
            digitx = x - '0';
            numx = numx*10 + digitx ;
        }
    }
    return numx;
}

main() {
    int numx;
    numx = convert();
    printf("%d\n",numx);
}



