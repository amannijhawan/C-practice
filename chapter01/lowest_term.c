#include<stdio.h>
#include "euclids.h"

struct fraction {
    int num;
    int den;
};

struct fraction lowest_term(struct fraction original) {
    struct fraction lowest;
    int gcd;
    gcd = iterative_gcd(original.num, original.den) ;
    lowest.num = original.num / gcd ;
    lowest.den = original.den / gcd ;
    return lowest ;
}

main()
{
    struct fraction original ;
    struct fraction lowest;
    original.num = 5;
    original.den = 15;

    lowest = lowest_term(original);
    printf("result %d/%d\n", lowest.num,lowest.den);
}

