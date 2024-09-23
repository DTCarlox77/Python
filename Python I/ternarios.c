# include <stdio.h>

int main() {

    int v = 50;
    int a = 50;
    int c = (a > 10) ? 10 : a;

    if (a > 10) {
        c = 10;
    } else {
        c = a;
    }
}