#include "functions.h"

long long factorial(int n) {
    long long res = 1;
    for (int i = 2; i <= n; ++i) res *= i;

    return res;
}


