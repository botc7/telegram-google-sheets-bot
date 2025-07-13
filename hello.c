#include <stdio.h>
int main () {
#if defined(_WIN32)
printf("hello, windows\n");
#elif defined(__linux__)
printf("hello, linux\n");
#elif defined(__APPLE__)
printf("hello, Apple\n");
#elif defined(BSD)
printf("hello, BSD\n");
#endif
}