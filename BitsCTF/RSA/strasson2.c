#include <stdio.h>

int main() {
    int i;
    double sum; // Change sum to double for accurate floating-point arithmetic
    
    sum = 0;
    for (i = 0; i < 9; i++) {
        sum += 0.1;
    }
    printf("%lf", sum); // Use %lf to print double
    return 0;
}
